from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import date, datetime
from time import strptime
from django.shortcuts import render, redirect

Name_Regex = re.compile(r'^[A-Za-z ]+$')
Email_Regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class userManager(models.Manager):

# Registration Validation**********************************
    def validate (self, postData):
        errors = []
        if len(User.objects.filter(email = postData['email'])) > 0:
            errors.append("User email already exists")
        if postData['password'] != postData['confirm_password']:
            errors.append("Your passwords don't match")
        if len(postData['first_name']) < 1 or len(postData['last_name']) < 1 or len(postData['password']) < 8 or len(postData['user_city']) < 1:
            errors.append("All fields must be entered")
        if not Name_Regex.match(postData['first_name']) or not Name_Regex.match(postData['last_name']):
            errors.append("Names must only be letters")
        if not Name_Regex.match(postData['user_city']):
            errors.append("City names can only be letters")
        if not Email_Regex.match(postData['email']):
            errors.append("Email must be in proper format")
        #create the user
        if len(errors) == 0:
            newuser = User.objects.create(first_name= postData['first_name'], last_name= postData['last_name'], email= postData['email'], user_city= postData['user_city'], password= bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
            return (True, newuser)
        else:
            return (False, errors)

    def loginval(self, postData): # LOGIN VALIDATION******************************************
        errors = []
        if len(postData['email']) < 1 or len(postData['password']) < 1:
            errors.append("Email and password must be entered to login")
            return (False, errors)
        if 'email' in postData and 'password' in postData:
            try:
                print 50*('8')
                user = User.objects.get(email = postData['email'])#userManage acceses the database using .get (finds that one user's object)
            except User.DoesNotExist: #if the user doesnt exist from the .get(.get returns nothin, this 'except' prevents an error message)
                print 50*('4')
                errors.append("User does not exit, try registering")
                return (False, errors)
        #password field/check
        pw_match = bcrypt.hashpw(postData['password'].encode(), user.password.encode())
        if pw_match == user.password:
            return (True, user)
        else:
            errors.append("User login passwords do not match!")
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
