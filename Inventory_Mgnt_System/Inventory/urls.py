
from django.contrib import admin
from django.urls import path
from .views import ItemsAPI

urlpatterns = [
   path('items/',ItemsAPI.as_view(),name="items"),
   path('items/<int:id>/',ItemsAPI.as_view(),name="item"),
]