# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/accounts/', permanent=False)),

    # django-cas-provider
    url(r'^cas/', include('cas_provider.urls')),

    # Admin panel
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('accounts.urls')),
]


if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
   ]
