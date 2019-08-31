from flask_testing import TestCase

from project import app, db


class BaseTestCase(TestCase):
    def create_app():
        app.config.from_object('project.config.QAConfig')
        return app
    
    def set_up():
        db.create_all()
        db.session.commit()
    
    def shut_down():    
        db.session.remove()
        db.drop_all()