from django.urls import path
from .views import UserRegisterView, UserAuthView, UserConfirmView

urlpatterns = [
    path('api/v1/users/register/', UserRegisterView.as_view(), name='user_register'),
    path('api/v1/users/login/', UserAuthView.as_view(), name='user_login'),
    path('api/v1/users/confirm/', UserConfirmView.as_view(), name='user_confirm'),
]
