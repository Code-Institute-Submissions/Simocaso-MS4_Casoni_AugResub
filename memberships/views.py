from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Membership

# Create your views here.


def all_memberships(request):
    """ A view to show all the memberships plans"""

    memberships = Membership.objects.all()
    query = None

    # Code used from Boutique Ado - CI Lesson

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search request")
                return redirect(reverse('memberships'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
                )
            memberships = memberships.filter(queries)

    context = {
        'memberships': memberships,
        'search_term': query,
    }

    return render(request, 'memberships/memberships.html', context)


def membership_detail(request, membership_id):
    """ A view to show the membership detail"""

    membership = get_object_or_404(Membership, pk=membership_id)

    context = {
        'membership': membership,
    }

    return render(request, 'memberships/membership_detail.html', context)
