import os
import logging

""" jwt create access monkey patch"""
import datetime
import flask_jwt_extended
_create_access_token = flask_jwt_extended.create_access_token
def monkey_patch_create_access_token(identity, fresh=False, expires_delta=None, user_claims=None):
    return _create_access_token(identity, fresh, datetime.timedelta(days=365), user_claims)
flask_jwt_extended.create_access_token = monkey_patch_create_access_token

from flask import Flask, make_response
from flask_appbuilder import AppBuilder, SQLA
from flask_appbuilder.views import IndexView
from flask_appbuilder.baseviews import expose
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("flask_appbuilder")
# logger.setLevel(logging.ERROR)
logging.getLogger("app").setLevel(logging.DEBUG)
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLA(app)
CORS(app)

APP_DIR = os.path.abspath(os.path.dirname(__file__))
INDEX_FILE = os.path.join(APP_DIR, "../openform/dist/static/index.html")

class HomeView(IndexView):
    
    @expose("/")
    def index(self):
        print(INDEX_FILE)
        fd = open(INDEX_FILE, "r")
        index = fd.read()
        fd.close()
        return make_response(index)

migrate = Migrate(app, db)
appbuilder = AppBuilder(app, db.session, indexview=HomeView)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views, models