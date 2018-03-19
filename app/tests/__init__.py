import os
import unittest
import sqlalchemy

from app import app, db

# parent class helps with testing against a test db


class DBTestCase(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            basedir = os.path.abspath(os.path.dirname(__file__))
            url = os.environ.get('DATABASE_URL') or \
                  'sqlite:///' + os.path.join(basedir, 'app.db')
            app.config['SQLALCHEMY_DATABASE_URI'] = url
            app.config['TESTING'] = True
            self.engine = sqlalchemy.create_engine(url)
            self.connection = self.engine.connect()
            db.create_all()
            self.client = app.test_client()

    def tearDown(self):
        with app.app_context():
            db.session.close()
            db.session.remove()
            db.drop_all()
            print 'cleaning up'

