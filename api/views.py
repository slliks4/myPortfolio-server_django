# Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def EndPoints(request):
    endpoints = {
        'categories -GET':'/categories',
        'blogs -GET':'/blogs',
        'blog_detail -GET':'/blog_detail/<str:pk>',
        'projects -GET':'/projects',
        'project_detail -GET':'/project_detail/<str:pk>',
        'profile -GET': '/profile/user_name',
        'comments -POST': '/comments/',
        'feedback -POST' : '/feedback/'
    }
    return Response(endpoints)