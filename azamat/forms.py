from django import forms
from .models import Profile, Post, Comment

class ProfileForm(forms.ModelForm):
    clear_avatar = forms.BooleanField(required=False, label="Удалить аватарку")
    
    class Meta:
        model = Profile
        fields = ['avatar']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Введите ваш комментарий...', 'rows': 3}),
        }