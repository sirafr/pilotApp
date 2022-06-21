from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseNotFound,Http404, HttpResponseRedirect
from django.urls import reverse


def simple_view(request):
    return render(request,"app1/example.html") #.HTML 





