from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User #Imports User table from Login app

class BusinessManager(models.Manager):
    def new_bus_validator(self,postData):
        errors = {}

        if len(postData["bus_name"]) < 3:
            errors["name"] = "Business Name must be over 3 characters"
        
        if len(postData["bus_address"]) < 5:
            errors["address"] = "Business Address must be over 5 characters"

        return errors

    def review_validator(self, postData):
        errors = {}

        # review_text is the name of the textarea box for adding reviews on the write_review.html page
        if len(postData["review_text"]) < 10:
            errors['review'] = "Business reviews must be longer than 10 characters"

        if len(postData["review_text"]) > 2000:
            errors['review2'] = "Business reviews cannot exceed 2000 characters"
            

        if len(postData["rating"]) < 1:
            errors['rating'] = "Rating cannot be left blank"

        if int(postData["rating"]) > 5 or int(postData["rating"]) < 1: #input box stores rating as a str, must convert to int type before validating for correct value.
            errors['rating1'] = "Rating must be a whole number between 1 and 5"
        return errors


class Business(models.Model):
    bus_name = models.CharField(max_length=255)
    bus_address = models.CharField(max_length=255)
    bus_city = models.TextField(max_length=100)
    bus_category = models.TextField(max_length=255)
    description = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(null=True)

    objects = BusinessManager()

class Review(models.Model):
    comment = models.TextField(max_length=2000, null=True, default="PLACEHOLDER TEXT COMMENT/REVIEW")
    rating = models.PositiveSmallIntegerField(null=True)
    images = models.ImageField(null=True)
    business = models.ForeignKey(Business, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")

    objects = BusinessManager()
