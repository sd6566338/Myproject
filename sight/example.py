# -*- coding:utf-8 -*-


from django.http import HttpResponse
import json

def question(request):
    if request.method == 'GET' and 'question' in request.GET:
       question = request.GET['question']
       print(question)
       data = {"answer": "answer"}
       #ensure_ascii=False用于处理中文
#       return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")

       response = HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")
       response["Access-Control-Allow-Origin"] = '*'
       return response
