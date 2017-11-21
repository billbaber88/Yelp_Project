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


def new_bus(request):
    return render(request, "business_app/new_bus.html")


def add_bus(request): #need to add validatoin for these forms
    Business.objects.create(bus_name=request.POST["bus_name"], bus_address=request.POST["bus_address"], bus_city=request.POST["bus_city"], bus_category=request.POST["bus_category"])
    return redirect("/display/new_bus") #Redirect this to the new business's page.


def admin(request):
    context = {
        "business_key": Business.objects.all()
    }
    return render(request, "business_app/admin.html", context)


def destroy(request, bus_id):
    Business.objects.get(id=bus_id).delete()
    return redirect("/display/admin")


# --------------TO DO ---------------------------
# 1) Popup login on landing page if no username in session.
# 2) Display image on business page.
# 3) Display profile pic on profile page.
# 4) Standardize color and styling
# 5) Ensure RWD across all browsers.
# 6) Integrate with Google Place API
# 6a) Google Search API
# 7) Insert awesome Easter Egg (circa Web 1.0)
# 8) Ability to add new Businesses
# 9) Dropdown filter bar (see Yelp)
#
