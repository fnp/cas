from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings


admin.site.site_header = settings.SITE_TITLE


urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),

    # django-cas-provider
    path('cas/', include('cas_provider.urls')),

    # Admin panel
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path('email/', include('emails.urls')),
    path('services/', include('services.urls')),
    path('ssh/', include('ssh_keys.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        path('media/<path>', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
   ]
