
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .forms import RecordForm

def registration_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request,"You Have Successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'website/register.html',{'form':form})
    return render(request,"website/register.html",{'form':form})




def home_page(request):
    record = Record.objects.all()
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
        return render(request,'website/home.html',{'record':record})
    


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


def customer_detail(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(pk=pk)
        return render(request,'website/customer_details.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You Must Have to login to make changes and view")


def delete_view(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(pk=pk)
        customer_record.delete()
        messages.success(request,"Customer Record Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request,"You Must be Logged in to do that ")
        return redirect('home')    
    

def add_view(request):
    form = RecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid:
                form.save()
                messages.success(request,"Record Added Successfully")
                return redirect('home')
        
        return render(request,'website/add.html',{'form':form})
    else:
        messages.success(request,'You Must be Logged In To Do That')
        return redirect('home')


def update_record(request, pk):
    record_instance = Record.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RecordForm(request.POST, instance=record_instance)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated Successfully")
                return redirect('home')
            else:
                messages.error(request, "Error! Please Enter Correct Record")
        else:
            form = RecordForm(instance=record_instance)
        return render(request, "website/update.html", {"form": form})
    else:
        messages.error(request, "You Must Be Logged In To Do That")
        return redirect('home')

# def update_record(request, pk):
# 	if request.user.is_authenticated:
# 		current_record = Record.objects.get(id=pk)
# 		form = RecordForm(request.POST or None, instance=current_record)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "Record Has Been Updated!")
# 			return redirect('home')
# 		return render(request, 'website/update.html', {'form':form})
# 	else:
# 		messages.success(request, "You Must Be Logged In...")
# 		return redirect('home')
        