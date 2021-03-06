from datetime import datetime
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from . import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        
    def __repr__(self):
        return f'User {self.username}'

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


class Contact(db.Model):
    __tablename__='feedback'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(255))
    email = db.Column(db.String(255))
    message=db.Column(db.String(255))
    


