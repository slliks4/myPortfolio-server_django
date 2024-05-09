# Imports
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile
from .serializers import ProfileSerializer
 
# Create your views here.

@api_view(['GET'])
def getProfile(request, user_name):
    try:
        profile = get_object_or_404(
            Profile.objects.prefetch_related(
                'email',
                'tel',
                'experience',
                'education',
                'services'
            ),
            user_name = user_name
        )
        
        serializer = ProfileSerializer(profile, many=False)

        return Response({
            'message': 'Profile loaded successfully',
            'data': serializer.data
        }, status=200)
    except Exception as error:
        return Response({'message':str(error)}, status=400)
