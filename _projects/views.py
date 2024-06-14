# Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, Projects
from django.db.models import Q
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getProjects(request):
    try:
        limit = int(request.GET.get('limit', 6))
        skip = int(request.GET.get('skip', 0))
        is_lab = request.GET.get('is_lab')
        category = request.GET.get('category')

        filters = Q()

        if category:
            filters &= Q(categories__name=category)
        if is_lab is not None:
            filters &= Q(is_lab=is_lab.lower() == 'true')

        data = Projects.objects.filter(filters).distinct()
        projects = data[skip:skip+limit]

        serializer = ProjectSerializer(projects, many = True)

        return Response(
            {'message': 'projects', 'data': serializer.data}, 
            status=status.HTTP_200_OK
        )
    except Exception as error:
        error_message = str(error)
        if len(error_message) > 30:
            error_message = error_message[:30]
        return Response({'message': error_message}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def getProject(request, id):
    try:
        project_detail = Projects.objects.get(id=id)
        serializer = ProjectSerializer(project_detail, many = False)

        return Response(
            {'message':'project_detail','data':serializer.data}, 
            status=200
        )
    except Exception as error:
        return Response({'message':str(error)}, status=400)