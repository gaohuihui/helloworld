from django.shortcuts import render
#coding:utf-8
from django.http import HttpResponse
def index(request):
       return HttpResponse(u"Hello World! 大家好！")
# Create your views here.
