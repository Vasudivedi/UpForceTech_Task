from rest_framework import status
from rest_framework.response import Response
from django.http import Http404 
from .models import *
from .serializer import PostsSerializer,UserSerializer,LikesSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_task(pk)
        print(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self.get_task(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        user = self.get_task(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = self.get_task(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_task(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404



class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        # data = request.body
        # json_data = data.decode('utf-8')
        # parsed_data = json.loads(json_data)
        # pub_status = parsed_data['status']
        # print("status",pub_status)
        # if pub_status == "public":
        posts = Posts.objects.filter(status='public')
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)
        # return Response(
        #     {'message': "you do not have permission to do this action"},
        #     status=status.HTTP_403_FORBIDDEN)
        
    def create(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        posts = self.get_task(pk)
        serializer = PostsSerializer(posts)
        return Response(serializer.data)

    def update(self, request, pk=None):
        posts = self.get_task(pk)
        print('task',posts)
        if request.user != posts.created_by:
            return Response(
            {'message': "you do not have permission to do this action"},
            status=status.HTTP_403_FORBIDDEN)
        serializer = PostsSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        posts = self.get_task(pk)
        print('task',posts.created_by)
        if request.user != posts.created_by:
            return Response(
            {'message': "you do not have permission to do this action"},
            status=status.HTTP_403_FORBIDDEN)
        serializer = PostsSerializer(posts, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        posts = self.get_task(pk)
        if request.user != posts.created_by:
            return Response(
            {'message': "you do not have permission to do this action"},
            status=status.HTTP_403_FORBIDDEN)
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_task(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404
        
class LikeViewSet(viewsets.ViewSet):
    def list(self, request):
        like = Likes.objects.all()
        serializer = LikesSerializer(like, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        like = self.get_task(pk)
        print(like)
        serializer = LikesSerializer(like)
        return Response(serializer.data)

    def update(self, request, pk=None):
        like = self.get_task(pk)
        serializer = LikesSerializer(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        like = self.get_task(pk)
        serializer = LikesSerializer(like, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        like = self.get_task(pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_task(self, pk):
        try:
            return Likes.objects.get(pk=pk)
        except Likes.DoesNotExist:
            raise Http404

        
        