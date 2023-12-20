from django.contrib import admin
from django.urls import path
from ApiApp import views

urlpatterns = [
   path('getall/',views.getall),
   path('   /<int:id>',views.getid),
   path('deleteid/<int:id>',views.deleteid),
   path('savedata/',views.savedata),
   path('updatedata/<int:id>',views.updatedata),
]
