from django.urls import path,include
from .views import PostViewSet,UserViewSet,LikeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'user', UserViewSet, basename='user')
router.register(r'likes', LikeViewSet, basename='like')



urlpatterns = [
    path('api/', include(router.urls)),
]