from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post


class PostApiView(APIView):
    def get(self, request):
        # posts = Post.objects.all()
        posts = [post.title for post in Post.objects.all()]
        return Response(status=status.HTTP_200_OK, data=posts)

    def post(self, request):
        Post.objects.create(title=request.POST['title'], content=request.POST['content'],
            slug=request.POST['slug'], order=request.POST['order'])
        return self.get(request)
