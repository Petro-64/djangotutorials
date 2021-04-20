from django.contrib import admin
from .models import Subject




class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_text', 'pub_date', 'categories_number', )
    list_filter = ('pub_date', )    


admin.site.register(Subject, SubjectAdmin)

