from app import create_app,db
from flask_script import Manager, Server
from app.models import Cancel, Session, User
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = create_app('production')
manager = Manager(app)
manager.add_command('server', Server)

admin=Admin(app)
admin.add_view(ModelView(Session, db.session))
admin.add_view(ModelView(Cancel, db.session))
admin.add_view(ModelView(User, db.session))

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.command
def tests():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Session = Session )

    
if __name__ == '__main__':
    manager.run()

