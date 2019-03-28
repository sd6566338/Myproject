# -*- coding:utf-8 -*-


from django.http import HttpResponse
import json

def saledata(request):
   data = { 
   			"data" : [
				{ 
				  "value":"123",
				  "name":"北方大药房"
				},
				{
				  "value":"244",
				  "name":"南方大药房"
				},
				{
			      "value":"360",
			      "name":"美宜佳"
			    },
			    {
			      "value":"666",
			      "name":"和生堂大药房"
			    },
			    {
			      "value":"456",
			      "name":"淘宝大药房"
			    },
			    {
			      "value":"180",
			      "name":"7-11便利店"
			    }
		    ]
	    }
   #ensure_ascii=False用于处理中文
   # json.dumps(data, ensure_ascii=False)
   response = HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")
   response["Access-Control-Allow-Origin"] = "*"
   response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
   response["Access-Control-Max-Age"] = "1000"
   response["Access-Control-Allow-Headers"] = "*"

   return response
