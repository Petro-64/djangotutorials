from django.contrib import admin
from .models import Tutorial, Contentblock
from django import forms

class TutorialAdminForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = "__all__"

class ContentblockAdminForm(forms.ModelForm):
    class Meta:
        model = Contentblock
        fields = "__all__"



class TutorialAdmin(admin.ModelAdmin):
    change_form_template = 'admin/tutorials/my_change_form.html'
    form = TutorialAdminForm
    list_display = ('tutorial_text', 'category', 'is_active', 'created_by' )
    list_filter = ('category', )


class ContentblockAdmin(admin.ModelAdmin):
    form = ContentblockAdminForm
    list_display = ('description', 'is_visible')

admin.site.register(Tutorial, TutorialAdmin )
admin.site.register(Contentblock )


