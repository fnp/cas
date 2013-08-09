# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.views.defaults import page_not_found

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/accounts/')),

    # django-cas-provider
    url(r'^cas/', include('cas_provider.urls')),

    # Admin panel
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^auth/(email|signup|login|logout|confirm_email)', page_not_found),
    url(r'^auth/', include('allauth.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
