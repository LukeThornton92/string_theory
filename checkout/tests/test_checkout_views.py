from django.test import TestCase, Client
from ..views import cache_checkout_data, checkout, checkout_success

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.conf import settings
from unittest.mock import patch
from checkout.models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time

class CheckoutViewsTest(TestCase):
    def setUp(self):
        """Sets up the test client, user, profile, and other required objects."""
        self.client = Client()
        self.user = User.objects.create_user(username=f'testuser_{int(time.time())}', password='testpass')

        # Check if a UserProfile exists for the user, and create one if not
        self.user_profile, created = UserProfile.objects.get_or_create(user=self.user)

        self.product = Product.objects.create(
            name='Test Product', price=100.00, sku='123456'
        )

        '''# Set up a session with a bag
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}  # Product added to cart
        session.save()'''

        # Order data to be entered
        self.order_data = {
            'full_name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone_number': '123456789',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': 'Test County',
        }

        # Create the order object
        self.order = Order.objects.create(
            order_number='', #Leave empty! its autogenerated!
            user_profile=self.user_profile, 
            email=self.order_data['email'],
            phone_number=self.order_data['phone_number'],
            country=self.order_data['country'],
            postcode=self.order_data['postcode'],
            town_or_city=self.order_data['town_or_city'],
            street_address1=self.order_data['street_address1'],
            street_address2=self.order_data['street_address2'],
            county=self.order_data['county']
        )

        self.order.refresh_from_db() # Ensures order_number has been generated
        self.order_number = self.order.order_number  # Stores the generated order_number

    def test_checkout_view(self):
        """Tests if the checkout page loads successfully"""

        # Set up the session with a product in the cart
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()

        response = self.client.get(reverse('checkout'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

        # Checks that the checkout form contains the necessary fields
        self.assertContains(response, 'name="full_name"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="phone_number"')
        self.assertContains(response, 'name="country"')
        self.assertContains(response, 'name="postcode"')
        self.assertContains(response, 'name="town_or_city"')
        self.assertContains(response, 'name="street_address1"')
        self.assertContains(response, 'name="street_address2"')
        self.assertContains(response, 'name="county"')
        
    def test_checkout_view_post_valid_authenticated(self):
        """Test that the checkout view processes the order correctly on POST."""

        # Log the user in using force_login
        self.client.force_login(self.user)
        
        # Set up the session with a product in the cart
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()
        form_data = self.order_data
        

        # Mock the Stripe PaymentIntent creation to return a mock client_secret
        with patch('stripe.PaymentIntent.create') as mock_create:
            mock_create.return_value.client_secret = 'mock_client_secret_123'

            # Add the mock client_secret to form_data
            form_data['client_secret'] = 'mock_client_secret_123'

            # Update the session data for the bag
            self.client.session['bag'] = {str(self.product.id): 1}
            self.client.session.save()
            response = self.client.post(reverse('checkout'), data=form_data)

            # Check if it's a redirected to checkout_success
            self.assertEqual(response.status_code, 302)
            order_number = Order.objects.last().order_number  # checkout_success needs the order number
            self.assertRedirects(response, reverse('checkout_success', args=[order_number]))

            # Verify if the order line item is created
            self.assertEqual(OrderLineItem.objects.count(), 1)
            order_line_item = OrderLineItem.objects.first()
            self.assertIsNotNone(order_line_item)
            self.assertEqual(order_line_item.product, self.product)
            self.assertEqual(order_line_item.quantity, 1)
    
    def test_save_info_in_post(self):
        """Test that save_info flag in POST redirects to checkout_success."""
        self.client.force_login(self.user)
        # Set up valid form data
        form_data = self.order_data
        form_data['save_info'] = 'save-info'  # Add 'save-info' to simulate saving info

        # Add a mock client_secret to the form data
        form_data['client_secret'] = 'mock_client_secret_123'  # Simulate a valid client_secret from Stripe

        # Set up the session with a product in the cart
        self.client.session['bag'] = {str(self.product.id): 3}
        self.client.session.save()

        # Mock the Stripe PaymentIntent creation to return a mock client_secret
        with patch('stripe.PaymentIntent.create') as mock_create:
            # Mock the response of Stripe's create method
            mock_create.return_value.client_secret = 'mock_client_secret_123'

            # Make the POST request with form data and the mocked Stripe client_secret
            response = self.client.post(reverse('checkout'), data=form_data)

            # Ensure the session is saved and the 'save_info' flag is set
            self.client.session.save()

            # Check that the user is redirected to the checkout success page
            order_number = Order.objects.last().order_number  # Get the most recent order number created
            self.assertRedirects(response, reverse('checkout_success', args=[order_number]))
    
    """def test_product_does_not_exist(self):
        Test that if a product is not found, an error is shown and the user is redirected.

        #logs in the setUp user
        self.client.force_login(self.user)
        form_data = self.order_data

        # Update the session data for the bag
        self.client.session['bag'] = {
            str(self.product.id): 1,
            str(9999):1 
        }
        self.client.session.save()

        # Mock the Stripe PaymentIntent creation to return a mock client_secret
        with patch('stripe.PaymentIntent.create') as mock_create:
            mock_create.return_value.client_secret = 'mock_client_secret_123'

            # Add the mock client_secret to form_data
            form_data['client_secret'] = 'mock_client_secret_123'

            response = self.client.post(reverse('checkout'), data=form_data)

            # Check that an error message is shown
            messages = [msg.message for msg in get_messages(response.wsgi_request)]
            self.assertIn("One of the products in your bag wasn't found in our database. Please call us for assistance!", messages)

            # Check that the order is deleted and no line items were created
            self.assertEqual(OrderLineItem.objects.count(), 0)

            # Check that the user is redirected to the bag view
            self.assertRedirects(response, reverse('view_bag'))"""
    
    def test_checkout_form_error_message(self):
        """Test that an error message appears when form submission is invalid."""

        # Log the user in using force_login
        self.client.force_login(self.user)
        
        # Set up the session with a product in the cart
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()
        
        form_data = {
            'full_name': '',
            'email': 'johndoe@example.com',
            'phone_number': '123456789',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': 'Test County',
        }
        # Mock the Stripe PaymentIntent creation to return a mock client_secret
        with patch('stripe.PaymentIntent.create') as mock_create:
            mock_create.return_value.client_secret = 'mock_client_secret_123'

            # Add the mock client_secret to form_data
            form_data['client_secret'] = 'mock_client_secret_123'
            
            response = self.client.post(reverse('checkout'), data=form_data)
            
            # Check that the form is invalid
            order_form = response.context['order_form']
            self.assertFalse(order_form.is_valid())

            # Extract messages from response
            messages = [msg.message for msg in get_messages(response.wsgi_request)]

            # Assert that the error message is in the messages list
            self.assertIn('There was an error with your form. Please double check your information.', messages)

            # Ensure the user is not redirected to checkout_success
            self.assertTemplateUsed(response, 'checkout/checkout.html')
    
    def test_empty_bag(self):
        """Test that if the bag is empty, an error is shown and the user is redirected."""
        # Create a new user
        user = User.objects.create_user(username='testuser', password='password')
        self.client.force_login(user)  # Log the user in

        # Clear the session and set the 'bag' to be empty
        self.client.session.clear()
        self.client.session['bag'] = {}
        self.client.session.save() 

        # Mock the Stripe PaymentIntent creation to return a mock client_secret
        form_data = {'client_secret': 'mock_client_secret_123'}

        # Send the GET request with the form data
        response = self.client.get(reverse('checkout'), data=form_data)

        # Check the messages that were generated
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("There's nothing in your bag at the moment", messages)
        self.assertRedirects(response, reverse('products'))

    """def test_authenticated_user_with_profile(self):
        Test that the order form is populated with profile data for authenticated users.

        # Create the user
        self.user = User.objects.create_user(username='johndoe', password='password')

        # Delete any existing user profile to ensure a new one is created
        UserProfile.objects.filter(user=self.user).delete()

        # Create a new user profile
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            default_phone_number='123456789',
            default_country='US',
            default_postcode='12345',
            default_town_or_city='Test City',
            default_street_address1='123 Test St',
            default_street_address2='',
            default_county='Test County'
        )
        
        # Log the user in using force_login
        self.client.force_login(self.user)

        # Make the GET request to the checkout view
        response = self.client.get(reverse('checkout'))

        # Assert that 'order_form' is passed in context
        self.assertIn('order_form', response.context)
        order_form = response.context['order_form']

        # Debugging: print out the response context
        print(response.context)  # This will show what is inside the context

        # Assert that the form is populated with profile data
        self.assertEqual(order_form.initial['full_name'], self.user_profile.user.get_full_name())
        self.assertEqual(order_form.initial['email'], self.user_profile.user.email)
        self.assertEqual(order_form.initial['phone_number'], self.user_profile.default_phone_number)
        self.assertEqual(order_form.initial['country'], self.user_profile.default_country)
        self.assertEqual(order_form.initial['postcode'], self.user_profile.default_postcode)
        self.assertEqual(order_form.initial['town_or_city'], self.user_profile.default_town_or_city)
        self.assertEqual(order_form.initial['street_address1'], self.user_profile.default_street_address1)
        self.assertEqual(order_form.initial['street_address2'], self.user_profile.default_street_address2)
        self.assertEqual(order_form.initial['county'], self.user_profile.default_county)"""
            
    def test_checkout_success_view(self):
        """Test if checkout_success page renders correctly, displays success message, updates the order, and clears the session"""
        session = self.client.session
        session['save_info'] = True
        session.save()

        # Log the user in from setUp
        self.client.force_login(self.user)
        # Order created in setUp
        order_number = self.order.order_number
        # Set session data
        self.client.session['save_info'] = 'true'
        self.client.session['bag'] = {'1': 2}
        # Call the checkout_success view
        response = self.client.get(reverse('checkout_success', kwargs={'order_number': self.order.order_number}))
        # Check response status
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        # Check if the success message is present in the response
        self.assertContains(response, f'Order successfully processed! Your order number is {self.order_number}. A confirmation email will be sent to {self.order.email}.')
        # Ensure the order's user_profile is updated
        self.order.refresh_from_db()
        self.assertEqual(self.order.user_profile.default_phone_number, self.order.phone_number)
        # Ensure the session 'bag' is cleared
        self.assertNotIn('bag', self.client.session)

class CacheCheckoutDataTest(TestCase):
    ''' Needed new setup(self) '''
    def setUp(self):
        self.client = Client()
        self.url = reverse('cache_checkout_data')  # Ensure this matches your URLs
        self.session = self.client.session
        self.session['bag'] = {'1': 2}  # Fake bag with 2 items of product ID 1
        self.session.save()

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data_success(self, mock_stripe):
        """Test cache_checkout_data with valid data"""

        # Create a real User object (needs to be unique each time)
        username = f'testuser_{int(time.time())}'
        user = User.objects.create_user(username=username, password='password')
        # Log in the user
        self.client.force_login(user)
        # Simulate successful Stripe response
        mock_stripe.return_value = {}

        response = self.client.post(self.url, {
            'client_secret': 'pi_12345_secret_67890',
            'save_info': 'true',
        })

        self.assertEqual(response.status_code, 200)
        mock_stripe.modify('pi_12345', metadata={
            'bag': '{"1": 2}', 
            'save_info': 'true', 
            'username': str(user.username)  # Ensure the username is a string
        })

    @patch('checkout.views.stripe.PaymentIntent.modify', side_effect=Exception("Stripe Error"))
    def test_cache_checkout_data_failure(self, mock_stripe):
        """ Test cache_checkout_data with a Stripe error """
        
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(self.url, {
            'client_secret': 'pi_12345_secret_67890',
            'save_info': 'true',
        })

        self.assertEqual(response.status_code, 400)
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('Sorry, your payment cannot be processed right now. Please try again later.', messages)