from django import forms
from .models import Image, Comment

class uploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'created_on']