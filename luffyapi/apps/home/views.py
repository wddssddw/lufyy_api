from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from luffyapi.utils.response import APIResponse


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        dic = {'name': 'lqz'}
        print(dic['age'])
        return APIResponse()
