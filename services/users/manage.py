import sys
import unittest
from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)


@cli.command('recreate_db')
def recreate_db():
    """Recreate the database state"""
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('test')
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py') # noqa
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
        sys.exit(result)


if __name__ == '__main__':
    cli()
