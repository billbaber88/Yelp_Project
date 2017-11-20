from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import date, datetime
from time import strptime

Name_Regex = re.compile(r'^[A-Za-z ]+$')
Email_Regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class userManager(models.Manager):
    def validate (self, postData):
        errors = []
        if len(User.objects.filter(username = postData['email'])) > 0:
            errors.append("User email already exists")
        if postData['password'] != postData['confirm_password']:
            errors.append("Your passwords don't match")
        if len(postData['first_name']) < 2:
            errors.append("First name needs to be more than 2 letter")
        if len(postData['last_name']) < 2:
            errors.append("Last name needs to be more than 2 letter")
        if not Name_Regex.match(postData['first_name']):
            errors.append("name can only be letters")
        if not Name_Regex.match(postData['last_name']):
            errors.append("name can only be letters")
        if len(postData['password']) < 8:
            errors.append("Password needs to be more than 8 letters")
        if len(postData['user_city']) < 1:
            errors.append("City Field Must be entered")
        if not Name_Regex.match(postData['user_city']):
            errors.append("City names can only be letters")
        if not Email_Regex.match(postData['email']):
            errors.append("email must be in proper format: ex/ name@website.com")
        if len(errors) == 0:
#create the user
            newuser = User.objects.create(first_name= postData['first_name'], last_name= postData['last_name'], email= postData['username'], user_city= postData['user_city'], password= bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
            return (True, newuser)
        else:
            return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    user_city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
