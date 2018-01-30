# -*- coding:utf-8 -*-


"""
@author: BUYI

@file: service.py

# Date: 2017/11/10

"""
from rbac.rbac_settings import PERMISSION_MENU_KEY, PERMISSION_URL_DICT_KEY


def init_permission(user, request):
    permission_dict = user.position.values('permission__id',
                                           'permission__title',
                                           'permission__url',
                                           'permission__codes',
                                           'permission__group_id',
                                           'permission__menu_gp__id',
                                           'permission__group__menu_id',
                                           'permission__group__menu__title'
                                           ).distinct()
    # print(permission_dict)
    # 处理数据信息,然后将信息绑定到session上
    # 菜单相关信息:url-title,url,menu信息,menu_gp信息(组长信息)
    menu_about = []
    for item in permission_dict:
        menu_about.append({
            'id': item['permission__id'],
            'title': item['permission__title'],
            'url': item['permission__url'],
            'menu_id': item['permission__group__menu_id'],
            'menu_title': item['permission__group__menu__title'],
            'menu_gp_id': item['permission__menu_gp__id'],
        })
    request.session[PERMISSION_MENU_KEY] = menu_about
    # 权限相关信息:组信息,codes信息,权限url信息
    result = {}
    for item in permission_dict:
        group_id = item['permission__group_id']
        if group_id in result:
            result[group_id]['code'].append(item['permission__codes'])
            result[group_id]['urls'].append(item['permission__url'])
        else:
            result[group_id] = {
                'code': [item['permission__codes']],
                'urls': [item['permission__url']]
            }
    request.session[PERMISSION_URL_DICT_KEY] = result
