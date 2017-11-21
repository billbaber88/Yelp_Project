from __future__ import unicode_literals
from django.db import models

class Business(models.Model):
    bus_name = models.CharField(max_length=255)
    bus_address = models.CharField(max_length=255)
    bus_city = models.TextField(max_length=100)
    bus_category = models.TextField(max_length=255)
    comment = models.TextField(null=True)
    rating = models.IntegerField(null=True)

#     ------------------TO DO-------------
#  validate Integer Field to only accept from 1 - 5.
