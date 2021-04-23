from django.contrib import admin
from .models import Tutorial
from django import forms


#class TutorialAdmin(admin.ModelAdmin):
    #list_filter = ('category')

admin.site.register(Tutorial)
# Register your models here.
