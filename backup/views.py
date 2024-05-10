from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def BackupBlogs(request):
    messages.info(request, 'Blogs Backed up successfully')
    return redirect('index')

def BackupFeedBack(request):
    messages.info(request, 'FeedBack Backed up successfully')
    return redirect('index')

def BackupProfile(request):
    messages.info(request, 'Profile Backed up successfully')
    return redirect('index')

def BackupProjects(request):
    messages.info(request, 'Projects Backed up successfully')
    return redirect('index')
