from django.shortcuts import render,redirect
from .froms import UserRegistrationForm
from django.contrib import messages

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
