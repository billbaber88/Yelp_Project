from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "Yelp Clone. Display business info app. "
    return HttpResponse(response)