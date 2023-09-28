from django.contrib import admin
from posts.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'modified_date', 'created_date')
    prepopulated_fields = {'slug': ['title']}
    list_display_links = ('title', 'slug')
    list_filter = ('title', 'slug')
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('-created_date',)


admin.site.register(Post, PostAdmin)

