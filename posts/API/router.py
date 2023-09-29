from rest_framework.routers import DefaultRouter
from posts.API.views import PostModelViewSet  # PostViewSet,PostModelViewSet

router_post = DefaultRouter()
# router_post.register(prefix='posts', basename='posts', viewset=PostViewSet)
router_post.register(prefix='posts', basename='posts', viewset=PostModelViewSet)


