from django.contrib import admin
from django.urls import path
from .views import RegisterView,LoginView
from Inventory.views import ItemsAPI

urlpatterns = [
    path('register/',RegisterView.as_view(),name="register" ),
    path('login/',LoginView.as_view(),name="login"),

    
]
