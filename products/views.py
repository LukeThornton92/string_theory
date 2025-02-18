from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from random import sample
from django.db.models.functions import Lower
from .forms import ProductForm
# Create your views here.

def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products= products.order_by(sortkey)


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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A view to show individual product details, also produces a random filtered selection of other products you may like"""

    product = get_object_or_404(Product, pk=product_id)
    product_category = product.category  # Uses pk to get product category
    product_brand = product.brand  # Uses pk to get product brand

    recommended_products = Product.objects.filter(category=product_category, brand=product_brand).exclude(id=product_id).order_by('?')  # Filters through all products for ideal recommendations
    

    context = {
        'product': product,
        'recommended_products': recommended_products,
    }


    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """Add a product to the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to do that!')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args = [product.id]))
        else:
            messages.error(request, 'Failed to add product, please ensure for is valid')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form' : form
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk = product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited product!')
            return redirect(reverse('product_detail', args = [product.id]))
        else:
            messages.error(request, 'Failed to edit product, please ensure for is valid')
    else:
        form = ProductForm(instance = product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form' : form,
        'product' : product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Deletes a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners are allowed to do that!')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk = product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
