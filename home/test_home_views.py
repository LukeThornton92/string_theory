from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_home_view(self):
        """Test that the index view returns the correct template and status code"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')