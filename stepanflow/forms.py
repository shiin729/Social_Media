from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите заголовок'}),
            'image': forms.ClearableFileInput(),  # без multiple=True
            'content': forms.Textarea(attrs={'placeholder': 'Введите текст поста'}),
        }
#asd