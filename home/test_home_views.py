from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_home_view(self):
        """Test that the index view returns the correct template and status code"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

class ContactUsViewTest(TestCase):
    def test_home_view(self):
        """Test that the contact_us view returns the correct template and status code"""
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact_us.html')

class AboutUsViewTest(TestCase):
    def test_home_view(self):
        """Test that the about_us view returns the correct template and status code"""
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about_us.html')