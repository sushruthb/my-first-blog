'''
Created on Jul 24, 2017

@author: sbharat
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]