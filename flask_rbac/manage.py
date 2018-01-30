#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_script import Manager, Server
from app01 import create_app
from flask_migrate import Migrate, MigrateCommand
from app01.my_db import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()
