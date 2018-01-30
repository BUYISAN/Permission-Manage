#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, session  # type=Flask

_order = Blueprint('order', __name__)


class BasePagePermission(object):
    def __init__(self, code_list):
        self.code_list = code_list

    def has_add(self):
        if "add" in self.code_list:
            return True

    def has_edit(self):
        if 'edit' in self.code_list:
            return True

    def has_del(self):
        if 'del' in self.code_list:
            return True


@_order.route('/index', methods=['GET'])
def index():
    return '登陆成功'


@_order.route('/user', methods=['GET'])
def user():
    print(request.permission_code_list, '从request获取')
    page_permission = BasePagePermission(request.permission_code_list)
    return render_template('user.html', page_permission=page_permission)


@_order.route('/order/', methods=['GET'])
def order():
    return render_template('order.html')
