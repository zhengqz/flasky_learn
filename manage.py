# coding:utf-8 
"""
Created on 2016/04/22
Author: shylock
"""
import os
import pdb
from flask.ext.script import Shell, Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app
from app import db
from app.models import User, Role


app = create_app(os.getenv('FLASK_CONFIG') or "default")

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    print app.url_map
    manager.run()
