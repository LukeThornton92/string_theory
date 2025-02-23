
from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class AllProductsViewTest(TestCase):
    
    def setUp(self):
        # Create categories for testing
        self.electric_category = Category.objects.create(name="electric_guitars", friendly_name="Electric Guitars")
        self.acoustic_category = Category.objects.create(name="acoustic_guitars", friendly_name="Acoustic Guitars")
        self.accessories_category = Category.objects.create(name="accessories", friendly_name="Accessories")

        # Create products for testing
        self.product1 = Product.objects.create(
            category=self.electric_category,
            name="Fender Stratocaster",
            description="A popular electric guitar",
            price=999.99,
            sku="12345",
            brand="Fender"
        )
        self.product2 = Product.objects.create(
            category=self.electric_category,
            name="Gibson Les Paul",
            description="A classic electric guitar",
            price=1199.99,
            sku="67890",
            brand="Gibson"
        )
        
        self.product3 = Product.objects.create(
            category=self.acoustic_category,
            name="Yamaha FG800",
            description="A great acoustic guitar for beginners",
            price=199.99,
            sku="11223",
            brand="Yamaha"
        )
        self.product4 = Product.objects.create(
            category=self.acoustic_category,
            name="Martin D-28",
            description="A premium acoustic guitar",
            price=2999.99,
            sku="44556",
            brand="Martin"
        )

        self.product5 = Product.objects.create(
            category=self.accessories_category,
            name="Guitar Pedal",
            description="A pedal for electric guitars",
            price=129.99,
            sku="13579",
            brand="Boss"
        )
        self.product6 = Product.objects.create(
            category=self.accessories_category,
            name="Tuner Pedal",
            description="A tuning pedal for guitars",
            price=89.99,
            sku="24680",
            brand="Boss"
        )

        # The URL for the products page (replace 'products' with the correct name if needed)
        self.url = reverse('products')

    def test_all_products_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product2.name)

    def test_search_filter(self):
        response = self.client.get(self.url, {'q': 'Fender'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertNotContains(response, self.product2.name)
    
    def test_blanksearch_filter(self):
        response = self.client.get(self.url, {'q': ''})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products'))

    def test_category_filter_category(self):
        response = self.client.get(self.url, {'category': 'electric_guitars'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'electric_guitars')
    
    def test_category_filter_brand(self):
        response = self.client.get(self.url, {'category': 'acoustic_guitars', 'brand': 'gibson'})
        self.assertEqual(response.status_code, 200)
        # different way to test!
        # Get the filtered products from the database
        filtered_products = Product.objects.filter(category__name='acoustic_guitars', brand='gibson')
        # Ensure each filtered product's name is present in the response
        for product in filtered_products:
            self.assertContains(response, product.name)
    
    def test_category_filter_description(self):
        response = self.client.get(self.url, {'category': 'accessories', 'description': 'pedal'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'accessories')
        self.assertContains(response, 'pedal')

    def test_sorting(self):
        # Sort by 'name' in ascending order
        response = self.client.get(self.url, {'sort': 'name', 'direction': 'asc'})
        self.assertEqual(response.status_code, 200)
        # Get the list of product names from the response
        product_names = [product.name for product in response.context['products']]
        # Sort the product names manually to compare
        expected_product_names = sorted(product_names)
        # Assert that the product names from the response are in the correct order
        self.assertEqual(product_names, expected_product_names)
        # Sort by 'name' in descending order
        response = self.client.get(self.url, {'sort': 'name', 'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        # Get the list of product names from the response
        product_names_desc = [product.name for product in response.context['products']]
        # Sort the product names manually in descending order
        expected_product_names_desc = sorted(product_names, reverse=True)
        # Assert that the product names from the response are in the correct order
        self.assertEqual(product_names_desc, expected_product_names_desc)
    
    def test_sorting_by_category(self):
        # Sort products by 'category' in ascending order
        response = self.client.get(self.url, {'sort': 'category', 'direction': 'asc'})
        self.assertEqual(response.status_code, 200)
        
        # Get the list of product objects from the response
        products = response.context['products']
        
        # Manually sort the products based on category
        expected_products = sorted(products, key=lambda x: x.category.name)
        
        # Assert that the products from the response are sorted correctly by category
        self.assertEqual(list(products), expected_products)
        
        # Sort products by 'category' in descending order
        response = self.client.get(self.url, {'sort': 'category', 'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        
        # Get the list of product objects from the response in descending order
        products_desc = response.context['products']
        
        # Manually sort the products in descending order based on category
        expected_products_desc = sorted(products, key=lambda x: x.category.name, reverse=True)
        
        # Assert that the products from the response are sorted correctly in descending order by category
        self.assertEqual(list(products_desc), expected_products_desc)
    
class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Guitar", friendly_name="Electric Guitars")
        self.product1 = Product.objects.create(
            category=self.category,
            name="Fender Stratocaster",
            description="A popular electric guitar",
            price=999.99,
            sku="12345"
        )
        self.product2 = Product.objects.create(
            category=self.category,
            name="Gibson Les Paul",

            description="A classic rock guitar",
            price=1199.99,
            sku="67890"
        )
        self.url = reverse('product_detail', args=[self.product1.id])

    def test_product_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.product1.description)

    def test_recommended_products(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.product2.name)  # Should recommend other products from the same category

class AddProductViewTest(TestCase):
    
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin', password='testpass')
        self.category = Category.objects.create(name="electric_guitars", friendly_name="Electric Guitars")
        self.url = reverse('add_product')
    
    def test_add_product_view_for_superuser(self):
        self.client.login(username='admin', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_add_product_view_for_non_superuser(self):
        user = User.objects.create_user(username='user', password='testpass')
        self.client.login(username='user', password='testpass')
        response = self.client.get(self.url)
        # Use `get_messages` to check if the message is included
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Sorry, only store owners are allowed to do that!")

    def test_add_product_submission(self):
        # Create a superuser for testing
        user = User.objects.create_superuser(username='superuser', password='testpass')
        self.client.login(username='superuser', password='testpass')

        # Send a POST request to add the product
        response = self.client.post(reverse('add_product'), {
            'name': 'Test Product',
            'description': 'A great product',
            'price': '20.99'
        })

        # Fetch the product that should have been created
        product = Product.objects.filter(name='Test Product').first()
        # Check if the response redirects to the product detail page
        self.assertRedirects(response, reverse('product_detail', args=[product.id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Successfully added product!")

    def test_add_product_submission_fail(self):
        # Create a superuser for testing
        user = User.objects.create_superuser(username='superuser', password='testpass')
        self.client.login(username='superuser', password='testpass')

        # Send a POST request to add the product
        response = self.client.post(reverse('add_product'), {
            'name': 'Test Product',
            'description': 'A great product',
            'price': ''
        })

        # Fetch the product that should have been created
        product = Product.objects.filter(name='Test Product').first()
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Failed to add product, please ensure for is valid")

class EditProductViewTest(TestCase):
    
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin', password='testpass')
        self.category = Category.objects.create(name="electric_guitars", friendly_name="Electric Guitars")
        self.product = Product.objects.create(
            category=self.category,
            name="Fender Stratocaster",
            description="A popular electric guitar",
            price=999.99,
            sku="12345"
        )
        self.url = reverse('edit_product', args=[self.product.id])

    def test_edit_product_view_for_superuser(self):
        self.client.login(username='admin', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_edit_product_view_for_non_superuser(self):
        user = User.objects.create_user(username='user', password='testpass')
        self.client.login(username='user', password='testpass')
        # Create a product to edit
        product = Product.objects.create(name='Test Product', price=100.00, description='Test Description')
        edit_url = reverse('edit_product', args=[product.id])
        response = self.client.get(edit_url)
        messages = list(get_messages(response.wsgi_request))
        # Check if the correct permission error message is in the response
        self.assertEqual(str(messages[0]), "Sorry, only store owners are allowed to do that!")

    def test_edit_product_submission(self):
        user = User.objects.create_superuser(username='superuser', password='testpass')
        self.client.login(username='superuser', password='testpass')

        # Create a product to edit
        product = Product.objects.create(name='Old Product', description='Old Description', price=10.99)

        # Send a POST request to edit the product
        response = self.client.post(reverse('edit_product', args=[product.id]), {
            'name': 'Updated Product',
            'description': 'Updated Description',
            'price': '12.99'
        })

        # Check that the response redirects to the product detail page
        self.assertRedirects(response, reverse('product_detail', args=[product.id]))

    def test_edit_product_submission_fail(self):
        user = User.objects.create_superuser(username='superuser', password='testpass')
        self.client.login(username='superuser', password='testpass')

        # Create a product to edit
        product = Product.objects.create(name='Old Product1', description='Old Description1', price=10.99)

        # Send a POST request to edit the product
        response = self.client.post(reverse('edit_product', args=[product.id]), {
            'name': 'Updated Product1',
            'description': 'Updated Description1',
            'price': 'uh-oh'
        })

        product = Product.objects.filter(name='Test Product').first()
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Failed to edit product, please ensure for is valid")

class DeleteProductViewTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin', password='testpass')
        self.category = Category.objects.create(name="electric_guitars", friendly_name="Electric Guitars")
        self.product = Product.objects.create(
            category=self.category,
            name="Fender Stratocaster",
            description="A popular electric guitar",
            price=999.99,
            sku="12345"
        )
        self.url = reverse('delete_product', args=[self.product.id])

    def test_delete_product_view_for_superuser(self):
        user = User.objects.create_superuser(username='superuser', password='testpass')
        self.client.login(username='superuser', password='testpass')

        # Create a product for deletion
        product = Product.objects.create(name='Test Product', description='Description', price=10.99)

        # Send a POST request to delete the product
        response = self.client.post(reverse('delete_product', args=[product.id]))

        # Check that the response redirects (expected 302 status code)
        self.assertRedirects(response, reverse('products'))

    def test_delete_product_view_for_non_superuser(self):
        # Create a non-superuser user
        user = User.objects.create_user(username='user', password='testpass')
        # Log the user in
        self.client.login(username='user', password='testpass')
        # Create a product
        product = Product.objects.create(
            name='Test Product',
            category=self.category,  # Assuming self.category is set up in setUp()
            price=10.99,
        )
        # Define the delete URL for the created product
        delete_url = reverse('delete_product', kwargs={'product_id': product.id})
        # Make the GET request to delete the product
        response = self.client.get(delete_url)
        # Get the messages from the response
        messages = list(get_messages(response.wsgi_request))
        # Assert that the correct message is displayed
        self.assertEqual(str(messages[0]), "Sorry, only store owners are allowed to do that!")

    def test_delete_product(self):
        self.client.login(username='admin', password='testpass')
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('products'))
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())