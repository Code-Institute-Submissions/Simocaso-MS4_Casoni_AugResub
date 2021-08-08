from django.shortcuts import render
from .models import Info
from django.contrib import messages

# Create your views here.


def info(request):
    """ a view to return the info page """
    if request.method == 'POST':
        info = Info()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        info.name = name
        info.email = email
        info.subject = subject
        info.message = message
        info.save()
        messages.success(request, 'Thank you for your message!')

    return render(request, 'info/info.html')
