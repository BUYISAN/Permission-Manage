#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, session, redirect
from wtforms import Form
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets
from rbac.service.init_permission import init_permission

account = Blueprint('account', __name__)


class LoginForm(Form):
    username = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control', 'placeholder': '用户名'}
    )
    password = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control', 'placeholder': '密码'}
    )


@account.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = request.form.get('username')
            password = request.form.get('password')
            if init_permission(username, password):
                return redirect('/index')
        else:
            return render_template('login.html', form=form)
