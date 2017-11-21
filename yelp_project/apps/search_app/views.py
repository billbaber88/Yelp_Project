from django.shortcuts import render, redirect, HttpResponse
from django.conf.urls.static import static

def search(request):
    response = "Yelp Clone. Search Display app  "
    return render(request, 'search_app/search.html')