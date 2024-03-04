
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages



def registration_view(request):
    return render(request,"website/register.html")




def home_page(request):
    # if check to see logging in 
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        # authenticate 
        user = authenticate (request,username = username,password = password)
        if user is not None:
            login(request,user) 
            messages.success(request,"You have been successsfully Logged In!")
            return redirect('home')
        else:
            messages.error(request,"There Was an error logging in , Please try again later")
            return redirect('home')
    else:
        return render(request,'website/home.html',{})
    


def login_user(request):
    if request.method== "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate ( request, username= username , password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been successfully Logged in ")
            return redirect('home')
        else:
            messages.error(request,"You Have Entered Wrong Username and Password , Please Try Again Later")
            return redirect('home')
    else:
        return render(request,'website/home.html')
        
def logout_user(request):
    logout(request)
    messages.success(request,"You have been successfully logged out")
    return redirect('home')
