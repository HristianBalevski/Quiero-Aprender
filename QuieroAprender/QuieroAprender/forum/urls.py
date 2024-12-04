from django.urls import path

from .views import (
    CommentDeleteView,
    ForumPostDeleteView,
    ForumPostUpdateView,
    forum_post_create,
    forum_post_detail,
    forum_posts,
)

urlpatterns = [
    path("", forum_posts, name="forum-posts"),
    path("create/", forum_post_create, name="create-post"),
    path("<int:pk>/", forum_post_detail, name="post-detail"),
    path("<int:pk>/edit/", ForumPostUpdateView.as_view(), name="edit-post"),
    path("<int:pk>/delete/", ForumPostDeleteView.as_view(), name="delete-post"),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
]
