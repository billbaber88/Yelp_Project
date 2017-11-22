from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Displays search results.
    url(r'^bus_results/(?P<bus_id>\d+)$', views.bus_results), # Displays the specific business user selects
    url(r'^new_bus$', views.new_bus), # Add a new business 
    url(r'^add_bus$', views.add_bus), # The route the POST form data will follow to add a new business
    url(r'^write_review/(?P<bus_id>\d+)$', views.write_review), # Route to render page to allow new review.
    url(r'^add_review/(?P<bus_id>\d+)$', views.add_review), # Route to add the new review into DB w/ relationships to User and Business
    url(r'^admin$', views.admin), # Admin Console for removing businesses.
    url(r'^destroy/(?P<bus_id>\d+)$', views.destroy), # Removes a business from the db
    url(r'^destroy_review/(?P<review_id>\d+)$', views.destroy_review), # Removes a review from the db
]