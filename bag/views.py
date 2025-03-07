from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.messages import get_messages

from products.models import Product


def view_bag(request):
    """A view that renders the bad contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specific product to the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))

    # Define the session bag first
    bag = request.session.get('bag', {})

    # Prevent adding more than 99 or less than 1
    if quantity > 99:
        messages.error(request, 'Please stop trying to break my site!')
        quantity = 99
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)
        bag[item_id] = quantity
        request.session['bag'] = bag
        redirect_url = request.POST.get('redirect_url', '/')
        return redirect(redirect_url)
    elif quantity < 1:
        messages.error(request, 'Please stop trying to break my site!')
        quantity = 1
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)
        bag[item_id] = quantity
        request.session['bag'] = bag
        redirect_url = request.POST.get('redirect_url', '/')
        return redirect(redirect_url)
    else:
        if item_id in bag:  # Check if item already in the bag
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} to {bag[item_id]}'
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # Save the updated bag back to the session
    request.session['bag'] = bag

    # Redirect back to the given URL or fallback
    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specific product in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))

    bag = request.session.get('bag', {})

    # If statement to stop someone from ordering more than 99 or less than 1
    if quantity > 99:
        messages.error(request, 'Please stop trying to break my site!')
        quantity = 99
        # Directly update the bag and redirect without continuing
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)
        bag[item_id] = quantity
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    elif quantity < 1:
        messages.error(request, 'Please stop trying to break my site!')
        quantity = 1
        # Directly update the bag and redirect without continuing
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)
        bag[item_id] = quantity
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} to {bag[item_id]}'
            )
        else:
            bag.pop(item_id, None)
            messages.success(request, f'Removed {product.name} from your bag')

    # Save the updated bag to the session
    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Removes the specific product from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)

    bag = request.session.get('bag', {})
    try:
        # Remove the item from the bag
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')


        # Save the updated bag to the session
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
