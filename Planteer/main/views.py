from django.http import HttpRequest
from django.shortcuts import render

def home_view(request: HttpRequest):
    return render(request, 'main/index.html')

def contact_view(request: HttpRequest):
    return render(request, 'main/contact.html')

def contact_messages_view(request: HttpRequest):
    return render(request, 'main/contact_messages.html')


