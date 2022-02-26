# -*- coding:utf-8 -*-
"""
@author: chifan
@time:2022/2/13 18:02
"""
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=100, result=None, msg='成功', status=None,
                 headers=None, content_type=None, **kwargs):
        dic = {
            'code': code,
            'msg': msg,
        }
        if result:
            dic['result'] = result
        dic.update(kwargs)
        super().__init__(data=dic, status=status, headers=headers, content_type=content_type)
