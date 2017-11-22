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


# --------------TO DO ---------------------------
# 1) Popup login on landing page if no username in session.
# 2) ** Display image on business page.
# 3) ** Display profile pic on profile page.
# 4) Standardize color and styling IN PROGRESS
# 5) **Ensure RWD across all browsers.
# 6) Integrate with Google Place API
# 6a) Google Search API
# 7) Insert awesome Easter Egg (circa Web 1.0) IN PROGRESS
# 8) Ability to add new Businesses COMPLETED
# 10)**  average rating + sort by highest rated
# 11)**  Download background images and store in DB.
# 12) Add a checkbox for businesses that allows them (only) to add new businesses
# 13)**  Allow comments and Ratings
# 14) ** validate new business entries.
# 15) ** validate Integer Field to only accept from 1 - 5.

# ----Mendel-----
# Validating new business entries COMPLETED
# Connecting login href's to login app COMPLETED
# ratings = stars
# Validate rating to only allow 1-5 integers

# -----Grant-------
# Finishing users profile page
# Create comment and ratings ability for users to rate businesses
# Images into user profile
# Images into businesses profile
# Images into DB

# ----------Bill-----------
# Continuing CSS