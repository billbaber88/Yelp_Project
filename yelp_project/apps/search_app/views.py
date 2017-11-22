from django.shortcuts import render, redirect, HttpResponse
from django.conf.urls.static import static

def search(request):
    try:
        request.session['id']
    except ValueError, KeyError:
        return redirect('/login')
    
    return render(request, 'search_app/search.html')