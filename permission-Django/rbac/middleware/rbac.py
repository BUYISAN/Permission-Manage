# -*- coding:utf-8 -*-


"""
@author: BUYI

@file: rbac.py

# Date: 2017/11/10

"""
import re
from django.shortcuts import redirect, HttpResponse
from rbac.rbac_settings import ALLOW_URLS, PERMISSION_URL_DICT_KEY


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddle(MiddlewareMixin):
    def process_request(self, request):
        current_url = request.path_info
        for url in ALLOW_URLS:
            regex = '^{0}$'.format(url)
            if re.match(regex, current_url):
                return None
        permission_dict = request.session.get(PERMISSION_URL_DICT_KEY)
        if not permission_dict:
            return redirect('/login/')
        # 权限相关处理
        for item in permission_dict.values():
            for i in item['urls']:
                regex = '^{0}$'.format(i)
                if re.match(regex, current_url):
                    request.permission_list = item['code']
                    return None
        return HttpResponse('无权访问')
