#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, re_path
from apps import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    path('api/poems/', views.PoemsList.as_view()),
    path('api/poetry/', views.PoetryList.as_view()),
    path('api/poems-author/', views.PoemsAuthorList.as_view()),
    path('api/poetry-author/', views.PoetryAuthorList.as_view()),
    path('api/poems-author/<name>/detail/', views.PoemsAuthorDetail.as_view()),
    path('api/poems/<name>/', views.AuthorPoems.as_view()),
    path('api/poetry/<name>/', views.AuthorPoetry.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)
