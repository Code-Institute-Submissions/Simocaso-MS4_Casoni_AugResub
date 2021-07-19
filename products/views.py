from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product

# Create your views here.


def product_detail(request, product_id):
    """ A view to show the product detail"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products_detail.html', context)
