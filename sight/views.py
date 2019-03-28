# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'simple.html')

def line_stack(request):
    return render(request, 'line-stack.html')

def add(request):
    getdata = request.GET
    print ("getdata={}".format(getdata))
    a = request.GET['a']
    print ("a={}".format(a))
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))

def ajax_list(request):
    a = list(range(100))
    return JsonResponse(a, safe=False)

def ajax_dict(request):
    # name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    name_dict = [{"name":"xiaoming", "age":20},{"name":"tuweizhong", "age":24},{"name":"xiaoli", "age":33}]
    # name_dict = json.dumps(name_dict)
    print(type(name_dict))
    return JsonResponse(name_dict, safe=False)
    # return HttpResponse(name_dict)

def test_list(request):
    # name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    test_list =[{ 'name': '直接访问','data':[100,200,300,400,500,600,700]}]
    # test_list = json.dumps(test_list)
    print(type(test_list))
    print(test_list)
    return JsonResponse(test_list, safe=False)
    # return HttpResponse(test_list)
    # return render(request,'line-stack.html',{'test_list': test_list})