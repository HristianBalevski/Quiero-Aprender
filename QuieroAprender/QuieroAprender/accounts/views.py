from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserUpdateForm, LoginForm
from django.contrib.auth.views import LogoutView

from .models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('update', username=user.username)


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        return super().form_valid(form)


class LogoutUserView(LogoutView):
    pass


class UpdateProfileView(UpdateView):
    form_class = CustomUserUpdateForm
    template_name = 'accounts/update-user.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})

    def get_object(self, queryset=None):
        return self.request.user

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'accounts/user-profile.html', {'user': user})





