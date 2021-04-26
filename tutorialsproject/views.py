from django.shortcuts import render
from django.http import HttpResponse
from subjects.models import Subject
from categories.models import Catergory
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
    #id = request.GET.get('key_id')
    #data = list(Subject.objects.values('id', 'subject_text'))
    data = list(Catergory.objects.filter(subject_id=int(key_id)).values('id', 'category_text'))
    return HttpResponse(json.dumps(data), content_type="application/json")