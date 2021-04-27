from django.contrib import admin
from .models import Catergory

class CatergoryAdmin(admin.ModelAdmin):
    list_display = ('category_text', 'subject', 'tuitorials_number', 'is_active')
    list_filter = ('subject', 'tuitorials_number') 
    prepopulated_fields = {'url_friendly_text': ('category_text',)}


admin.site.register(Catergory, CatergoryAdmin)
# Register your models here.
