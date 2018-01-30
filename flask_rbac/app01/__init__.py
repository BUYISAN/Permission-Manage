#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, session, redirect
from flask_session import Session
from app01.my_db import db
from .views import account
from .views import order
from rbac.models import *
from rbac.middleware.rbac import process_request
from rbac.templatetags.rbac import menu_html


def create_app():
    app = Flask(__name__)
    print(app.static_url_path)
    print(app.static_folder)
    app.secret_key = 'uksdjjwehjwefwnf'
    app.debug = True
    # 读取配置文件
    app.config.from_object('settings.DevelopmentConfig')
    Session(app)
    # 蓝图注册
    app.register_blueprint(account.account)
    app.register_blueprint(order._order)
    # SQLAlchemy初始化app
    db.init_app(app)
    # 中间件注册
    app.before_request(process_request)

    app.template_global()(menu_html)
    return app
