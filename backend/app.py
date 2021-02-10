import connexion
from flask_cors import CORS
from flask_socketio import SocketIO

import view
from database import db

DEBUG = True


def create_app():
    connexion_app = connexion.App(__name__)
    app = connexion_app.app  # equals to app = Flask(__name__)
    app.config.from_object(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.config['SECRET_KEY'] = 'would become a secret in production...'
    _socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*",
                         path="/api-ws/socket.io",
                         ping_timeout=20, manage_session=True)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.url_map.strict_slashes = False

    connexion_app.add_api('../swagger.yaml')
    register_blueprints(app)

    app.emit = lambda *arg, **kwargs: print("lol")
    return app, _socketio


def register_blueprints(the_app):
    url_prefix = "/api/"
    the_app.register_blueprint(view.app, url_prefix=url_prefix)


flask_app, socketio = create_app()

if __name__ == '__main__':
    with flask_app.app_context():
        print("setting up database")
        db.create_all()

    # socketio.run(flask_app, host="0.0.0.0", extra_files=["../swagger.yaml"])
