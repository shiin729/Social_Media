from django.shortcuts import render
from .models import Post

# Create your views here.
def ribbon(request):
    all_posts = Post.objects.all()
    
    
<<<<<<< HEAD
    
    
    
    
    context = {
=======
    return render(request, 'content/ribbon.html', context = {
>>>>>>> 2e6780057d60d768dfb2a30f7693243ad7d90e93
        'all_posts': all_posts,
    })