from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail, BadHeaderError

def index (request):
    return render (request, 'index.html')