from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "Yelp Clone. Search Display app  "
    return HttpResponse(response)