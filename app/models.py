from flask.globals import session
from . import db

class Session(db.Model):
    __tablename__='sessions'
    id = db.Column(db.Integer, primary_key=True)
    tarehe = db.Column(db.Date())
    email = db.Column(db.String(255))
    service=db.Column(db.String(255))
    status= db.Column(db.String(255))

class Cancel(db.Model):
    __tablename__='del'
    id = db.Column(db.Integer, primary_key=True)
    tarehe = db.Column(db.Date())
    email = db.Column(db.String(255))
    service=db.Column(db.String(255))
    status= db.Column(db.String(255))


