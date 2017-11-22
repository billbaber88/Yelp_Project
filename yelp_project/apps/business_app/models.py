from __future__ import unicode_literals
from django.db import models

class BusinessManager(models.Manager):
    def new_bus_validator(self,postData):
        errors = {}

        if len(postData["bus_name"]) < 3:
            errors["name"] = "Business Name must be over 3 characters"
        
        if len(postData["bus_address"]) < 5:
            errors["address"] = "Business Address must be over 5 characters"

        return errors

class Business(models.Model):
    bus_name = models.CharField(max_length=255)
    bus_address = models.CharField(max_length=255)
    bus_city = models.TextField(max_length=100)
    bus_category = models.TextField(max_length=255)
    description = models.TextField(max_length=1000, null=True)
    comment = models.TextField(null=True)
    rating = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(null=True)

    objects = BusinessManager()