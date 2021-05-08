from app import db
from datetime import datetime

class User(db.Model):
    email = db.Column(db.String(120), index=True, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    results = db.relationship('Result', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Result(db.Model):
    username = db.Column(db.String(64), db.ForeignKey('user.username'),primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    mark = db.Column(db.Integer)

    def __repr__(self):
        return '<Result {}>'.format(self.body)



