from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_products = []
    total = 0
    product_count = 0
    delivery = 9.99
    bag = request.session.get('bag', {})

    for product_id, product_data in bag.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += product_data * product.price
            product_count += product_data
            bag_products.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, quantity in product_data['products_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_products.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    final_total = delivery + float(total)

    context = {
        'bag_products': bag_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'final_total': final_total,
    }

    return context
