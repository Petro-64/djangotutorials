from django.contrib import admin
from .models import Tutorial, Contentblock, Contentcontent
from subjects import models as subject
from categories import models as category
#from django import forms
from django.utils.translation import ngettext
#from django.contrib import messages
from categories.models import Catergory
from django.db import models
#from django.http import HttpResponse
#from django.urls import path

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
            contentblocksList = Contentblock.objects.all().values_list('id', 'description')
            kwargs["extra_context"]["tutName"] = tutorialName
            kwargs["extra_context"]["catName"] = catName
            kwargs["extra_context"]["subjName"] = subjName
            kwargs["extra_context"]["subjId"] = subjId
            kwargs["extra_context"]["contentblocksList"] = contentblocksList
        kwargs["extra_context"]["tutid"] = ggg[0]

def add_extra_context(model, request, args, kwargs):#this is for injecting subj id, categ id into tutorial change form. look at TutorialAdmin
    kwargs.setdefault("extra_context", {})
    objid = request.resolver_match.kwargs['object_id']#gives current object id
    catId = Tutorial.objects.filter(pk=objid).values_list('category_id')[0][0]#gives current object parent id
    subId = category.Catergory.objects.filter(pk=catId).values_list('subject_id')[0][0]#gives current object parent id
    kwargs["extra_context"]["objId"] = objid
    kwargs["extra_context"]["catId"] = catId
    kwargs["extra_context"]["subId"] = subId
    #kwargs["extra_context"]["category"] = request.resolver_match.kwargs['object_id']