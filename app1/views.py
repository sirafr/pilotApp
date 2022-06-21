from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseNotFound,Http404, HttpResponseRedirect

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}

# domain.com/first_app/0---> domain.com/first_app/sports
def news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "No page for that topic"
        raise Http404(result)


def num_page_view(request, num_page):
    url_base = "/app1/"
    topics_list = list(articles.keys()) # [sports,finance,politics]
    topic = topics_list[num_page]

    return HttpResponseRedirect(f"{url_base}{topic}")







