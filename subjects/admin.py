from django.contrib import admin
from .models import Subject
from django import forms
from django.utils.translation import ngettext
from django.contrib import messages

# Globally disable delete selected
admin.site.disable_action('delete_selected')

class SubjectAdminForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

    #kinda validation
    def clean_subject_text(self):
        if self.cleaned_data["subject_text"] == "Spike":
            raise forms.ValidationError("Spike is forbidden")

        return self.cleaned_data["subject_text"]

class SubjectAdmin(admin.ModelAdmin):
    change_form_template = 'admin/subjects/change_form.html'
    form = SubjectAdminForm
    list_display = ('subject_text', 'pub_date', 'is_active', 'categories_number', )
    list_filter = ('pub_date', 'is_active', 'categories_number') 
    prepopulated_fields = {'url_friendly_text': ('subject_text',)}
    
    #def change_view(self, request, object_id, extra_context=None):
        #self.exclude = ('categories_number', )
        #return super().change_view(request, object_id, extra_context)


    @admin.action(description='Mark Selected Subjects as Active')
    def make_active(self, request, queryset):
        updated = queryset.update(is_active = True)
        self.message_user(request, ngettext(
            '%d subject was successfully marked as active.',
            '%d subjects were successfully marked as active.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark Selected Subjects as Unactive')
    def make_unactive(self, request, queryset):
        updated = queryset.update(is_active = False)
        self.message_user(request, ngettext(
            '%d subject was successfully marked as unactive.',
            '%d subjects were successfully marked as unactive.',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [make_active, make_unactive]

    #def has_delete_permission(self, request, obj=None):
        #return False

    #defining search 
    search_fields = ("subject_text__startswith", )

    #changing field label
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["subject_text"].label = "Subject name"
        return form

admin.site.register(Subject, SubjectAdmin)
admin.site.site_header = "Django Tutorials by Petro"

