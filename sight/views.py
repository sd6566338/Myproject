# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json

def line_stack(request):
    return render(request, 'line-stack.html')

def test_list(request):
    # name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    test_list =[{ 'name': '直接访问','data':[100,200,300,400,500,600,700]}]
    # test_list = json.dumps(test_list)
    print(type(test_list))
    print(test_list)
    return JsonResponse(test_list, safe=False)
    # return HttpResponse(test_list)
    # return render(request,'line-stack.html',{'test_list': test_list})