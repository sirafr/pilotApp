from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
# def index(requests):
#     return HttpResponse("First view in app1")

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}


def sports_view(request):
    return HttpResponse(articles['sports'])

def finance_view(request):
    return HttpResponse(articles['finance'])