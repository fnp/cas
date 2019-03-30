from django.urls import path
from . import views


urlpatterns = [
    path('', views.SSHKeysView.as_view(), name='ssh_keys'),
    path('<int:pk>/delete/', views.DeleteSSHKeyView.as_view(), name='ssh_keys_delete'),
    path('add/', views.AddSSHKeyView.as_view(), name='ssh_keys_add'),

]
