from django.shortcuts import render
from .models import Post

# Create your views here.
def ribbon(request):
    posts = Post.objects.order_by('-created_at')[:10]
    
    
    return render(request, 'content/ribbon.html', {'ribbons': posts})



