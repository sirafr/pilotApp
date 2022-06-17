from curses.ascii import HT
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound,Http404


# Create your views here.
# def index(requests):
#     return HttpResponse("First view in app1")

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}


def news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "No page for that topic"
        raise Http404("result")

    return HttpResponse(articles[topic])

def add_view(request,num1,num2):
    # domain.com/app1/num1/num2
    add_result = num1+num2
    result = f"{num1}+{num2}={add_result}"

    return HttpResponse(str(result))
 
