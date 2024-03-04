from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page,name='home'),
    path('login/', views.login_user,name='home'),
    path('logout/', views.logout_user,name='login'),
]
