from flask_script import Manager
from project import app, db

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    x = X()
    db.session.add()
    db.session.commit()


if __name__ == "__main__":
    manager.run()
