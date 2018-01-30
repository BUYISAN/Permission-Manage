#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = [{'id': 1, 'title': '查看用户', 'url': '/user', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单一'},
     {'id': 2, 'title': '编辑用户', 'url': '/user/edit/d+', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'},
     {'id': 3, 'title': '添加用户', 'url': '/user/add/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'},
     {'id': 4, 'title': '删除用户', 'url': '/user/del/d+', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'},
     {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单二'},
     {'id': 6, 'title': '编辑订单', 'url': '/order/edit/d+', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'},
     {'id': 7, 'title': '添加订单', 'url': '/order/add/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'},
     {'id': 8, 'title': '删除订单', 'url': '/order/del/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}]
b = {1: {'menu_id': 1, 'menu_title': '菜单一', 'active': True,
         'children': [{'title': '查看用户', 'url': '/user', 'active': True}]},
     2: {'menu_id': 2, 'menu_title': '菜单二', 'active': None,
         'children': [{'title': '查看订单', 'url': '/order/', 'active': None}]}}
c = [{'id': 1, 'title': '查看用户', 'url': '/user', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单一', 'active': True},
     {'id': 2, 'title': '编辑用户', 'url': '/user/edit/d+', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'},
     {'id': 3, 'title': '添加用户', 'url': '/user/add/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'},
     {'id': 4, 'title': '删除用户', 'url': '/user/del/d+', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'},
     {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单二'},
     {'id': 6, 'title': '编辑订单', 'url': '/order/edit/d+', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'},
     {'id': 7, 'title': '添加订单', 'url': '/order/add/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'},
     {'id': 8, 'title': '删除订单', 'url': '/order/del/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}]

d = {1: {'menu_id': 1, 'menu_title': '菜单一', 'active': True,
         'children': [{'title': '查看用户', 'url': '/user', 'active': True}]},
     2: {'menu_id': 2, 'menu_title': '菜单二', 'active': True,
         'children': [{'title': '查看订单', 'url': '/order/', 'active': True}]}}
