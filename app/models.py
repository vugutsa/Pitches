from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    pitch = db.relationship('Comments', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return f'User {self.username}'
   
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






class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    
    def __repr__(self):
        return f'User {self.name}'
    
class Comments(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(movie_id=id).all()
        
        return comments
    
    
class Pitches(db.Model):
    __tablename__= 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    date = db.Column(db.DateTime(250), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comments', backref='title', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,cate):
        pitch = Pitches.query.filter_by(category=cate).all()
        return pitch

    def __repr__(self):
        return f"Pitches {self.pitch}','{self.date}')"