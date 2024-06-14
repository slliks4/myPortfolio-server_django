# Imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def EndPoints(request):
    endpoints = {
        'categories -GET':'/getCategories',
        'blogs -GET params(limit:6, skip:0, category, query)':'/getBlogs',
        'blog_detail -GET':'/getBlog/<str:pk>',
        'projects -GET params(limit:6, skip:0, category, query)':'/projects',
        'project_detail -GET':'/getProject/<str:pk>',
        'profile -GET': '/getProfile/user_name',
        'comments -POST': '/getComments/<int:blog_id>',
        'comments -POST': '/postComment/',
        'feedback -POST' : '/postFeedback/'
    }
    return Response(endpoints)