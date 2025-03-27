"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import UserRegisterView, UserAuthView, UserConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/register/', UserRegisterView.as_view(), name='user_register'),
    path('api/v1/users/login/', UserAuthView.as_view(), name='user_login'),
    path('api/v1/users/confirm/', UserConfirmView.as_view(), name='user_confirm'),
    path('api/', include('movies.urls')),
]

