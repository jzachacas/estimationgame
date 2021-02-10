from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(data):
        return [item.serialize() for item in data]


class Story(db.Model):
    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

    def __init__(self, title, description=""):
        self.title = title
        self.description = description

    def __repr__(self):
        return f"<Story {self.title!r} {self.description!r}>"

    def serialize(self):
        return Serializer.serialize(self)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    has_voted = db.Column(db.Boolean)
    vote = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = relationship("Role")

    def __init__(self, username=None, role_id=None):
        self.username = username
        self.role_id = role_id

    def __repr__(self):
        return f'<User {self.username!r}>'

    def serialize(self):
        return Serializer.serialize(self)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, name=None, description=""):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<User {self.name!r} {self.description!r}>"

    def serialize(self):
        return Serializer.serialize(self)
