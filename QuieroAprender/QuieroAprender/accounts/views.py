from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserUpdateForm, LoginForm
from .models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("profile", username=user.username)


class LoginUserView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm


class LogoutUserView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully!")
        return super().dispatch(request, *args, **kwargs)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserUpdateForm
    template_name = "accounts/update-user.html"
    success_url = reverse_lazy("profile")

    def get_success_url(self):
        return reverse("profile", kwargs={"username": self.request.user.username})

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        user = get_object_or_404(CustomUser, username=username)

        if user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this profile.")

        return user


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "accounts/delete-profile.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        user = get_object_or_404(CustomUser, username=username)

        if user != self.request.user:
            raise PermissionDenied("You can only delete your own profile.")

        return user


@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(CustomUser, username=username)
    return render(request, "accounts/user-profile.html", {"profile_user": profile_user})
