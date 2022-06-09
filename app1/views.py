from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
# def index(requests):
#     return HttpResponse("First view in app1")

def simple_view(request):
    return HttpResponse("SIMPLE VIEW")