from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.all().order_by("created_at")
    context = {"posts": posts}

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    previous_post = (
        BlogPost.objects.filter(created_at__lt=post.created_at)
        .order_by("-created_at")
        .first()
    )
    next_post = (
        BlogPost.objects.filter(created_at__gt=post.created_at)
        .order_by("created_at")
        .first()
    )

    context = {
        "post": post,
        "previous_post": previous_post,
        "next_post": next_post,
    }
    return render(request, "blog/blog_detail.html", context)
