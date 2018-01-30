# -*- coding:utf-8 -*-

from django import template
import re
from rbac.rbac_settings import PERMISSION_MENU_KEY

register = template.Library()


@register.inclusion_tag('menu_html.html')
def menu_html(request):
    menu_list = request.session[PERMISSION_MENU_KEY]
    current_url = request.path_info
    menu_dict = {}
    for i in menu_list:
        if not i['menu_gp_id']:
            menu_dict[i['id']] = i
    for i in menu_list:
        url = i['url']
        regex = '^{0}$'.format(url)
        if re.match(regex, current_url):
            if i['menu_gp_id']:
                menu_dict[i['menu_gp_id']]['active'] = True
            else:
                menu_dict[i['id']]['active'] = True
            break
    result = {}
    for i in menu_dict.values():
        active = i.get('active')
        if i['menu_id'] in result:
            result[i['menu_id']]['children'].append({
                'title': i['title'],
                'url': i['url'],
                'active': active,
            })
            if active:
                result[i['menu_id']]['active'] = active;

        else:
            result[i['menu_id']] = {
                'menu_title': i['menu_title'],
                'active': active,
                'children': [{
                    'title': i['title'],
                    'url': i['url'],
                    'active': active
                }]}
    return {'result': result.values()}


a = [{'id': 1, 'title': '查看用户', 'url': '/user/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': None},
     {'id': 2, 'title': '编辑用户', 'url': '/user/edit/\\d+', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': 1},
     {'id': 3, 'title': '添加用户', 'url': '/user/add/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': 1},
     {'id': 4, 'title': '删除用户', 'url': '/user/del/\\d+', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': 1},
     {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': None},
     {'id': 6, 'title': '编辑订单', 'url': '/order/edit/\\d+', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': 5},
     {'id': 7, 'title': '添加订单', 'url': '/order/add/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': 5},
     {'id': 8, 'title': '删除订单', 'url': '/order/del/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': 5}]
b = {1: {'id': 1, 'title': '查看用户', 'url': '/user/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': None},
     5: {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': None}}
c = {1: {'id': 1, 'title': '查看用户', 'url': '/user/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': None,
         'active': True},
     5: {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': None}}
d = {1: {'id': 1, 'title': '查看用户', 'url': '/user/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': None,
         'active': True},
     5: {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': None}}
menu_dict = {1: {'id': 1, 'title': '查看用户', 'url': '/user/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': None,
                 'active': True},
             5: {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': None}}

aaa = {1: {'menu_title': '菜单一', 'active': True, 'children': [{'title': '查看用户', 'url': '/user/', 'active': True}]},
       2: {'menu_title': '菜单2', 'active': None, 'children': [{'title': '查看订单', 'url': '/order/', 'active': None}]}}
