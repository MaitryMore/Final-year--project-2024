
from django.contrib import admin
from .models import Database

@admin.register(Database)
class DataAdmin(admin.ModelAdmin):
    pass 

# Register your models here.

# Register your models here.
