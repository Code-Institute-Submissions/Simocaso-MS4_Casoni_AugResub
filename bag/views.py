from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ a view to see the products in the bag """

    return render(request, 'bag/bag.html')


def add_item(request, product_id):
    """ add products to the bag """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['products_by_size'].keys():
                bag[product_id]['products_by_size'][size] += quantity
                messages.success(
                    request, f'Size {size.upper()} quantity updated!'
                )
            else:
                bag[product_id]['products_by_size'][size] = quantity
                messages.success(
                    request, f'{product.name} {size.upper()} size added to your bag!'
                )
        else:
            bag[product_id] = {'products_by_size': {size: quantity}}
            messages.success(
                request, f'{product.name} {size.upper()} size added to your bag!'
            )
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
            messages.success(request, f'Updated {product.name} qty!')
        else:
            bag[product_id] = quantity
            messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, product_id):
    """ adjust the products' quantities in the bag """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[product_id]['products_by_size'][size] = quantity
            messages.success(
                request, f'{size.upper()} size qty updated!'
            )
        else:
            del bag[product_id]['products_by_size'][size]
            if not bag[product_id]['products_by_size']:
                bag.pop(product_id)
            messages.success(
                request, f'{product.name} {size.upper()} removed!'
            )
    else:
        if quantity > 0:
            bag[product_id] = quantity
            messages.success(
                request, f'{product.name} qty updated!'
            )
        else:
            bag.pop(product_id)
            messages.success(
                request, f'Removed {product.name} from your bag!'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, product_id):
    """ remove product from the bag directly """

    try:
        product = get_object_or_404(Product, pk=product_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[product_id]['products_by_size'][size]
            if not bag[product_id]['products_by_size']:
                bag.pop(product_id)
            messages.success(
                request, f'{product.name} {size.upper()} removed!'
            )
        else:
            bag.pop(product_id)
            messages.success(
                request, f'Removed {product.name} from your bag!'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing product: {e}')
        return HttpResponse(status=500)
