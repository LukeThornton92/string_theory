from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order
import time
from django.contrib.messages import get_messages

class ProfileViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username=f'testuser_{int(time.time())}', password='testpass')
        # Manually create the user profile if it doesn't exist
        if not hasattr(self.user, 'userprofile'):
            self.profile = UserProfile.objects.create(user=self.user)
        else:
            self.profile = self.user.userprofile
        
        self.url = reverse('profile')
    
    def test_profile_page_loads(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
    
    def test_update_profile(self):
        self.client.force_login(self.user)
        data = {'default_postcode': '202592'}  # Replace with the actual fields from UserProfileForm
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()  # Ensure the profile is updated
        self.assertEqual(self.profile.default_postcode, '202592')  # Replace with actual field checks
    
    def test_invalid_profile_update(self):
        self.client.force_login(self.user)
        data = {'default_postcode': '202592202592202592202592202592202592'}  
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update failed, please ensure the form is valid')

class OrderHistoryViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username=f'testuser_{int(time.time())}', password='testpass')
        
        # Manually create the user profile if it doesn't exist
        if not hasattr(self.user, 'userprofile'):
            self.profile = UserProfile.objects.create(user=self.user)
        else:
            self.profile = self.user.userprofile
        
        # Create a test order associated with the UserProfile
        self.order = Order.objects.create(order_number='12345', user_profile=self.profile, full_name='Test User')  # Ensure correct user_profile is used
        
        # Set the URL for the order history view
        self.url = reverse('order_history', args=[self.order.order_number])

    def test_order_history_view(self):
        # Log the user in
        self.client.login(username='testuser', password='testpass')  # Use correct password here
        
        # Make the request to the view
        response = self.client.get(self.url)

        # Check if the correct order is passed in context
        self.assertEqual(response.context['order'], self.order)

        # Check for the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f'This is a past confirmation for order number {self.order.order_number}. A confirmation email was sent on the order date.')

        # Check if the status code is 200 (page loaded successfully)
        self.assertEqual(response.status_code, 200)

        # Optionally, check for specific content in the response body (e.g., order number)
        self.assertContains(response, str(self.order.order_number))