from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from datetime import date, timedelta

# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            brand = request.GET.get('brand')
            description = request.GET.get('description')
            if categories:
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)
            if brand:
                products = products.filter(brand__iexact=brand)
            if description:
                products = products.filter(description__icontains=description)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }


    return render(request, 'products/product_detail.html', context)

def estimated_shipping(request):
    """Calculates estimated shipping date, 7 business days"""
    today = date.today()
    days_to_add = 7
    estimated_date = today + timedelta(days=days_to_add)