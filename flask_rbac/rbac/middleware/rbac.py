#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rbac import my_settings
import re
from flask import redirect
from flask import request
from flask import session


def process_request():
    # 1. 获取当前请求的URL
    # request.path
    # 2. 获取session中保存当前用户的权限
    # session.get("permission_url_list')
    # 当前请求不需要执行权限验证
    current_url = request.path
    for url in my_settings.VALID_URL:
        if re.match(url, current_url):
            return None

    permission_dict = session.get(my_settings.PERMISSION_URL_DICT_KEY)
    if not permission_dict:
        return redirect('/login')

    flag = False
    for group_id, code_url in permission_dict.items():
        for db_url in code_url['urls']:
            regax = "^{0}$".format(db_url)
            if re.match(regax, current_url):
                request.permission_code_list = code_url['codes']
                print(code_url['codes'], '中间件绑定codes')
                flag = True
                break
        if flag:
            break

    if not flag:
        return '无权访问'
