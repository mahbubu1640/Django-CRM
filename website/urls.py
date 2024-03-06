from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page,name='home'),
    path('registration/',views.registration_view,name='registration'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('customer_detail/<int:pk>', views.customer_detail,name='customer-detail'),
    #path('customer_detail/<pk:int>/', views.customer_detail, name='customer-detail'),
    # must be correct <int:pk>
    path('delete/<int:pk>/', views.delete_view,name='delete'),
    path('add/',views.add_view,name='add-record'),
    path('update/<int:pk>/',views.update_record,name='update'),
]
