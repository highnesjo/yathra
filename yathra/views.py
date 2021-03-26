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