from django.contrib import admin
from django.urls import path,include
from societyapp import views

urlpatterns = [
     path('',views.index),
     
]
