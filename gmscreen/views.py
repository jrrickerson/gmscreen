from flask import request
from gmscreen import app
from gmscreen.database import ViewSystem, Viewport, Playlist, PlayState


@app.route('/', methods=['GET', 'POST'])
def dashboard_view():
    return 'Dashboard View'
