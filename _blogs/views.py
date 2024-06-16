# Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer, Blogs
from django.db.models import Q
from rest_framework import status

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
        total = len(data)

        # Ensure limit is at least 1
        limit = max(limit, 1)

        # Prevent pagination limit exceeding the total number of projects
        if skip >= total:
            return Response({'message': 'Pagination limit exceeded'}, status=status.HTTP_400_BAD_REQUEST)

        # Adjust the limit to avoid IndexError
        end_index = min(skip + limit, total)

        blogs = data[skip:end_index]

        serializer = BlogSerializer(blogs, many = True)
        
        # TODO: Implement Pagination and include in response
        response = {
            'message': 'success',
            'data': serializer.data,
            'total': total
        }
        return Response(response, status=status.HTTP_200_OK)
    except Exception as error:
        error_message = str(error)
        if len(error_message) > 30:
            error_message = error_message[:30]
        return Response({'message': error_message}, status=status.HTTP_400_BAD_REQUEST)
    
    
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