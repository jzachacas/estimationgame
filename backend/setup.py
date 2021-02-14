from app import flask_app
from database import db

if __name__ == '__main__':
    print(" initializing database setup ".center(80, "="))
    with flask_app.app_context():
        print("setting up database")
        db.create_all()