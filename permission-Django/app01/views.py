from django.shortcuts import render, HttpResponse, redirect
from rbac import models
from rbac.service.service import init_permission


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.User.objects.filter(username=username, password=password).first()
        if not user_obj:
            return render(request, 'login.html')
        else:
            init_permission(user_obj, request)
            return redirect('/user/')


class Code(object):
    def __init__(self, codes):
        self.codes = codes

    def has_add(self):
        if 'add' in self.codes:
            return True

    def has_edit(self):
        if 'edit' in self.codes:
            return True

    def has_del(self):
        if 'del' in self.codes:
            return True


def user(request):
    code = Code(request.permission_list)
    return render(request, 'user.html', {'code': code})


def user_add(request):
    return render(request, 'user_add.html')


def user_edit(request):
    return render(request, 'user_edit.html')


def user_del(request):
    return HttpResponse('user 删除页面')


def order(request):
    return render(request, 'order.html')


a = [{'permission__id': 1, 'permission__title': '查看用户', 'permission__url': '/user/', 'permission__codes': 'list',
      'permission__group_id': 1, 'permission__menu_gp__id': None, 'permission__group__menu_id': 1},
     {'permission__id': 2, 'permission__title': '编辑用户', 'permission__url': '/user/edit/\\d+',
      'permission__codes': 'edit', 'permission__group_id': 1, 'permission__menu_gp__id': 1,
      'permission__group__menu_id': 1},
     {'permission__id': 3, 'permission__title': '添加用户', 'permission__url': '/user/add/', 'permission__codes': 'add',
      'permission__group_id': 1, 'permission__menu_gp__id': 1, 'permission__group__menu_id': 1},
     {'permission__id': 4, 'permission__title': '删除用户', 'permission__url': '/user/del/\\d+',
      'permission__codes': 'del', 'permission__group_id': 1, 'permission__menu_gp__id': 1,
      'permission__group__menu_id': 1},
     {'permission__id': 5, 'permission__title': '查看订单', 'permission__url': '/order/', 'permission__codes': 'list',
      'permission__group_id': 2, 'permission__menu_gp__id': None, 'permission__group__menu_id': 2},
     {'permission__id': 6, 'permission__title': '编辑订单', 'permission__url': '/order/edit/\\d+',
      'permission__codes': 'edit', 'permission__group_id': 2, 'permission__menu_gp__id': 5,
      'permission__group__menu_id': 2},
     {'permission__id': 7, 'permission__title': '添加订单', 'permission__url': '/order/add/', 'permission__codes': 'add',
      'permission__group_id': 2, 'permission__menu_gp__id': 5, 'permission__group__menu_id': 2},
     {'permission__id': 8, 'permission__title': '删除订单', 'permission__url': '/order/del/', 'permission__codes': 'del',
      'permission__group_id': 2, 'permission__menu_gp__id': 5, 'permission__group__menu_id': 2}]
# 权限相关信息

b = {1: {'code': ['list', 'edit', 'add', 'del'],
         'urls': ['/user/', '/user/edit/\\d+', '/user/add/', '/user/del/\\d+']},
     2: {
         'code': ['list', 'edit', 'add', 'del'],
         'urls': ['/order/', '/order/edit/\\d+', '/order/add/', '/order/del/']}}

# 菜单相关
c = [{'id': 1, 'title': '查看用户', 'url': '/user/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': None},
     {'id': 2, 'title': '编辑用户', 'url': '/user/edit/\\d+', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': 1},
     {'id': 3, 'title': '添加用户', 'url': '/user/add/', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': 1},
     {'id': 4, 'title': '删除用户', 'url': '/user/del/\\d+', 'menu_id': 1, 'menu_title': '菜单一', 'menu_gp_id': 1},
     {'id': 5, 'title': '查看订单', 'url': '/order/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': None},
     {'id': 6, 'title': '编辑订单', 'url': '/order/edit/\\d+', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': 5},
     {'id': 7, 'title': '添加订单', 'url': '/order/add/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': 5},
     {'id': 8, 'title': '删除订单', 'url': '/order/del/', 'menu_id': 2, 'menu_title': '菜单2', 'menu_gp_id': 5}]

d = {1: {'menu_title': '菜单一', 'active': True, 'children': [{'title': '查看用户', 'url': '/user/', 'active': True},
                                                           {'title': '查看订单', 'url': '/order/', 'active': None}]}}
