from django.shortcuts import render, redirect, HttpResponse
from django.conf.urls.static import static
from ..login_app.models import User

def search(request):
    return render(request, 'search_app/search.html')