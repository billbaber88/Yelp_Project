from django.shortcuts import render, redirect
from models import Business

def index(request):
    context = {
        "business_key" : Business.objects.all() # Change this to only FILTER businesses that match the location and category that the user searched for.
    }
    return render(request, "business_app/index.html", context)

# This view returns the business that the user clicked on.
def bus_results(request, bus_name):
    context = {
        "bus_name" : Business.objects.get(bus_name=bus_name)
    }
    return render(request, "business_app/bus_results.html", context)