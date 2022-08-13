from django.shortcuts import render

# Create your views here.
"""
    视图实际上就是python函数
    1.视图函数第一个参数就是接受请求,这个请求函数其实就是HttpRequest
    2.必须返回一个响应
"""
from django.http import HttpRequest
from django.http import HttpResponse
def index(request):
    return HttpResponse("ok")
