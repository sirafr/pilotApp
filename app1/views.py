from curses.ascii import HT
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


def news_view(request,topic):
    return HttpResponse(articles[topic])

def add_view(request,num1,num2):
    # domain.com/app1/num1/num2
    add_result = num1+num2
    result = f"{num1}+{num2}={add_result}"

    return HttpResponse(str(result))

