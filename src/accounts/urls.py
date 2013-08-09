# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, url
from .views import Register

urlpatterns = patterns('accounts.views',
    url(r'^$', 'account_profile', name='account_profile'),
    url(r'^change_profile$', 'account_change_basic_profile'),
    url(r'^change_password$', 'account_change_password'),
)

if settings.REGISTRATION_OPEN:
    urlpatterns += patterns('accounts.views',
        url(r'^register/$', Register.as_view(), name='account_register'),
    )

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^password_reset/$', 'password_reset', name='account_reset_password'),
    url(r'^password_reset_done/$', 'password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb36>[^/]+)/(?P<token>[^/]+)/$', 'password_reset_confirm'),
    url(r'^password_reset_complete/$', 'password_reset_complete'),
)
