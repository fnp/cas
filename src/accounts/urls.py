# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^$', 'account_profile'),
    url(r'^change_profile$', 'account_change_basic_profile'),
    url(r'^change_password$', 'account_change_password'),
)
