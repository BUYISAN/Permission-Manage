#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from rbac.my_settings import PERMISSION_MENU_KEY
from flask import render_template
import copy


def menu_html(session, request):
    menu_list = copy.deepcopy(session[PERMISSION_MENU_KEY])
    current_url = request.path
    menu_dict = {}
    for item in menu_list:
        if not item['menu_gp_id']:
            menu_dict[item['id']] = item

    for item in menu_list:
        regex = "^{0}$".format(item['url'])
        if re.match(regex, current_url):
            menu_gp_id = item['menu_gp_id']
            if menu_gp_id:
                menu_dict[menu_gp_id]['active'] = True
            else:
                menu_dict[item['id']]['active'] = True

    result = {}
    for item in menu_dict.values():
        active = item.get('active')
        menu_id = item['menu_id']
        if menu_id in result:
            result[menu_id]['children'].append({'title': item['title'], 'url': item['url'], 'active': active})
            if active:
                result[menu_id]['active'] = True
        else:
            result[menu_id] = {
                'menu_id': item['menu_id'],
                'menu_title': item['menu_title'],
                'active': active,
                'children': [
                    {'title': item['title'], 'url': item['url'], 'active': active}
                ]
            }
    print(result, 2323232323)  # {'menu_dict': result}
    return render_template('xxxxx.html', menu_dict=result)
