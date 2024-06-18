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
        page = int(request.GET.get('page', 1))
        query = request.GET.get('query')
        category = request.GET.get('category')

        filters = Q()

        if category:
            filters &= Q(categories__name=category)
        if query:
            filters &= Q(title__icontains=query) | Q(text__icontains=query)

        data = Blogs.objects.filter(filters).distinct()
        total = data.count()

        # Ensure limit is at least 1
        limit = max(limit, 1)

        # Calculate the starting and ending indices for slicing the queryset
        start = (page - 1) * limit
        end = start + limit

        # Prevent pagination limit exceeding the total number of projects
        if start >= total:
            return Response({'message': 'Pagination limit exceeded'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the projects for the current page
        blogs = data[start:end]

        serializer = BlogSerializer(blogs, many = True)

        # Calculate total number of pages
        total_pages = (total + limit - 1) // limit  # Ceiling division for total pages
        
        # TODO: Implement Pagination and include in response
        response = {
            'message': 'success',
            'data': serializer.data,
            'currentPage': page,
            'nextPage': page + 1 if page * limit < total else None,
            'totalPages': total_pages,
            'totalData': total,
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