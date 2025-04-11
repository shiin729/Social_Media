from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    clear_avatar = forms.BooleanField(required=False, label="Удалить аватарку")
    
    class Meta:
        model = Profile
        fields = ['avatar']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']