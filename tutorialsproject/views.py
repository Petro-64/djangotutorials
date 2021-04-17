from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the main 11 index.")


def about(request):
    return HttpResponse("You're at the about.")

def contact(request):
    return render(request, 'contact.html', {})