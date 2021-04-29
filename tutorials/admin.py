from django.contrib import admin
from .models import Tutorial, Contentblock
from django import forms
from django.utils.translation import ngettext
from django.contrib import messages

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
    list_filter = ('category', 'is_active')
    prepopulated_fields = {'url_friendly_text': ('tutorial_text',)}
    search_fields = ("tutorial_text__startswith", )

    @admin.action(description='Mark Selected Tutorial as Active')
    def make_active(self, request, queryset):
        updated = queryset.update(is_active = True)
        self.message_user(request, ngettext(
            '%d Tutorial was successfully marked as active.',
            '%d Tutorials were successfully marked as active.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark Selected Tutorial as Unactive')
    def make_unactive(self, request, queryset):
        updated = queryset.update(is_active = False)
        self.message_user(request, ngettext(
            '%d Tutorial was successfully marked as unactive.',
            '%d Tutorials were successfully marked as unactive.',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [make_active, make_unactive]


class ContentblockAdmin(admin.ModelAdmin):
    form = ContentblockAdminForm
    list_display = ('description', 'is_visible')

admin.site.register(Tutorial, TutorialAdmin )
admin.site.register(Contentblock )


