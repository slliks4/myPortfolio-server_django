# Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def EndPoints(request):
    endpoints = {
        'categories':'/categories',
        'blogs':'/blogs',
        'blog_detail':'/blog_detail/<str:pk>/',
        'projects':'/projects',
        'project_detail':'/project_detail/<str:pk>/',
    }
    return Response(endpoints)