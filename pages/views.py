from django.shortcuts import render
from django.core.exceptions import PermissionDenied
# Create your views here.

def IndexPage(request):
    if (
        request.user.is_authenticated and
        request.user.is_staff
    ):
        context = {
        }

        return render (request, 'index.html', context)
    
    else:
        raise PermissionDenied('sorry you are not permitted to view this page')