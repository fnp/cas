from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_aliases, name='emails'),
    path('user/<username>/', views.user_aliases, name='emails_user'),
]
