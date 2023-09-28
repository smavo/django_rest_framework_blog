from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.API.serializer import PostSerializer
from rest_framework.viewsets import ViewSet

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


class PostViewSet(ViewSet):
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)

    def create(self, request):
        serializer = PostSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
