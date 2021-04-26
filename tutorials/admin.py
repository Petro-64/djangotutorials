from django.contrib import admin
from .models import Tutorial
from django import forms

class TutorialAdminForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = "__all__"

@admin.register(Tutorial)


class TutorialAdmin(admin.ModelAdmin):
    form = TutorialAdminForm
    list_display = ('tutorial_text', 'category', 'is_active', 'created_by' )
    #list_display = ['category']
    #readonly_fields = ['category']
    #pub_date = models.DateTimeField(auto_now_add = True)
    #category = models.ForeignKey(category.Catergory, on_delete=models.CASCADE, default=1)
    #tutorial_text = models.CharField(max_length=30)
    #is_active = models.BooleanField(default=False)
    #url_friendly_text = models.CharField(max_length=50, default='url-friendly-tutorial-name')
    #created_by = models.CharField(max_length=30, default='admin')
    #views = models.IntegerField(default=0)
    pass


