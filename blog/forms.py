from django import forms
from .models import BlogPost, Author
from django.contrib import messages

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags', 'image']
        
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Enter title of the blog post *',
            'content': 'Enter content *',
            'tags': 'Enter tags *',
        }
        # form placeholders
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders.get(field, f'{field.capitalize()} *')

        # Set autofocus on the title field
        self.fields['title'].widget.attrs['autofocus'] = True

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Create or get the Author instance corresponding to the logged-in user
        author, created = Author.objects.get_or_create(name=self.user.username)

        # Set the author if it's not already set
        instance.author = author

        if commit:
            instance.save()
        return instance