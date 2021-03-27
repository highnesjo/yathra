from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from yathra.models import story,review
from .forms import *

# Create your views here.

def index(request):
    posts = story.objects.all() 
    reviews = review.objects.all()
    return render(request,'index.html',context= {'posts':posts,'reviews':reviews})


def adminpanel(request):
    if request.method == 'POST':
        form = storyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = storyForm()
    return render(request, 'adminpanel.html', {'form' : form})


def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
             if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
             else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            # messages.error(request,'Invalid login details supplied. Please try again')
            return HttpResponse("Invalid login details supplied. Please try again")
            return HttpResponseRedirect(reverse('index'))

    else:
        #Nothing has been provided for username or password.
        return HttpResponseRedirect(reverse('index'))



@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def reviewadd(request):
    if request.method == 'POST' :
        Review = review()
        Review.user = request.user
        Review.storyid = request.POST.get('storyid')
        Review.review = request.POST.get('review')
        Review.save()
        return HttpResponseRedirect(reverse('index'))


#-------------------------------------------Register----------------------------------------
def register(request):

    registered = False
    if request.method == 'POST':

        # Get info from "both" forms
        user_form = UserForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():        
            user = user_form.save(commit=False)

            if User.objects.filter(email=user.email).exists() :
                print('Already Exists!!')
                return HttpResponse("Email id already exist!!")

            else:

                # Save User Form to Database
                user = user_form.save()
                # Hash the password
                user.set_password(user.password)
                # Update with Hashed password
                user.save()              
                # Registration Successful!
                registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    return render(request,'register.html',{'user_form':user_form , 'registered' : registered })

