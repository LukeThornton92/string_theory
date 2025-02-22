from django.test import TestCase
from ..forms import OrderForm

class CheckoutOrderFormTest(TestCase):
    def test_valid_form(self):
        ''' Checks to see if the form is valid when fields are populated'''
        form_data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 4',
            'town_or_city': 'Springfield',
            'postcode': '12345',
            'country': 'US',
            'county': 'Some County',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_form_missing_fields(self):
        ''' Populated form with no data, checks to see if fullname, 
        email, phone number ans street address fail '''
        form_data = {}
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)
        self.assertIn('street_address1', form.errors)
    
    def test_invalid_email_format(self):
        ''' Inputs incorrect email, checks its False '''
        form_data = {
            'full_name': 'John Doe',
            'email': 'invalid-email',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'town_or_city': 'Springfield',
            'postcode': '12345',
            'country': 'US',
            'county': 'Some County',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    def test_optional_fields(self):
        ''' Checks to see if Null=True fields do not cause errors when blank'''
        form_data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'town_or_city': 'Springfield',
            'postcode': '12345',
            'country': 'US',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
