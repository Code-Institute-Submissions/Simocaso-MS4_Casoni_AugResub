from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ a view to see the products in the bag """
    return render(request, 'bag/bag.html')


def add_item(request, product_id):
    """ add products to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['products_by_size'][size].keys():
                bag[product_id]['products_by_size'][size] += quantity
            else:
                bag[product_id]['products_by_size'][size] = quantity
        else:
            bag[product_id] = {'products_by_size': {size: quantity}}
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
        else:
            bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
