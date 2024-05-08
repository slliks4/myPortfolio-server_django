from rest_framework import serializers
from .models import Categories


# Serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
