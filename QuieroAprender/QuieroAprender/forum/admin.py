from django.contrib import admin

from QuieroAprender.forum.models import Comment, ForumPost


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "content", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(Comment)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["post__title"]
