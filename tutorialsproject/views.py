from django.shortcuts import render
from django.http import HttpResponse
from subjects.models import Subject
from categories.models import Catergory
from tutorials.models import Tutorial, Contentblock, Contentcontent

import json

def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def blog(request, id=None):
    return render(request, 'blog.html', {})

def get_subject(request):
    data = list(Subject.objects.values('id', 'subject_text'))
    return HttpResponse(json.dumps(data), content_type="application/json")

def get_categories(request, key_id):
    data = list(Catergory.objects.filter(subject_id=int(key_id)).values('id', 'category_text'))
    return HttpResponse(json.dumps(data), content_type="application/json")

def add(request):
    #block_id = int(request.POST['block_id'])
    #tutorial_id = int(request.POST['tutorial_id'])
    block_id = request.POST.get('block_id', 1)
    tutorial_id = request.POST.get('tutorial_id', 1)
    myDict = {"blockId": block_id, "tutorial_id": tutorial_id}
    tutt =Tutorial.objects.get(id=tutorial_id)
    contblock =Contentblock.objects.get(id=block_id)
    if not not request.user.is_superuser:
        contentcontent = Contentcontent(content='sample data', mediapath="mediapath", is_visible=False, tutorial_id=tutt, block_id=contblock, order="asdfasdfas")
        contentcontent.save()
        return HttpResponse(json.dumps(myDict), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"message": 'Permission error'}), content_type="application/json")
