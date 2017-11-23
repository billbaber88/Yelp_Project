"""yelp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.search_app.urls')), # Root route is search since that's the landing page.
    url(r'^display/', include('apps.business_app.urls')), # Displays search results
    url(r'^login/', include('apps.login_app.urls')), #login and registration
]

# ----Mendel-----
# BILL, GRANT, OR MENDEL- Whoever is going to be doing the presentation needs to input a bunch of test data into his DB. That includes multiple businesses in each category, in each city (or just choose one or two cities to demonstrate). Also hardcode business photos and user uploaded photos to some reviews(with some variety. We're using spongebob business photos.

# -----Grant-------
# BILL, GRANT, OR MENDEL- Whoever is going to be doing the presentation needs to input a bunch of test data into his DB. That includes multiple businesses in each category, in each city (or just choose one or two cities to demonstrate). Also hardcode business photos and user uploaded photos to some reviews.(with some variety. We're using spongebob business photos.

# ----------Bill-----------
# PRIORITY CSS for Add a New Business Page
# PRIORITY change the font color for reviews so that they are more visible against the dark background.
# 
# NOT PRIORITY add a kelp logo or href on the login screen that links to the search page for ease of navigation (I have a href in the corner, but it's hard to spot it,)
# NOT PRIORITY Fix login/register and logout buttons so that they are horizontally stacked, not vertically 
# NOT PRIORITY If possible, make the "city" entry on the registration page a drop down selection with our three options (Atlantis, Dead Sea, and Mariana Trench (value="Mariana")). I tried to do it, but I'm not sure how that login form works.
# 
# BILL, GRANT, OR MENDEL- Whoever is going to be doing the presentation needs to input a bunch of test data into his DB. That includes multiple businesses in each category, in each city (or just choose one or two cities to demonstrate). Also hardcode business photos and user uploaded photos to some reviews.(with some variety. We're using spongebob business photos.


# --------------TO DO ---------------------------
# 1) Popup login on landing page if no username in session.
# 2) ** Display image on business page. COPMLETE
# 3) ** Display profile pic on profile page. COMPLETED
# 4) Standardize color and styling COMPLETED
# 5) **Ensure RWD across all browsers. COMPLETED
# 6) Integrate with Google Place API
# 6a) Google Search API
# 7) Insert awesome Easter Egg (circa Web 1.0) IN PROGRESS
# 8) Ability to add new Businesses COMPLETED
# 10)**  average rating + sort by highest rated COMPLETED
# 11)**  Download background images and store in DB.
# 12) Add a checkbox for businesses that allows them (only) to add new businesses
# 13)**  Allow comments and Ratings COMPLETED
# 14) ** validate new business entries. COMPLETE
# 15) ** validate Integer Field to only accept from 1 - 5. COMPLETE