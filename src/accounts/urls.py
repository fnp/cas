from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView.as_view(), name='accounts_profile'),
    path('onboarding/', views.OnboardingView.as_view(), name='onboarding'),
]
