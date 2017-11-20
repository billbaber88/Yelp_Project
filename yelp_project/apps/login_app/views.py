from django.shortcuts import render, redirect, HttpResponse

def login_index(request):
    response = "Yelp Clone. Login app page."
    return render(request, 'login_app/login_index.html')

