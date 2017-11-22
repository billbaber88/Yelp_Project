from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_index),
    url(r'^register$', views.register),
    url(r'^userlogin$', views.userlogin),
    url(r'^userlogout$', views.userlogout),
    url(r'^user/(?P<user_id>\d+)$', views.show),
    url(r'^print_ses$', views.print_ses),
    
]