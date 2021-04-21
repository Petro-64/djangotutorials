from django.contrib import admin
from .models import Subject

# Admin Action Functions
def make_active(modeladmin, request, queryset):
    queryset.update(is_active = True)

def make_unactive(modeladmin, request, queryset):
    queryset.update(is_active = False)

# Action description
make_active.short_description = "Mark Selected Subjects as Active"
make_unactive.short_description = "Mark Selected Subjects as Unactive"


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_text', 'pub_date', 'is_active', 'categories_number', )
    list_filter = ('pub_date', ) 
    actions = [make_active, make_unactive]   


admin.site.register(Subject, SubjectAdmin)

admin.site.site_header = "Django Tutorials by Petro"

