from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    clear_avatar = forms.BooleanField(required=False, label="Удалить аватарку")
    
    class Meta:
        model = Profile
        fields = ['avatar']