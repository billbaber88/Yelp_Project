from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import User
from ..business_app.models import Business, Review #Importing the Business and Review DB tables from the business_app 


def login_index(request):
    if 'id' in request.session:
        messages.error(request, "There is already a user logged in")
    return render(request,'login_app/login_index.html')


def register(request):
    if 'id' in request.session:
        messages.error(request, "There is already a user logged in") 
        return redirect('/login')
    
    newuser = User.objects.register_validate(request.POST)
    if newuser[0] == False:
        for each in newuser[1]:
            messages.error(request, each) #for each error in the list, make a message for each one.
        return redirect('/login')

    if newuser[0] == True:
        messages.success(request, "You've registered, well done!")
        request.session['id'] = newuser[1].id
        return redirect('/login/user/{}'.format(request.session['id']))


def userlogin(request):   
    if 'id' in request.session:
        messages.add_message(request, messages.INFO,'There is a user already logged in')
        return redirect('/login')
    if request.method == 'GET':
        return redirect('/login')
    else:
        user = User.objects.loginval(request.POST)
        if user[0] == False:
            for each in user[1]:
                messages.add_message(request, messages.INFO, each)
            return redirect('/login')
        if user[0] == True:
            messages.add_message(request, messages.INFO,'Welcome, You are logged in!')
            request.session['id'] = user[1].id
            return redirect('/search')


# Print_Ses only for testing login page:

# def print_ses(request):
#     if 'id' not in request.session:
#         messages.add_message(request, messages.INFO,'No user logged in')
#         print "No user logged in"
#         return redirect('/login')
#     else:
#         print "*********** session.id # below ************"
#         print (request.session['id'])
#         print "*******************************************"
#         context= {
#             "user":User.objects.get(id=request.session['id'])
#         }
#         return render(request, 'login_app/login_index.html', context)


def userlogout(request):
    if 'id' not in request.session:
        return redirect('/search')
    messages.add_message(request, messages.INFO,'You have logged out')
    del request.session['id']
    return redirect('/login')


def show(request, user_id):
    if 'id' not in request.session:
        messages.error(request, "You aren't logged in . Please login or register to see your profile.")
        return redirect('/login')
    else:
        context = {
        'user': User.objects.get(id=user_id),
        "rating_key" : Review.objects.filter(user=User.objects.get(id=user_id))
        }
    return render(request,'login_app/user_page.html',context)
# Personal Note for Grant: ^^^ Semi-User ^^^

def show_error(request):
    messages.error(request, "You aren't logged in . Please login or register to see your profile.")
    return redirect('/login')
    




