from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            if form.cleaned_data.get('clear_avatar'):
                request.user.profile.avatar.delete(save=False)
                request.user.profile.avatar = 'avatars/default.jpg'  # Установите аватарку по умолчанию
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})

@csrf_exempt
def delete_avatar(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.avatar.delete(save=False)
        profile.avatar = 'avatars/default.jpg'  
        profile.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')  
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user or request.user.is_superuser:
        post.delete()
        return redirect('home')
    else:
        return redirect('home')

@login_required    
def post_page(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Ваш комментарий добавлен')
            return redirect('post', post_slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'post.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })
        
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Комментарий успешно удален.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Устанавливаем текущего пользователя как автора поста
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)  # Логируем ошибки сериализации
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)