import unittest
import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import create_app
from app.Model import db

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app(env)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
