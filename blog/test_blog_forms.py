from django.test import TestCase
from blog.forms import BlogPostForm
from blog.models import Author, BlogPost  # Added BlogPost import
from django.contrib.auth.models import User

class BlogPostFormTest(TestCase):
    def setUp(self):
        """Create an author and a superuser for testing."""
        self.super_user = User.objects.create_superuser(username='superuser', password='password')
        self.author = Author.objects.create(name="Test Author", bio="Test bio")
    
    def test_blog_post_form_valid(self):
        """Test the form with valid data.""" 
        form_data = {
            'title': 'Valid Blog Post Title',
            'content': 'This is the content of a valid blog post.',
            'author': self.author.id,
            'tags': 'Valid, Tags',
            'image': None  # You can also test with an image field if needed
        }
        
        form = BlogPostForm(data=form_data)
        
        # Check if the form is valid
        self.assertTrue(form.is_valid())
        
        # Now, simulate saving the form and check if a BlogPost was created
        blog_post = form.save()
        
        # Check if the BlogPost is saved to the database
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(blog_post.title, 'Valid Blog Post Title')
        self.assertEqual(blog_post.content, 'This is the content of a valid blog post.')
        self.assertEqual(blog_post.author, self.author)
        self.assertEqual(blog_post.tags, 'Valid, Tags')

    def test_blog_post_form_invalid(self):
        """Test the form with invalid data."""
        form_data = {
            'title': '',  # Invalid field
            'content': 'This is content without a title.',
            'author': self.author.id,
            'tags': '',
            'image': None
        }
        
        form = BlogPostForm(data=form_data)
        
        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        
        # Check for specific form errors
        self.assertIn('title', form.errors)  # title is required
        self.assertIn('tags', form.errors)   # tags is required if you add validators for it