from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib.auth.views import LogoutView

from .models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)

        user.save()
        login(self.request, user)
        if hasattr(self.request, 'session'):
            self.request.session.save()

        return redirect('home')

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutUserView(LogoutView):
    pass


class UpdateProfileView(UpdateView):
    form_class = CustomUserUpdateForm
    template_name = 'accounts/update-user.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def profile_view(request):
    return render(request, 'accounts/user-profile.html', {'user': request.user})





