from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.API.serializer import PostSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.API.permisions import IsAdminOrReadyOnly


# GET - POST 'Simple'
# class PostApiView(APIView):
#     def get(self, request):
#         # posts = Post.objects.all()
#         posts = [post.title for post in Post.objects.all()]
#         return Response(status=status.HTTP_200_OK, data=posts)
#
#     def post(self, request):
#         Post.objects.create(title=request.POST['title'], content=request.POST['content'], slug=request.POST['slug'],
#         order=request.POST['order'])
#         return self.get(request)


# GET - POST + Seralizer
# class PostApiView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)


# Clases con ViewSet
# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     def retrieve(self, request, pk: int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)
#
#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     def update(self, request, pk: int):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#     def destroy(self, request, pk: int):
#         try:
#             post = Post.objects.get(pk=pk)
#             post.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# En Django Rest Framework (DRF), ModelViewSet es una clase de vista genérica que se utiliza comúnmente
# para crear vistas basadas en modelos en una API web
class PostModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminOrReadyOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

