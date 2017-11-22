from django.shortcuts import render, redirect
from django.contrib import messages
from models import Business

# Returns a list of businesses that match the users search paramaters
def index(request):
    print request.POST["bus_category"]
    context = {
        "business_key" : Business.objects.filter(bus_city=request.POST["bus_city"], bus_category=request.POST["bus_category"]) #.filter(bus_category=request.POST["bus_category"])
    }
    return render(request, "business_app/index.html", context)


# This view returns the business that the user clicked on.
def bus_results(request, bus_id):
    context = {
        "bus_id" : Business.objects.get(id=bus_id)
    }
    return render(request, "business_app/bus_results.html", context)

# Form to create a new Business
def new_bus(request):
    return render(request, "business_app/new_bus.html")


# Insertion of new business into DB
def add_bus(request): 
    #This runs validation to ensure new business name/address is not blank
    errors = Business.objects.new_bus_validator(request.POST)

    if len(errors) <= 0:
        Business.objects.create(bus_name=request.POST["bus_name"], bus_address=request.POST["bus_address"], bus_city=request.POST["bus_city"], bus_category=request.POST["bus_category"])
        last_bus = Business.objects.last()

        return redirect("/display/bus_results/{}".format(last_bus.id)) 
    else:
        for x in errors:
            messages.error(request, errors[x])
        return redirect("/display/new_bus")


def admin(request):
    context = {
        "business_key": Business.objects.all()
    }
    return render(request, "business_app/admin.html", context)


def destroy(request, bus_id):
    Business.objects.get(id=bus_id).delete()
    return redirect("/display/admin")


