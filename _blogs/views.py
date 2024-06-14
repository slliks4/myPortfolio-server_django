# Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer, Blogs
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def getBlogs(request):
    try:
        limit = int(request.GET.get('limit', 6))
        skip = int(request.GET.get('skip', 0))
        query = request.GET.get('query')
        category = request.GET.get('category')

        filters = Q()

        if category:
            filters &= Q(categories__name=category)
        if query:
            filters &= Q(title__icontains=query) | Q(text__icontains=query)

        data = Blogs.objects.filter(filters).distinct()
        blogs = data[skip:skip+limit]

        serializer = BlogSerializer(blogs, many = True)

        return Response(
            {'message':'blogs','data':serializer.data}, 
            status=200
        )
    except Exception as error:
        return Response({'message':str(error)}, status=400)
    
    
@api_view(['GET'])
def getBlog(request, id):
    try:
        blog_detail = Blogs.objects.get(id=id)
        serializer = BlogSerializer(blog_detail, many=False)
        return Response({'message': 'blog_detail', 'data': serializer.data}, status=200)
    except Blogs.DoesNotExist:
        return Response({'message': 'Blog not found'}, status=404)
    except Exception as error:
        return Response({'message': str(error)}, status=500)