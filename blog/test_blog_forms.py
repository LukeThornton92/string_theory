from django.test import TestCase
from blog.forms import BlogPostForm
from blog.models import Author, BlogPost  # Added BlogPost import
from django.contrib.auth.models import User

class BlogPostFormTest(TestCase):
    def setUp(self):
        """Create an author and a superuser for testing."""
        self.super_user = User.objects.create_superuser(username='superuser', password='password')
        self.author = Author.objects.create(name="Test Author", bio="Test bio")
        form = BlogPostForm(data={'title': 'Test Title', 'content': 'Test Content'}, user=self.super_user)
    
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

    def test_blog_post_form_valid(self):
        """ Test the form with valid data """
        # Prepare form data
        data = {
            'title': 'Test Blog',
            'content': 'This is a test blog post',
            'tags': 'test, blog'
        }

        # Create a form instance with the user passed as an argument
        form = BlogPostForm(data, user=self.user)
        
        self.assertTrue(form.is_valid())  # Check if the form is valid

        # Save the form and get the created blog post
        blog_post = form.save()

        # Ensure the blog post was saved and the author is correctly assigned
        self.assertEqual(blog_post.author.name, self.user.username)