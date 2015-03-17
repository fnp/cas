# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.account_profile),
    url(r'^change_profile$', views.account_change_basic_profile),
    url(r'^change_password$', views.account_change_password),
]
