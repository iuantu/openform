
from flask import Flask
from flask_appbuilder import SQLA
from flask_appbuilder import AppBuilder
from flask_migrate import upgrade
from flask_migrate import Migrate

import unittest
import logging
logging.getLogger("flask_appbuilder").setLevel(logging.ERROR)

class OpenFormTestCase(unittest.TestCase):

    app : Flask = None
    db : SQLA = None
    appbuilder : AppBuilder = None
    
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        self.app.config['CSRF_ENABLED'] = False
        self.app.config['SECRET_KEY'] = 'thisismyscretkey'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = True
        
        self.db = SQLA(self.app)
        Migrate(self.app, self.db)
        self.appbuilder = AppBuilder(self.app, self.db.session)

        with self.app.app_context():
            upgrade()