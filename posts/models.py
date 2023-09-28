from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, null=False)
    content = models.TextField(verbose_name="Contenido")
    slug = models.SlugField(max_length=200, unique=True, null=False)
    order = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'posts'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

