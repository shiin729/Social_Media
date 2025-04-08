from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter post content'}),
        }




