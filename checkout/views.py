from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# taken from CI checkout module


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['final_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JLmsBKRksOaxPKiZSRjY0bY5wST3uiqIum1wlTCCr6CkWzsPMCUkgacbzbS7Qc7k8DsG4Gc4EpfUGGxpSXv4NxJ00MMqH73q0',
        'client_secret': 'test test',
    }

    return render(request, template, context)
