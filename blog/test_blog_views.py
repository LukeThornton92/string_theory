from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BlogPost, Tag, BlogImage
from datetime import datetime

class BlogViewsTest(TestCase):
    """ Test to see if Blog renders page"""
    def test_blog_view(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)