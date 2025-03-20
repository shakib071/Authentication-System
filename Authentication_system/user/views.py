from django.shortcuts import render,redirect
from .froms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def user_signUp(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"SignUp Successful")
            return redirect('homepage')
    else:
        form = UserRegistrationForm()
            
    return render(request,'signup.html',{'form':form})

def user_login(request):
    # user_data = request.POST
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request,"Logged in Successfully")
                return redirect('homepage')
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})


def user_profile(request):
    user_name = request.user.username
    return render(request,'profile.html' , {'username': user_name})

def user_logout(request):
    logout(request)
    return redirect('login')
