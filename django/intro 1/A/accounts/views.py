from django.shortcuts import render , redirect
from .forms import UserRegisterationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout


def user_register(request):
    if request.method=="POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(username=cd['username'] , password=cd['password'] , email=cd['email'])
            messages.success(request,'user is registered' , 'success')
            return redirect('home')

    else:
        form = UserRegisterationForm() #Get : if user entered the page by url

    return render(request , 'register.html' , {'form':form})


def user_login(request):
    if request.method=="POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username =cd['username'] , password =cd['password'] , email=cd['email'])
            if user is not None:
                login(request , user)
                messages.success(request,'logined successfully' , 'success')
            else:
                messages.error(request,'invalid information check your login stuffs again', 'danger')
    else:
        form = UserLoginForm() #Get : if user entered the page by url

    return render(request, 'login.html', {'form':form})



def user_logout(request):

    logout(request)
    messages.success(request,'logged out successfully ' , 'success')
    return redirect('home')