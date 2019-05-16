from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config.from_pyfile('setting.py')

moment = Moment(app)

csrf = CSRFProtect(app)

db = SQLAlchemy(app)

Debugtool = DebugToolbarExtension(app)

from qurey_systerm import views,commands