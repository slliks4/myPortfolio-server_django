from rest_framework import serializers
from .models import *
from _links.models import Links

class MissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mission
        fields = '__all__'

class VisionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vision
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Email
        fields = '__all__'

class TelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tel
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Experience
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Services
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Links
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    email = EmailSerializer(many=True, read_only = True)
    tel = TelSerializer(many=True, read_only = True)
    education = EducationSerializer(many=True, read_only = True)
    experience = ExperienceSerializer(many=True, read_only = True)
    services = ServicesSerializer(many=True, read_only = True)
    links = LinkSerializer(many=True, read_only =True)
    mission = MissionSerializer(many=False, read_only = True)
    vision = VisionSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'