import os
import unittest

from flask import current_app

from flask_testing import TestCase

from project import create_app

app = create_app()


class TestDevelopmentConfig(TestCase):
    """Tests for Development Config"""

    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQL_ALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_DEV_URL') # noqa
        )


class TestQAConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.QAConfig')
        return app

    def test_app_is_qa(self):
        self.assertTrue(app.config['TESTING'])
        self.assertTrue(
            app.config['SQL_ALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_QA_URL') # noqa
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertFalse(app.config['TESTING'])
        self.assertTrue(
            app.config['SQL_ALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_PROD_URL') # noqa
        )


if __name__ == '__main__':
    unittest.main()