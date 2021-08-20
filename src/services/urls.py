from django.urls import path
from . import views


urlpatterns = [
    path('', views.ServicesView.as_view(), name='services'),
    path('<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),
    path('<int:pk>/ssh/authorized_keys', views.SshAuthorizedKeysView.as_view()),
]
