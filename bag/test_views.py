from django.test import TestCase
from django.urls import reverse
from products.models import Product
from django.contrib.messages import get_messages

class BagViewsTest(TestCase):
    def test_view_bag(self):
        """Test the view_bag view"""
        response = self.client.get(reverse('view_bag'))  # Assuming 'view_bag' is the URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        """Test adding a product to the bag"""
        # Create a product instance
        product = Product.objects.create(name="Test Product", price=10.00)
        
        # Simulate adding the product to the bag
        response = self.client.post(reverse('add_to_bag', args=[product.id]), {'quantity': 1})

        # Check if redirected
        self.assertRedirects(response, '/')

        # Check if the product is in the session
        self.assertIn(str(product.id), self.client.session['bag'])

    def test_adjust_bag(self):
        """Test adjusting the quantity of an item in the bag"""
        # Create a product instance
        product = Product.objects.create(name="Test Product", price=10.00)

        # Add product to the bag
        self.client.post(reverse('add_to_bag', args=[product.id]), {'quantity': 1})

        # Simulate adjusting the quantity
        response = self.client.post(reverse('adjust_bag', args=[product.id]), {'quantity': 2})

        # Check if the quantity is updated
        self.assertEqual(self.client.session['bag'][str(product.id)], 2)

    def test_remove_from_bag(self):
        """Test removing a product from the bag"""
        # Create a product instance
        product = Product.objects.create(name="Test Product", price=10.00)

        # Add product to the bag
        self.client.post(reverse('add_to_bag', args=[product.id]), {'quantity': 1})

        # Simulate removing the product
        response = self.client.post(reverse('remove_from_bag', args=[product.id]))

        # Check if the product is removed from the bag
        self.assertNotIn(str(product.id), self.client.session['bag'])
        self.assertEqual(response.status_code, 200)

class BagViewsTestHigherLower(TestCase):
    def setUp(self):
        # Set up your test product and session
        self.client.session.clear()
        self.product = Product.objects.create(name="Test Guitar", price=200)
        self.url_adjust_bag = reverse('adjust_bag', args=[self.product.id])
        self.url_remove_from_bag = reverse('remove_from_bag', args=[self.product.id])

        # Manually add the product to the session without triggering the "added to bag" message
        bag = self.client.session.get('bag', {})
        bag[str(self.product.id)] = 1  # Add product with initial quantity of 1
        self.client.session['bag'] = bag
        self.client.session.save()

    def test_adjust_bag_quantity_above_99(self):
        response = self.client.post(self.url_adjust_bag, {'quantity': 150})
        messages = list(get_messages(response.wsgi_request))
        
        self.assertEqual(len(messages), 1)  # Expect only one message for limiting quantity
        self.assertEqual(str(messages[0]), 'Please stop trying to break my site!')
        self.assertEqual(response.status_code, 302)  # Redirect after successful adjustment
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 99)


    def test_adjust_bag_quantity_below_1(self):
        # Trying to adjust quantity below 1 (0 in this case)
        response = self.client.post(self.url_adjust_bag, {'quantity': 0})
        messages = list(get_messages(response.wsgi_request))
        
        self.assertEqual(len(messages), 1)  # Expect only one message for limiting quantity
        self.assertEqual(str(messages[0]), 'Please stop trying to break my site!')
        self.assertEqual(response.status_code, 302)  # Redirect after successful adjustment
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 1)

    def test_adjust_bag_valid_quantity(self):
        # Trying to adjust quantity to a valid value (2)
        response = self.client.post(self.url_adjust_bag, {'quantity': 2})
        # Getting the messages from the response
        messages = list(get_messages(response.wsgi_request))
        
        # Verify that the message is correct
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Updated Test Guitar to 2')
        self.assertEqual(response.status_code, 302)
        # Verify the bag has the correct quantity (should be 2)
        self.assertEqual(self.client.session['bag'][str(self.product.id)], 2)

    def test_remove_from_bag(self):
        # Post request to remove the product
        response = self.client.post(self.url_remove_from_bag)

        # Get the messages from the response
        messages = list(get_messages(response.wsgi_request))
        
        # Ensure only 1 message and it's the correct one
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Removed Test Guitar from your bag')  # Correct message for removal

        # Verify the status code (200 is expected after removal)
        self.assertEqual(response.status_code, 200)

        # Verify the item is removed from the session bag
        self.assertNotIn(str(self.product.id), self.client.session['bag'])

class BagViewsTestAddToBag(TestCase):
    def setUp(self):
        # Set up your test product and session
        self.client.session.clear()
        self.product = Product.objects.create(name="Test Guitar", price=200)
        self.url_add_to_bag = reverse('add_to_bag', args=[self.product.id])

    def test_add_to_bag_valid_quantity(self):
        # Test adding an item with valid quantity
        response = self.client.post(self.url_add_to_bag, {'quantity': 2})
        messages = list(get_messages(response.wsgi_request))

        # Check if the success message is returned
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Added {self.product.name} to your bag')
        self.assertEqual(response.status_code, 302)  # Redirect after adding to the bag

        # Check if the product was added with correct quantity
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product.id)], 2)

    def test_add_to_bag_quantity_above_99(self):
        # Test adding an item with quantity greater than 99
        response = self.client.post(self.url_add_to_bag, {'quantity': 150})
        messages = list(get_messages(response.wsgi_request))

        # Expect error message
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Please stop trying to break my site!')
        self.assertEqual(response.status_code, 302)

        # Check if quantity is capped at 99
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product.id)], 99)

    def test_add_to_bag_quantity_below_1(self):
        # Test adding an item with quantity less than 1
        response = self.client.post(self.url_add_to_bag, {'quantity': 0})
        messages = list(get_messages(response.wsgi_request))
        
        # Expect error message
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Please stop trying to break my site!')
        self.assertEqual(response.status_code, 302)

        # Check if quantity is set to 1
        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product.id)], 1)