from django.shortcuts import render
from azamat.models import Post

# Create your views here.
def ribbon(request):
    all_posts = Post.objects.all()
    
    
    return render(request, 'content/ribbon.html', context = {
        'all_posts': all_posts,
    })