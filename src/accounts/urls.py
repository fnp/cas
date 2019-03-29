from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProfileView.as_view(), name='accounts_profile'),
]
