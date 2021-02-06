from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_socketio import SocketIO

USERS = {
}
STORY = {
    "title": "(not yet set)",
    "description": "(not yet set)"
}
VOTE_OPTIONS = ["0", "1/2", "1", "3", "5", "8", "15", "20", "50", "100", "?"]
VOTES = {
}

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

app.config['SECRET_KEY'] = 'would become a secret in production...'
socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*",
                    path="/prefix/socket.io",
                    ping_timeout=20, manage_session=True)
CORS(app, resources={r'/*': {'origins': '*'}})


def all_users_have_voted():
    return all(u.get("has_voted") for u in USERS.values())


@app.route('/', methods=['GET'])
def index():
    return jsonify("server up and running")


@app.route('/api', methods=['GET'])
def index_with_prefix():
    return jsonify("server up and running with prefix")


@app.route('/api/hello', methods=['GET'])
def hello():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1  # setting session data
    return jsonify("Total visits: {}".format(session.get('visits')))


@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/api/story/', methods=['PUT'])
def add_story():
    post_data = request.get_json()
    print(f"story: {post_data}")
    if "title" in post_data.keys():
        STORY["title"] = post_data.get("title")
    if "description" in post_data.keys():
        STORY["description"] = post_data.get("description")

    socketio.emit('storyModified', {'Story modified': STORY}, broadcast=True)

    return jsonify('story ok!')


@app.route('/api/story/', methods=['GET'])
def get_story():
    return jsonify(STORY)


@app.route('/api/votes/<user_id>', methods=['POST'])
def do_vote(user_id):
    if all_users_have_voted():
        return jsonify("too late"), 418

    post_data = request.get_json()
    vote = post_data.get("vote")
    if vote not in VOTE_OPTIONS:
        return jsonify(f"Value {vote} not in allowed options")
    VOTES[user_id] = vote
    USERS[user_id]["has_voted"] = True
    socketio.emit('userVoted', {'User voted': user_id}, broadcast=True)
    return jsonify("ok")


@app.route('/api/votes/', methods=['DELETE'])
def clear_votes():
    for k in list(VOTES.keys()):
        VOTES.pop(k)
    for u in USERS.values():
        u["has_voted"] = False
        u["vote"] = None
    socketio.emit('votesCleared', {'Votes have been cleared': None}, broadcast=True)
    return jsonify("ok")


@app.route('/api/vote_options', methods=['GET'])
def get_vote_options():
    return jsonify(VOTE_OPTIONS)


@app.route('/api/login', methods=['POST'])
def login():
    if session.get("username"):
        print("aha. re-login")

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    post_data = request.get_json()
    print(f"user login: {post_data}")
    username = post_data.get("username")
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400

    new_user = {"username": username, "has_voted": False}
    USERS[username] = new_user
    session.username = username
    socketio.emit('userJoined', {'User Joined': username}, broadcast=True)

    return jsonify({"username": username}), 200


@app.route('/api/users', methods=['GET'])
def all_users():
    response_object = {'status': 'success'}
    users = USERS.copy()
    print(f"all users {users}")
    print(f"all votes {VOTES}")

    if all_users_have_voted():
        for user_name, user in USERS.items():
            vote = VOTES[user_name]
            users[user_name]["vote"] = vote
    else:
        for user_name, user in USERS.items():
            users[user_name]["vote"] = "hidden"
    response_object['users'] = list(users.values())
    return jsonify(response_object)


@app.route('/api/users/<username>', methods=['DELETE'])
def delete_user(username):
    print(f"deleting user {username}")

    try:
        del USERS[username]
    except KeyError:
        pass

    response_object = {'status': 'success'}
    socketio.emit('userJoined', {'User Quit': username}, broadcast=True)
    return jsonify(response_object)


@socketio.on('message')
def handle_message(data, second_argument):
    print(dir(request))
    print(f'server received message: {data}, {second_argument}')
    socketio.emit('messageChannel', {'Message': data, 'from': second_argument}, broadcast=True)


@socketio.on('ping')
def ping(message):
    print('ping event', message)


if __name__ == '__main__':
    app.secret_key = "123"
    socketio.run(app, host="0.0.0.0")
