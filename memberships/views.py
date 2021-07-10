from django.shortcuts import get_object_or_404, render
from .models import Membership

# Create your views here.


def all_memberships(request):
    """ A view to show all the memberships plans"""

    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'memberships/memberships.html', context)


def memberships_detail(request, membership_id):
    """ A view to show the membership detail"""

    memberships = get_object_or_404(Membership, pk=membership_id)

    context = {
        'memberships': memberships,
    }

    return render(request, 'memberships/memberships_detail.html', context)
