# -*- coding: utf-8 -*-
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),

    # django-cas-provider
    path('cas/', include('cas_provider.urls')),

    # Admin panel
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
]


if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        path('media/<path>', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
   ]
