from django.contrib import admin
from .models import Subject
from django import forms

# Admin Action Functions
def make_active(modeladmin, request, queryset):
    queryset.update(is_active = True)

def make_unactive(modeladmin, request, queryset):
    queryset.update(is_active = False)

# Action description
make_active.short_description = "Mark Selected Subjects as Active"
make_unactive.short_description = "Mark Selected Subjects as Unactive"

class SubjectAdminForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

    def clean_subject_text(self):
        if self.cleaned_data["subject_text"] == "Spike":
            raise forms.ValidationError("Spike is forbidden")

        return self.cleaned_data["subject_text"]

class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = ('subject_text', 'pub_date', 'is_active', 'categories_number', )
    list_filter = ('pub_date', ) 
    actions = [make_active, make_unactive]  
    #defining search 
    search_fields = ("subject_text__startswith", )

    #changing field label
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["subject_text"].label = "Subject name"
        return form




admin.site.register(Subject, SubjectAdmin)

admin.site.site_header = "Django Tutorials by Petro"

