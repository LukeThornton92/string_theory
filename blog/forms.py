from django import forms
from .models import BlogPost, Author, Tag
from django.contrib import messages

class BlogPostForm(forms.ModelForm):
    tag_string = forms.CharField(
        required=True,
        label="Tags",
        help_text="Enter tags separated by commas (e.g., travel, food, technology)",
        widget=forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas *'})
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']  # Remove 'tags' from fields

    def __init__(self, *args, **kwargs):
        """
        Customize form placeholders, autofocus, and handle user-specific data.
        """
        self.user = kwargs.pop('user', None)
        
        # If we're editing an existing post, set initial tag_string
        instance = kwargs.get('instance', None)
        if instance:
            initial = kwargs.get('initial', {})
            # Convert the existing tags to a comma-separated string
            initial['tag_string'] = ', '.join([tag.name for tag in instance.tags.all()])
            kwargs['initial'] = initial
            
        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Enter the blog post title *',
            'content': 'Write your content here *',
        }

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]

        # Set autofocus on the title field
        self.fields['title'].widget.attrs['autofocus'] = True

    def clean_tag_string(self):
        '''Tags to be entered separated with commas'''
        tag_string = self.cleaned_data.get('tag_string')
        if not tag_string:
            raise forms.ValidationError("Please enter at least one tag.")
        
        # Split by comma, strip whitespace, and capitalize the first letter of each tag.
        tag_list = [tag.strip().title() for tag in tag_string.split(',')]

        # Remove empty tags
        tag_list = [tag for tag in tag_list if tag]
        
        if not tag_list:
            raise forms.ValidationError("Please enter at least one non-empty tag.")
        
        # Avoid duplicates in the list itself
        unique_tag_list = []
        for tag_name in tag_list:

            # Check if tag already exists in the database (ignore case)
            tag, created = Tag.objects.get_or_create(name=tag_name)
            
            if created:
                # If the tag was created, ensure it's capitalized before saving
                tag.name = tag_name.title()  # Capitalize the name
                tag.save()
            
            # Add the tag to the list to be returned (even if it already exists)
            unique_tag_list.append(tag_name)
            
        return tag_list

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Ensure a user is provided before setting the author
        if self.user and self.user.is_authenticated:
            author, created = Author.objects.get_or_create(name=self.user.username)
            instance.author = author

        if commit:
            instance.save()
            
            # Process the tags
            tag_list = self.cleaned_data.get('tag_string')
            # Clear existing tags if editing
            instance.tags.clear()
            # Create or get tags and add them to the post
            for tag_name in tag_list:
                tag, created = Tag.objects.get_or_create(name=tag_name.lower())
                instance.tags.add(tag)

        return instance