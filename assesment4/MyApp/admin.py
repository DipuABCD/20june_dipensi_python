from django.contrib import admin
from .models import *

# Register your models here.

class studData(admin.ModelAdmin):
    list_display=['name','email','mobile','city']

admin.site.register(userinfo,studData)