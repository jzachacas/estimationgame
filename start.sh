#!/usr/bin/env bash
service nginx start

# restrict to one worker as gunicorn does not support sticky sessions:
# https://flask-socketio.readthedocs.io/en/latest/#gunicorn-web-server
# https://github.com/miguelgrinberg/Flask-SocketIO/issues/402
gunicorn --bind 0.0.0.0:5000 --worker-class eventlet -w 1 \
--error-logfile - \
--access-logfile /var/log/gunicorn/access.log \
--capture-output --log-level debug \
app:flask_app