from django.test import TestCase
from blog.forms import BlogPostForm
from blog.models import Author, BlogPost, Tag
from django.contrib.auth.models import User

class BlogPostFormTest(TestCase):
    def setUp(self):
        """Create an author and a superuser for testing."""
        self.super_user = User.objects.create_superuser(username='superuser', password='password')
        self.author = Author.objects.create(name="Test Author", bio="Test bio")

        self.tag1 = Tag.objects.create(name="Valid")
        self.tag2 = Tag.objects.create(name="Tags")
        
    def test_blog_post_form_valid(self):
        """Test the form with valid data.""" 
        form_data = {
            'title': 'Valid Blog Post Title',
            'content': 'This is the content of a valid blog post.',
            'tag_string': [self.tag1.id, self.tag2.id],
            'image': None
        }
        
        form = BlogPostForm(data=form_data, user=self.super_user)

        self.assertTrue(form.is_valid())

        blog_post = form.save()
        
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(blog_post.title, 'Valid Blog Post Title')
        self.assertEqual(blog_post.content, 'This is the content of a valid blog post.')
        self.assertEqual(blog_post.author.name, self.super_user.username)  # Ensure correct author assignment