from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView
from .models import ForumPost, Comment
from .forms import ForumPostForm, CommentForm


def forum_posts(request):
    posts = ForumPost.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'posts': posts, 'page_obj': page_obj}

    return render(request, 'forum/forum-posts.html', context)


def forum_post_detail(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'forum/forum-post-detail.html', context)


@login_required
def forum_post_create(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('forum-posts')
        else:
            print(form.errors)
    else:
        form = ForumPostForm()
        print("GET request, form loaded")
    return render(request, 'forum/forum-create-post.html', {'form': form})


class ForumPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ForumPost
    fields = ['title', 'content']
    template_name = 'forum/forum-edit-post.html'
    success_url = reverse_lazy('forum-posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user



class ForumPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ForumPost
    template_name = 'forum/forum-delete-post.html'
    success_url = reverse_lazy('forum-posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user or self.request.user.is_staff


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'forum/comment-delete.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user


