from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import login
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

from .forms import CustomUserCreationForm, CustomUserUpdateForm, LoginForm
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
        username = self.kwargs.get('username')
        user = get_object_or_404(CustomUser, username=username)

        if user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this profile.")

        return user

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        user = get_object_or_404(CustomUser, username=username)

        if user != self.request.user:
            raise PermissionDenied("You can only delete your own profile.")

        return user

@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(CustomUser, username=username)
    return render(request, 'accounts/user-profile.html', {'profile_user': profile_user})





