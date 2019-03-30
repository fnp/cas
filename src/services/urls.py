from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/ssh/authorized_keys', views.SshAuthorizedKeysView.as_view()),
]
