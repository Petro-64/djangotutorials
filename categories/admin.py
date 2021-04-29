from django.contrib import admin
from .models import Catergory


# Admin Action Functions
def make_active(modeladmin, request, queryset):
    queryset.update(is_active = True)

def make_unactive(modeladmin, request, queryset):
    queryset.update(is_active = False)
# Action description
make_active.short_description = "Mark Selected Category as Active"
make_unactive.short_description = "Mark Selected Category as Unactive"


class CatergoryAdmin(admin.ModelAdmin):
    change_form_template = 'admin/categories/change_form.html'
    list_display = ('category_text', 'subject', 'tuitorials_number', 'is_active')
    list_filter = ('subject', 'tuitorials_number', 'is_active') 
    prepopulated_fields = {'url_friendly_text': ('category_text',)}
    actions = [make_active, make_unactive]
    search_fields = ("category_text__startswith", )

    #def change_view(self, request, object_id, extra_context=None):
        #self.exclude = ('tuitorials_number', )
        #return super().change_view(request, object_id, extra_context)


admin.site.register(Catergory, CatergoryAdmin)
# Register your models here.
