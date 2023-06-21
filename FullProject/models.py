from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = 'planten'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    watering = db.Column(db.String)

class MyPlant(db.Model):
    __tablename__ = 'mijnPlanten'
    id = db.Column(db.Integer, primary_key=True)
    # foreing key naar planten tabel with
    plant_id = db.Column(db.Integer, db.ForeignKey('planten.id'))
    plant = db.relationship('Plant', backref='mijnPlanten')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='mijnPlanten')
    location = db.Column(db.String)
    last_watered = db.Column(db.DateTime)
    automatic_watering = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    moisture_value = db.Column(db.Integer)
    
class Post_gifs(db.Model):
    __tablename__ = 'post_gifs'
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='posts')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    gif_id = db.Column(db.Integer, db.ForeignKey('post_gifs.id'))
    gif = db.relationship('Post_gifs', backref='posts')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


