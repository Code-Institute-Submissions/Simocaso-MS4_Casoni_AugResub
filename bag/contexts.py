

def bag_contents(request):

    bag_products = []
    total = 0
    product_count = 0
    delivery = 9.99

    context = {
        'bag_products': bag_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
    }

    return context
