from django.shortcuts import render,redirect
from .form import CreateUserForm
from django.contrib.auth import login

def home_page(request):
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request,'home.html',{'form':form})
