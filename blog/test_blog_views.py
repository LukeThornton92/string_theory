from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

class BlogViewsTest(TestCase):
    def setUp(self):
        self.super_user = User.objects.create_superuser(username='superuser', password='password')
        ''' Set up a BlogPost for edit view test
        self.blog_post = BlogPost.objects.create(
            title="Test Post", 
            content="Test Content", 
            author=self.super_user
        )'''

    def test_blog_view(self):
        """ Test to see if Blog renders page """
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_add_view(self):
        """ Test to see if Blog create page renders """
        url = reverse('add_blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')  # Ensure a form exists on the page
        self.assertContains(response, 'name="title"')  # Ensure title field is prefilled with post data
        self.assertContains(response, 'name="content"')  # Ensure content field is prefilled
    
    '''def test_blog_edit_view(self):
         """Test to see if Blog edit page renders """
        blog_post = BlogPost.objects.create(title="Test Post", content="Test Content", author=self.super_user)
        url = reverse('edit_blog', args=[blog_post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="title"')
        self.assertContains(response, 'name="content"') '''