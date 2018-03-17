# -*- coding: utf-8 -*-
"""
 @Time    : 2018/3/13 16:50
 @Author  : CyanZoy
 @File    : urls.py
 @Software: PyCharm
 """
from django.urls import path
from BlogFront import views


urlpatterns = [

    path('register.html', views.register),
    path('register', views.register),
    path('login', views.login_process),
    path('login.html', views.login_process),
    path('note', views.note),
    path('logout', views.logout_process),
    path('', views.index),

]