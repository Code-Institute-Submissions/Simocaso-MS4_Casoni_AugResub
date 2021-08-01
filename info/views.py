from django.shortcuts import render

# Create your views here.


def info(request):
    """ a view to return the info page """

    return render(request, 'info/info.html')
