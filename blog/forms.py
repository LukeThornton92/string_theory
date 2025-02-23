from django import forms
from .models import BlogPost, Author
from django.contrib import messages

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'tags', 'image']
        
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            messages.error(self.request, "Title is required.")
        return title
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            messages.error(self.request, "Blog content is required.")
        return content
    
    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if not tags:
            raise forms.ValidationError("At least one tag is required.")
        return tags