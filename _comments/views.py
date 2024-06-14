from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CommentSerializers, Comments
from _blogs.models import Blogs

# Create your views here.
@api_view(['GET'])
def getComments(request, blog_id) -> Response:
    blog = get_object_or_404(Blogs, id=blog_id)
    
    comments = Comments.objects.filter(blog=blog)
    serializer = CommentSerializers(comments, many=True)

    return Response(
        {'message': 'success', 'data': serializer.data},
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
def postComments(request, blog_id) -> Response:
    blog = get_object_or_404(Blogs, id=blog_id)

    serializer = CommentSerializers(data=request.data)

    if serializer.is_valid():
        # save request data
        serializer.save(blog=blog)

        return Response(
            {'message': 'success', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)