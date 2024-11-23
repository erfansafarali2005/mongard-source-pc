from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# this is a constructor , when the blog is imported all the codes here will get ran , it classes it has __init__ which while making objects it startes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'fewijaefioiernfgioengieniogesiogoien934893u49qhf8jbnjkfdnvjknrntgu4hw8trh8'

db = SQLAlchemy(app)

becrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'login first ...'
login_manager.login_message_category = 'info'

from blog import routes

with app.app_context():
    db.create_all()