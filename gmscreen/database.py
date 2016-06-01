from flask_sqlalchemy import SQLAlchemy
from gmscreen import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class ViewSystem(db.Model):
    """ Represents a specific group and layout of Viewports. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    location = db.Column(db.String(120))
    viewports = db.relationship(
        'Viewport', backref='viewsystem', lazy='dynamic')
    playlists = db.relationship(
        'Playlist', backref='viewsystem', lazy='dynamic')


class Viewport(db.Model):
    """ Represents an individual device or screen capable of playing back
    media. """
    id = db.Column(db.Integer, primary_key=True)
    viewsystem_id = db.Column(db.Integer, db.ForeignKey('view_system.id'))
    name = db.Column(db.String(120))
    code = db.Column(db.String(30), unique=True)


class Playlist(db.Model):
    """ Represents a playlist to be replayed on a particular ViewSystem. """
    id = db.Column(db.Integer, primary_key=True)
    viewsystem_id = db.Column(db.Integer, db.ForeignKey('view_system.id'))
    name = db.Column(db.String(120), unique=True)


class PlayState(db.Model):
    """ Represents a single combined state of components on a viewport,
    e.g. a background image, piece of music, etc. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    background_uri = db.Column(db.String(300))
    music_uri = db.Column(db.String(300))
    video_uri = db.Column(db.String(300))
