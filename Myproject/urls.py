"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sight.views import index,add,ajax_list,ajax_dict,line_stack,test_list,hello
from sight import heyidata, example
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add/', add, name='add'),
    path('ajax_list/', ajax_list, name='ajax_list'),
    path('ajax_dict/', ajax_dict, name='ajax_dict'),
    path('line_stack/', line_stack, name='line_stack'),
    path('test_list/', test_list, name='test_list'),
    path('heyidata/', heyidata.saledata, name='heyidata'),
    path('example/', example.question, name='example'),
    path('hello/', hello, name='hello'),

]
