from rest_framework import serializers
from .models import FeedBack

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['full_name', 'email', 'subject', 'message']