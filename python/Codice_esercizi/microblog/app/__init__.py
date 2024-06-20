from flask import Flask
from config import Config
from flask_debugtoolbar import DebugToolbarExtension

# creation di app
app = Flask(__name__)
# config of app from config.py
app.config.from_object(Config)

# the toolbar is only enabled in debug mode:
app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = Config.SECRET_KEY
# setup the toolbar for app
toolbar = DebugToolbarExtension(app)

from app import routes