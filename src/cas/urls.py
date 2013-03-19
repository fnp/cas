# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/accounts/')),

    # django-cas-provider
    url(r'^cas/', include('cas_provider.urls')),

    # Admin panel
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^%s(?P<path>.+)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)


