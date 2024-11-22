from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView
from .models import ForumPost
from .forms import ForumPostForm



def forum_posts(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    context = {'posts': posts}

    return render(request, 'forum/forum-posts.html', context)


def forum_post_detail(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    context = {'post': post}

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
    return render(request, 'forum/forum-post-form.html', {'form': form})


class ForumPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ForumPost
    fields = ['title', 'content']
    template_name = 'forum/forum-post-form.html'
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


