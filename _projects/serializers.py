from rest_framework import serializers
from .models import Projects

# Serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        depth =1