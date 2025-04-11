from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .form import CreateUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.db.models import Q
from azamat.models import Post
from azamat.forms import PostForm


def home_page(request):
    all_posts = Post.objects.all().order_by('-created_at')
    return render(request,'home.html', context = {
        'all_posts': all_posts,
    })

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

def friends_page(request):
    # username = User.objects.all().get(username=username)
    # user_id = User.objects.get(username=username).id
    # user_avatar = User.objects.get(username=username).profile.avatar.url
    # user_first_name = User.objects.get(username=username).first_name
    # user_last_name = User.objects.get(username=username).last_name
    return render(request,'friends.html')

def other_profile(request, username):
    username = User.objects.all().get(username=username)
    user_id = User.objects.get(username=username).id
    user_avatar = User.objects.get(username=username).profile.avatar.url
    user_first_name = User.objects.get(username=username).first_name
    user_last_name = User.objects.get(username=username).last_name
    if username == request.user:
        return redirect('/my_profile')
    return render(request,'other_profile.html', {'username':username, 'user_avatar':user_avatar, 'user_first_name':user_first_name, 'user_last_name':user_last_name, 'user_id':user_id})

def search_friends(request):
    query = request.GET.get('q', '')
    users = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)).exclude(id=request.user.id)
    users_data = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username, 'avatar': user.profile.avatar.url if user.profile.avatar else '/media/avatars/default.jpeg'} for user in users]
    return JsonResponse({'users': users_data})
