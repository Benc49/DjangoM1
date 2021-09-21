from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.
def hello_view(request: HttpRequest):
    return HttpResponse ("Hello World")