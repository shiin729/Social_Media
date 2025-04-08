from django.shortcuts import render
from .models import Post

# Create your views here.
def ribbon(request):
    all_posts = Post.objects.all()
    
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'content/ribbon.html', context)