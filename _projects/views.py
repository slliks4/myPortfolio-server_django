# Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, Projects
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def getProjects(request):
    try:
        query = request.GET.get('query','')

        projects = Projects.objects.filter(
            Q(title__icontains = query) | 
            Q(categories__name__icontains = query) |
            Q(text__icontains = query)
        ).distinct()

        serializer = ProjectSerializer(projects, many = True)

        return Response(
            {'message':'projects','data':serializer.data}, 
            status=200
        )
    except Exception as error:
        return Response({'message':str(error)}, status=400)
    
    
@api_view(['GET'])
def getProjectDetail(request, id):
    try:
        project_detail = Projects.objects.get(id=id)
        serializer = ProjectSerializer(project_detail, many = False)

        return Response(
            {'message':'project_detail','data':serializer.data}, 
            status=200
        )
    except Exception as error:
        return Response({'message':str(error)}, status=400)