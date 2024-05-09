# Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Categories, CategorySerializer

# Create your views here.

@api_view(['GET']) 
def getCategories(request):
    try:
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many = True)

        return Response(
            serializer.data,
            status=200
        )
    except Exception as error:
        return Response ({ 'Error': str(error) }, status=400)