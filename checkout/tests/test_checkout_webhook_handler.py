'''from django.test import TestCase
from unittest.mock import patch, MagicMock
from django.urls import reverse
from checkout.webhook_handler import StripeWH_Handler
from checkout.models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django.contrib.auth.models import User 
import time
import json

class StripeWH_HandlerTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username=f'testuser_{int(time.time())}', password='testpass')
        
        # Ensure a UserProfile is not created twice for the same user
        self.profile, created = UserProfile.objects.get_or_create(user=self.user)

        # Create a product
        self.product = Product.objects.create(name='Test Guitar', price=500.00, sku='TEST123')

        # Create mock billing and shipping details
        self.billing_details = {
            'email': 'johndoe@example.com',
        }
        
        self.shipping_details = {
            'name': 'John Doe',
            'phone': '1234567890',
            'address': {
                'line1': '123 Test St',
                'line2': 'Apt 1',
                'city': 'Test City',
                'postal_code': '12345',
                'state': 'Test State',
                'country': 'US',
            }
        }

        # Create an order with matching details
        self.order = Order.objects.create(
            full_name=self.shipping_details['name'],
            email=self.billing_details['email'],
            phone_number=self.shipping_details['phone'],
            country=self.shipping_details['address']['country'],
            postcode=self.shipping_details['address']['postal_code'],
            town_or_city=self.shipping_details['address']['city'],
            street_address1=self.shipping_details['address']['line1'],
            street_address2=self.shipping_details['address']['line2'],
            county=self.shipping_details['address']['state'],
            user_profile=self.profile,
            grand_total=500.00,
            stripe_pid='payment_intent_id',
            original_bag=json.dumps({str(self.product.id): 1})
        )

        # Add a line item to the order
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

        # Mock the Stripe event data structure
        mock_shipping = MagicMock()
        mock_shipping.name = self.shipping_details['name']
        mock_shipping.phone = self.shipping_details['phone']
        mock_shipping.address = MagicMock()
        mock_shipping.address.line1 = self.shipping_details['address']['line1']
        mock_shipping.address.line2 = self.shipping_details['address']['line2']
        mock_shipping.address.city = self.shipping_details['address']['city']
        mock_shipping.address.postal_code = self.shipping_details['address']['postal_code']
        mock_shipping.address.state = self.shipping_details['address']['state']
        mock_shipping.address.country = self.shipping_details['address']['country']

        mock_metadata = MagicMock()
        mock_metadata.bag = json.dumps({str(self.product.id): 1})
        mock_metadata.save_info = "true"
        mock_metadata.username = self.user.username

        mock_intent = MagicMock()
        mock_intent.id = "payment_intent_id"
        mock_intent.metadata = mock_metadata
        mock_intent.shipping = mock_shipping
        mock_intent.latest_charge = "ch_123456"

        # Create the mock data object
        mock_data = MagicMock()
        mock_data.object = mock_intent

        # Setup the mock event with proper dictionary-style access
        self.mock_event = MagicMock()
        self.mock_event.data = mock_data
        
        # Make event["type"] return "payment_intent.succeeded"
        def mock_getitem(key):
            if key == "type":
                return "payment_intent.succeeded"
            return MagicMock()
        
        self.mock_event.__getitem__.side_effect = mock_getitem

    @patch('stripe.Charge.retrieve')
    @patch('django.core.mail.send_mail')
    def test_handle_payment_intent_succeeded(self, mock_send_mail, mock_charge_retrieve):
        # Mock the Charge.retrieve call
        mock_charge = MagicMock()
        mock_charge.amount = 50000  # 500.00 in cents
        mock_charge.billing_details = MagicMock()
        mock_charge.billing_details.email = self.billing_details['email']
        
        mock_charge_retrieve.return_value = mock_charge
        
        # Add print statement to verify event type access
        print("\nVerifying event type:", self.mock_event["type"])
        
        handler = StripeWH_Handler(self.client)
        response = handler.handle_payment_intent_succeeded(self.mock_event)
        
        # Assert the response status is correct
        self.assertEqual(response.status_code, 200)
        
        # Verify the order exists
        order = Order.objects.get(stripe_pid="payment_intent_id")
        self.assertIsNotNone(order)
        
        # Verify email was sent and check arguments
        mock_send_mail.assert_called_once()
        
        # If the test fails, print the mock_send_mail call info
        if not mock_send_mail.called:
            print("\nEmail sending info:")
            print("mock_send_mail.call_args:", mock_send_mail.call_args)
            print("mock_send_mail.call_count:", mock_send_mail.call_count)'''