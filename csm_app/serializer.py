from rest_framework import serializers
from .models import User,Posts,Likes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = '__all__'
      
    def get_likes_count(self, obj):
            return obj.post_post.count()
           
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
