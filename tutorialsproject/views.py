from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return HttpResponse("You're at the about.")

def contact(request):
    return render(request, 'contact.html', {})