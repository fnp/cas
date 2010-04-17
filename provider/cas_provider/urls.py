from django.conf.urls.defaults import *

from cas_provider.views import *

urlpatterns = patterns('',
    url(r'^login/$', login),
    url(r'^validate/$', validate),
    url(r'^serviceValidate/$', service_validate),
    url(r'^logout/$', logout),
)