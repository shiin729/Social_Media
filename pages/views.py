from django.shortcuts import render,redirect
from .form import CreateUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    return render(request,'home.html')

def register_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request,'register.html',{'form':form})

def logout_page(request):
    logout(request)
    return redirect('/')

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

