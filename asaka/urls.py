"""asaka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from asaka.views import INLoginView, RegisterUserView, OUTLogoutView, update_page, delete_page, home
from .decorators import unauthenticated_user, allowed_users

urlpatterns = [
    path('', unauthenticated_user(allowed_users(allowed_roles = ['high', 'middle', 'low'])(home)), name = 'home'),
    path('update-page/<int:pk>', allowed_users(allowed_roles = ['high'])(update_page), name = 'update_page'),
    path('delete-page/<int:pk>', allowed_users(allowed_roles = ['high'])(delete_page), name = 'delete_page'),
    path('login', INLoginView.as_view(), name = 'login_page'),
    path('register', RegisterUserView.as_view(), name = 'register_page'),
    path('logout', OUTLogoutView.as_view(), name = 'logout_page'),
]
