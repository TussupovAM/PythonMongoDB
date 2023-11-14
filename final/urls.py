# urls.py
from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('api/user/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/user/login/', UserLoginView.as_view(), name='user-login'),
    # Добавьте другие URL-маршруты при необходимости
]
