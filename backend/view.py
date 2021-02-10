from flask import jsonify, request, session, Blueprint
from database import db, User, Story

VOTE_OPTIONS = ["0", "1/2", "1", "3", "5", "8", "15", "20", "50", "100", "?"]

app = Blueprint('temp', __name__)

_socketio = None


def get_socketio():
    global _socketio
    if not _socketio:
        from app import socketio
        _socketio = socketio
    return _socketio


def respond_with(message, http_status=200, **extra):
    result = {}
    result.update(extra)
    result["message"] = message
    return jsonify(result), http_status


@app.route('/', methods=['GET'])
def index():
    return jsonify("backend server up and running")


@app.route('/api', methods=['GET'])
def index_with_prefix():
    return jsonify("backend server up and running with prefix")


def hello():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1  # setting session data
    get_socketio().emit('ping', broadcast=True)
    return jsonify("Total visits: {}".format(session.get('visits')))


def ping_pong():
    from app import socketio
    socketio.emit('ping', broadcast=True)
    return jsonify('pong!')


def put_story():
    post_data = request.get_json()
    print(f"story: {post_data}")
    story = Story.query.first()
    if not story:
        story = Story("", "")
        db.session.add(story)
        db.session.commit()

    if "title" in post_data.keys():
        story.title = post_data.get("title")
    if "description" in post_data.keys():
        story.description = post_data.get("description")

    db.session.commit()

    get_socketio().emit('storyModified', broadcast=True)

    return respond_with('updated story')


def get_story():
    story = Story.query.first()
    if not story:
        return jsonify({'title': '', 'description': ''})
    return jsonify({'title': story.title, 'description': story.description})


def _all_users_have_voted():
    return all(u.has_voted for u in User.query.all())


def put_vote(username):
    if _all_users_have_voted():
        return jsonify("too late"), 403

    post_data = request.get_json()
    vote = post_data.get("vote")
    if vote not in VOTE_OPTIONS:
        return jsonify(f"Value {vote} not in allowed options", 400)
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify(f"User {username} does not exist", 404)
    user.has_voted = True
    user.vote = vote
    db.session.commit()
    get_socketio().emit('userVoted', {'User voted': user.id}, broadcast=True)
    get_socketio().emit('userJoined', {'User Joined': username}, broadcast=True)
    return respond_with(f"vote of {vote} accepted")


def delete_votes():
    print("deleting all votes")
    for u in User.query.all():
        u.has_voted = False
        u.vote = None
    db.session.commit()

    get_socketio().emit('votesCleared', {'Votes have been cleared': None}, broadcast=True)
    return respond_with("votes have been cleared")


def get_vote_options():
    return jsonify(VOTE_OPTIONS)


def post_login():
    if not request.is_json:
        return respond_with("Missing JSON body in request", 400)

    post_data = request.get_json()
    print(f"user login: {post_data}")
    username = post_data.get("username")
    if not username:
        return respond_with("Missing parameter 'username'", 400)

    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username, role_id=None)
        db.session.add(user)
        db.session.commit()
        print(f"created new user {user}")

    session.username = username
    get_socketio().emit('userJoined', {'User Joined': username}, broadcast=True)

    return respond_with(f"welcome {username}", 200, username=username)


def get_users():
    users = User.query.all()
    result = []

    if _all_users_have_voted():
        for user in users:
            result.append({"username": user.username, "vote": user.vote, 'hasVoted': True})
    else:
        for user in users:
            result.append({"username": user.username, "vote": "hidden", 'hasVoted': user.has_voted})

    return jsonify({"users": result})


def delete_user(username):
    print(f"deleting user {username}")

    user = User.query.filter_by(username=username).first()
    if not user:
        return "not found", 404
    try:
        db.session.delete(user)
        db.session.commit()
    except KeyError:
        pass

    get_socketio().emit('userJoined', {'User quit': username}, broadcast=True)
    return respond_with(f"deleted user {username}")
