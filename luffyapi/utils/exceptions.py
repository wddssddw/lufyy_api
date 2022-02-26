# -*- coding:utf-8 -*-
"""
@author: chifan
@time:2022/2/13 18:13
"""
from rest_framework.views import exception_handler
# from luffyapi.utils.response import APIResponse
from .response import APIResponse
from .logger import log


def common_exception_handler(exc, context):
    log.error('view是: %s,错误是:%s' % (str(context['view']), str(exc)))
    ret = exception_handler(exc, context)
    if not ret:
        if isinstance(exc, KeyError):
            # context['view']
            return APIResponse(code=0, msg='error')
        return APIResponse(code=0, msg='error', result=str(exc))
    else:
        return APIResponse(code=0, msg='error', result=ret.data)
