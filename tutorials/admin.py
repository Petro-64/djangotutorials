from django.contrib import admin
from .models import Tutorial, Contentblock, Contentcontent
from subjects import models as subject
from categories import models as category
from django import forms
from django.utils.translation import ngettext
from django.contrib import messages
from categories.models import Catergory
from django.db import models
from django.http import HttpResponse
from django.urls import path

class SubjectsListFilter(admin.SimpleListFilter):
    title = 'category'
    parameter_name = 'category'
    default_value = None
    related_filter_parameter = 'category__subject__id__exact'
    def lookups(self, request, model_admin):
        list_of_questions = []
        queryset = Catergory.objects.order_by('subject_id')
        if self.related_filter_parameter in request.GET:
            queryset = queryset.filter(subject_id=request.GET[self.related_filter_parameter])
        for category in queryset:
            list_of_questions.append((str(category.id), category.category_text))
        return sorted(list_of_questions, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category_id=self.value())
        return queryset


class TutorialAdminForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = "__all__"

class ContentblockAdminForm(forms.ModelForm):
    class Meta:
        model = Contentblock
        fields = "__all__"

class ContentcontentAdminForm(forms.ModelForm):
    class Meta:
        model = Contentcontent
        fields = ('content', 'mediapath', 'is_visible', 'tutorial_id', 'block_id')


def add_extra_context_contentcontent(model, request, args, kwargs):#this is for injecting subj id, categ id into tutorial change form. look at TutorialAdmin
        kwargs.setdefault("extra_context", {})
        GET = request.GET.copy()
        ggg = GET.pop('tutorial_id', ['000'])
        if ggg[0] != '000':
            catId = Tutorial.objects.filter(pk=ggg[0]).values_list('category_id')[0][0]
            catName = category.Catergory.objects.filter(pk=catId).values_list('category_text')[0][0]
            subjId = category.Catergory.objects.filter(pk=catId).values_list('subject_id')[0][0]
            subjName = subject.Subject.objects.filter(pk=subjId).values_list('subject_text')[0][0]
            catName = category.Catergory.objects.filter(pk=catId).values_list('category_text')[0][0]


            tutorialName = Tutorial.objects.filter(pk=ggg[0]).values_list('tutorial_text')[0][0]#gives current object parent id
            kwargs["extra_context"]["tutName"] = tutorialName
            kwargs["extra_context"]["catName"] = catName
            kwargs["extra_context"]["subjName"] = subjName
            kwargs["extra_context"]["subjId"] = subjId
            

        kwargs["extra_context"]["tutid"] = ggg[0]


class ContentcontentAdmin(admin.ModelAdmin):
    change_list_template = 'admin/tutorials/my_change_list.html'
    form = ContentcontentAdminForm
    list_display = ['get_block', 'tutorial', 'is_visible' ]
    ordering = ['tutorial_id']

    def changelist_view(self, request, *args, **kwargs):
        add_extra_context_contentcontent(self.model, request, args, kwargs)
        return super(ContentcontentAdmin, self).changelist_view(request, *args, **kwargs)



def add_extra_context(model, request, args, kwargs):#this is for injecting subj id, categ id into tutorial change form. look at TutorialAdmin
        kwargs.setdefault("extra_context", {})
        objid = request.resolver_match.kwargs['object_id']#gives current object id
        catId = Tutorial.objects.filter(pk=objid).values_list('category_id')[0][0]#gives current object parent id
        subId = category.Catergory.objects.filter(pk=catId).values_list('subject_id')[0][0]#gives current object parent id
        kwargs["extra_context"]["objId"] = objid
        kwargs["extra_context"]["catId"] = catId
        kwargs["extra_context"]["subId"] = subId
        #kwargs["extra_context"]["category"] = request.resolver_match.kwargs['object_id']

class TutorialAdmin(admin.ModelAdmin):
    change_form_template = 'admin/tutorials/my_change_form.html'
    form = TutorialAdminForm
    list_display = ('tutorial_text', 'category', 'get_subject', 'fill_tutorial', 'is_active', 'created_by' )
    list_filter = ('category__subject', SubjectsListFilter, 'is_active')
    prepopulated_fields = {'url_friendly_text': ('tutorial_text',)}
    search_fields = ("tutorial_text__startswith", )


    def change_view(self, request, *args, **kwargs):
        add_extra_context(self.model, request, args, kwargs)
        return super(TutorialAdmin, self).change_view(request, *args, **kwargs)


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

class DummyModel(models.Model):

    #class Meta:
        verbose_name_plural = 'Dummy Model'
        app_label = 'tutorials'


def my_custom_view(request):
    return HttpResponse('Admin Custom View')

class DummyModelAdmin(admin.ModelAdmin):
    model = DummyModel
    change_form_template = 'admin/tutorials/my_change_form.html'
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('my_admin_path/', my_custom_view, name=view_name),
        ]


admin.site.register(Tutorial, TutorialAdmin )
admin.site.register(Contentblock, ContentblockAdmin )
admin.site.register(Contentcontent, ContentcontentAdmin )
admin.site.register(DummyModel, DummyModelAdmin)



