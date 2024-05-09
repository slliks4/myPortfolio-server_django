from rest_framework import serializers
from .models import Blogs
from _comments.serializers import CommentSerializers

# Serializers
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Blogs
        fields = "__all__"
        depth =1

    def get_comment_count(self,obj):
        count = obj.comments.count()
        return count