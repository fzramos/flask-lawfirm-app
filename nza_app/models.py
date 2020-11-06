from nza_app import app, db, login_manager

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

import uuid

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.String(256), primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique=True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    case_note = db.relationship('Note', backref = 'author', lazy = True)

    def __init__(self,username,email,password):
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        """
            Grab the password that is passed into the method
            return the hashed verson of the password 
            which will be stored inside the database
        """
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.username} has been created with the following email: {self.email}'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    case_name = db.Column(db.String(100))
    case_note = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    edited = db.Column(db.Boolean, nullable = False, default = False)
    date_updated = db.Column(db.DateTime)
    user_id = db.Column(db.String(256), db.ForeignKey('user.id'), nullable = False)

    def __init__(self,case_name, case_note , user_id = user_id):
        self.case_name = case_name
        self.case_note = case_note
        self.user_id = user_id
    
    def __repr__(self):
        return f'The name  of the new case note is {self.case_name} \n and the content is: {self.case_note}.'