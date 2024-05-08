# Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer, Blogs
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def getBlogs(request):
    try:
        query = request.GET.get('query','')

        blogs = Blogs.objects.filter(
            Q(title__icontains = query) | 
            Q(categories__name__icontains = query) |
            Q(text__icontains = query)
        ).distinct()

        serializer = BlogSerializer(blogs, many = True)

        return Response(
            {'message':'blogs','data':serializer.data}, 
            status=200
        )
    except Exception as error:
        return Response({'message':str(error)}, status=400)
    
    
@api_view(['GET'])
def getBlogDetail(request, id):
    try:
        blog_detail = Blogs.objects.get(id=id)
        serializer = BlogSerializer(blog_detail, many = False)

        return Response(
            {'message':'blog_detail','data':serializer.data}, 
            status=200
        )
    except Exception as error:
        return Response({'message':str(error)}, status=400)