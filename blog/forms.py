from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        pass