#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from rbac.models import *

# from app01.my_db import db

engine = create_engine('mysql+pymysql://root:123@127.0.0.1:3306/flask-demo?charset=utf8')
Session = sessionmaker(bind=engine)
db_session = Session()

res = db_session.query(User).filter_by(username='egon').first()
flat = lambda L: sum(map(flat, L), []) if isinstance(L, list) else [L]
print(res.position)
print(flat([i.permission for i in res.position]))
# print(type(res[0]))

res1 = db_session.query(User.username, Permission.id, Permission.title, Permission.url, Permission.code,
                        Permission.menu_gp_id, Permission.groups_id,
                        Menu.id, Menu.title).join(User2Position, Position,
                                                  Position2Permission,
                                                  Permission, Groups,
                                                  Menu).filter(User.username == 'alex', User.password == '123').all()

print(res1)
permission_list = []
for i in res1:
    permission_list.append({'permissions__id': i[1], 'permissions__title': i[2], 'permissions__url': i[3],
                            'permissions__code': i[4],
                            'permissions__menu_gp_id': i[5], 'permissions__group_id': i[6],
                            'permissions__group__menu_id': i[7],
                            'permissions__group__menu__title': i[8]})

print(permission_list)
my_bound = [
    {'permissions__id': 1, 'permissions__title': '查看用户', 'permissions__url': '/user', 'permissions__code': 'list',
     'permissions__menu_gp_id': None, 'permissions__group_id': 1, 'permissions__group__menu_id': 1,
     'permissions__group__menu__title': '菜单一'},
    {'permissions__id': 2, 'permissions__title': '编辑用户', 'permissions__url': '/user/edit/d+',
     'permissions__code': 'edit', 'permissions__menu_gp_id': 1, 'permissions__group_id': 1,
     'permissions__group__menu_id': 1, 'permissions__group__menu__title': '菜单一'},
    {'permissions__id': 3, 'permissions__title': '添加用户', 'permissions__url': '/user/add/', 'permissions__code': 'add',
     'permissions__menu_gp_id': 1, 'permissions__group_id': 1, 'permissions__group__menu_id': 1,
     'permissions__group__menu__title': '菜单一'},
    {'permissions__id': 4, 'permissions__title': '删除用户', 'permissions__url': '/user/del/d+', 'permissions__code': 'del',
     'permissions__menu_gp_id': 1, 'permissions__group_id': 1, 'permissions__group__menu_id': 1,
     'permissions__group__menu__title': '菜单一'},
    {'permissions__id': 5, 'permissions__title': '查看订单', 'permissions__url': '/order/', 'permissions__code': 'list',
     'permissions__menu_gp_id': None, 'permissions__group_id': 2, 'permissions__group__menu_id': 2,
     'permissions__group__menu__title': '菜单二'},
    {'permissions__id': 6, 'permissions__title': '编辑订单', 'permissions__url': '/order/edit/d+',
     'permissions__code': 'edit', 'permissions__menu_gp_id': 5, 'permissions__group_id': 2,
     'permissions__group__menu_id': 2, 'permissions__group__menu__title': '菜单二'},
    {'permissions__id': 7, 'permissions__title': '添加订单', 'permissions__url': '/order/add/', 'permissions__code': 'add',
     'permissions__menu_gp_id': 5, 'permissions__group_id': 2, 'permissions__group__menu_id': 2,
     'permissions__group__menu__title': '菜单二'},
    {'permissions__id': 8, 'permissions__title': '删除订单', 'permissions__url': '/order/del/', 'permissions__code': 'del',
     'permissions__menu_gp_id': 5, 'permissions__group_id': 2, 'permissions__group__menu_id': 2,
     'permissions__group__menu__title': '菜单二'}]

bound = [
    {'permissions__id': 1, 'permissions__title': '用户列表', 'permissions__url': '/userinfo/', 'permissions__code': 'list',
     'permissions__menu_gp_id': None, 'permissions__group_id': 1, 'permissions__group__menu_id': 1,
     'permissions__group__menu__title': '菜单管理'},
    {'permissions__id': 2, 'permissions__title': '添加用户', 'permissions__url': '/userinfo/add/',
     'permissions__code': 'add', 'permissions__menu_gp_id': 1, 'permissions__group_id': 1,
     'permissions__group__menu_id': 1, 'permissions__group__menu__title': '菜单管理'},
    {'permissions__id': 3, 'permissions__title': '删除用户', 'permissions__url': '/userinfo/del/(\\d+)/',
     'permissions__code': 'del', 'permissions__menu_gp_id': 1, 'permissions__group_id': 1,
     'permissions__group__menu_id': 1, 'permissions__group__menu__title': '菜单管理'},
    {'permissions__id': 4, 'permissions__title': '修改用户', 'permissions__url': '/userinfo/edit/(\\d+)/',
     'permissions__code': 'edit', 'permissions__menu_gp_id': 1, 'permissions__group_id': 1,
     'permissions__group__menu_id': 1, 'permissions__group__menu__title': '菜单管理'},
    {'permissions__id': 5, 'permissions__title': '订单列表', 'permissions__url': '/order/', 'permissions__code': 'list',
     'permissions__menu_gp_id': None, 'permissions__group_id': 2, 'permissions__group__menu_id': 2,
     'permissions__group__menu__title': '菜单2'},
    {'permissions__id': 6, 'permissions__title': '添加订单', 'permissions__url': '/order/add/', 'permissions__code': 'add',
     'permissions__menu_gp_id': 5, 'permissions__group_id': 2, 'permissions__group__menu_id': 2,
     'permissions__group__menu__title': '菜单2'},
    {'permissions__id': 7, 'permissions__title': '删除订单', 'permissions__url': '/order/del/(\\d+)/',
     'permissions__code': 'del', 'permissions__menu_gp_id': 5, 'permissions__group_id': 2,
     'permissions__group__menu_id': 2, 'permissions__group__menu__title': '菜单2'},
    {'permissions__id': 8, 'permissions__title': '修改订单', 'permissions__url': '/order/edit/(\\d+)/',
     'permissions__code': 'edit', 'permissions__menu_gp_id': 5, 'permissions__group_id': 2,
     'permissions__group__menu_id': 2, 'permissions__group__menu__title': '菜单2'}]

bsession2 = {1: {'codes': ['list', 'add', 'del', 'edit'],
                 'urls': ['/userinfo/', '/userinfo/add/', '/userinfo/del/(\\d+)/', '/userinfo/edit/(\\d+)/']},
             2: {'codes': ['list', 'add', 'del', 'edit'],
                 'urls': ['/order/', '/order/add/', '/order/del/(\\d+)/', '/order/edit/(\\d+)/']}}

urlsession = {1: {'menu_id': 1, 'menu_title': '菜单管理', 'active': True,
                  'children': [{'title': '用户列表', 'url': '/userinfo/', 'active': True}]},
              2: {'menu_id': 2, 'menu_title': '菜单2', 'active': None,
                  'children': [{'title': '订单列表', 'url': '/order/', 'active': None}]}}
