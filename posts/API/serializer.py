from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'slug', 'order', 'created_date', 'modified_date']
        # fields = '__all__'
