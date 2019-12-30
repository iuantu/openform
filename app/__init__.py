import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from app import models

load_dotenv()
logger = logging.getLogger("flask_appbuilder")
logger.setLevel(logging.ERROR)
logging.getLogger("app").setLevel(logging.DEBUG)
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

from datetime import datetime
from flask_jwt_extended import utils
_create_access_token = utils.create_access_token
utils.create_access_token = lambda identity, fresh=False, expires_delta=None, user_claims=None: _create_access_token(identity, fresh, datetime.timedelta(days=365), user_claims)

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
CORS(app)

migrate = Migrate(app, db)
appbuilder = AppBuilder(app, db.session)


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

from . import views
from .models import *