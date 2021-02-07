# The Backend Part 

A minimal Python-based backend using [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/).

Currently, there is no persistence whatsoever - except for sessions. State is kept in
the global variables `USERS STORY VOTE_OPTIONS VOTES`. 

The state gets lost on hot-reload, of course.