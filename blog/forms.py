from django import forms
from .models import BlogPost, Author
from django.contrib import messages

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'tags', 'image']
        
        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'title': 'title',
                'content': 'content',
                'tags': 'tags',
            }

            self.fields['title'].widget.attrs['autofocus'] = True
            for field in self.fields:
                if field != 'image':
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'IM_IN_FORMS_CHANGE_ME '
                self.fields[field].label = False