#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from rbac.models import *
from flask import session
from rbac import my_settings

engine = create_engine('mysql+pymysql://root:123@127.0.0.1:3306/flask-demo?charset=utf8')
Session = sessionmaker(bind=engine)
db_session = Session()


def init_permission(username, password):
    res = db_session.query(User).filter_by(username=username, password=password).first()
    if not res:
        return None

    res1 = db_session.query(User.username, Permission.id, Permission.title, Permission.url, Permission.code,
                            Permission.menu_gp_id, Permission.groups_id, Menu.id, Menu.title).join(User2Position,
                                                                                                   Position,
                                                                                                   Position2Permission,
                                                                                                   Permission, Groups,
                                                                                                   Menu).filter(
        User.username == username,
        User.password == password).all()
    permission_list = []
    for i in res1:
        permission_list.append({'permissions__id': i[1], 'permissions__title': i[2], 'permissions__url': i[3],
                                'permissions__code': i[4],
                                'permissions__menu_gp_id': i[5], 'permissions__group_id': i[6],
                                'permissions__group__menu_id': i[7],
                                'permissions__group__menu__title': i[8]})

    sub_permission_list = []
    for item in permission_list:
        tpl = {
            'id': item['permissions__id'],
            'title': item['permissions__title'],
            'url': item['permissions__url'],
            'menu_gp_id': item['permissions__menu_gp_id'],
            'menu_id': item['permissions__group__menu_id'],
            'menu_title': item['permissions__group__menu__title'],
        }
        sub_permission_list.append(tpl)
    print(sub_permission_list)
    session[my_settings.PERMISSION_MENU_KEY] = sub_permission_list

    # 权限相关
    result = {}
    for item in permission_list:
        group_id = item['permissions__group_id']
        code = item['permissions__code']
        url = item['permissions__url']
        if group_id in result:
            result[group_id]['codes'].append(code)
            result[group_id]['urls'].append(url)
        else:
            result[group_id] = {
                'codes': [code, ],
                'urls': [url, ]
            }
    print(result)
    session[my_settings.PERMISSION_URL_DICT_KEY] = result
    db_session.close()
    return True
