from rest_framework import serializers
from .models import User,Posts,Likes


class UserSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=30)
    # email =  serializers.EmailField()
    user_id = serializers.CharField(read_only= True)
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password':{'write_only': True }}        

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
