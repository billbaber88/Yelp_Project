from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "Yelp Clone. Login app page.  "
    return HttpResponse(response)