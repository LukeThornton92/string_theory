from django.test import TestCase
from django.urls import reverse

class BlogViewsTest(TestCase):
    def test_blog_view(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)