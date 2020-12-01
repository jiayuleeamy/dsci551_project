from django.contrib import admin
from projectapp.models import Business

class Businessadmin(admin.ModelAdmin):
    list_display = ('name','address','stars','hours','categories')
admin.site.register(Business,Businessadmin)

# Register your models here.
