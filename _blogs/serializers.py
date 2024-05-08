from rest_framework import serializers
from .models import Blogs

# Serializers
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"
        depth =1