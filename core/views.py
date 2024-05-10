from django.shortcuts import redirect
from django.contrib.auth import logout

def Logout(request):
    logout(request)
    return redirect('index')