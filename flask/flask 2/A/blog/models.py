from blog import db , login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20) , unique=True , nullable=False)
    email = db.Column(db.String(20) , unique=True , nullable=False)
    password = db.Column(db.String(60) , unique=True , nullable=False)
    posts = db.relationship('Post' , backref='author' , lazy=True) #the post model , backref : back relationship with the name of author : post.author , lazy : one run when its ran

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id} , {self.username})'



class Post(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(120) , nullable=False)
    date = db.Column(db.DateTime() , nullable=False , default=datetime.now)
    content = db.Column(db.Text , nullable=False )
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False) #user is an object (it is lowerscaled) , we have relationships with the objects of the model not itself

    def __repr__(self):
        return '{self.__class__.__name__} , {self.id} , {self.title[:30]} , {self.date}'