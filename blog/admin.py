from django.contrib import admin
from blog.models import Post

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     model = Post
#     list_display = ["title", "content", "status"]

class PostForm(SummernoteModelAdmin):
    list_display = ["title", "created_at", "updated_at", "status", "author"]
    summernote_fields = ('content',)
    serach_fields = ("title", "content")

    class Meta:
        ordering = ['-created_at']


admin.site.register(Post, PostForm)