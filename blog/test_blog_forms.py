
from django.test import TestCase
from .models import Author, BlogPost
from django.urls import reverse

class TestModels(TestCase):
   ''' def setUp(self):
        # Create a category instance
        self.category = Category.objects.create(name='Guitars', friendly_name='Electric Guitars')
        
        # Create a product instance
        self.product = Product.objects.create(
            category=self.category,
            name='Fender Stratocaster',
            description='A great guitar.',
            price=999.99,
            in_stock=True
        )
    
    def test_category_str_method(self):
        # Check if the Category's __str__ method returns the correct name
        self.assertEqual(str(self.category), 'Guitars')
    
    def test_product_str_method(self):
        # Check if the Product's __str__ method returns the correct name
        self.assertEqual(str(self.product), 'Fender Stratocaster')'''