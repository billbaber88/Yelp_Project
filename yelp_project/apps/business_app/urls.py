from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Displays all the search results.
    url(r'^bus_results/(?P<bus_name>.+)$', views.bus_results), # Displays the specific business user selects

]