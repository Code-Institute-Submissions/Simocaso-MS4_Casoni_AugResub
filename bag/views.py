from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ a view to see the products in the bag """
    return render(request, 'bag/bag.html')


def add_item(request, product_id):
    """ add products to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
