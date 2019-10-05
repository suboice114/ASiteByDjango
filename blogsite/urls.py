#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/2 12:18
# @Author  : su
# @File    : urls.py

from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.index),
     path('article/<int:article_id>/', views.article_page, name='article_id'),
     path('edit/<int:article_id>/', views.edit_page, name='edit_page'),
     path('edit/action/', views.edit_action, name='edit_action'),
]
