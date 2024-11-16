from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    profile_photo = forms.ImageField(required=False)
    bio = forms.CharField(required=False)
    birth_date = forms.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile_photo', 'bio', 'birth_date')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        }


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'bio', 'birth_date', 'profile_photo')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Update First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Update Last Name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Update Email Address',
            }),
            'bio': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Update Biography',
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Update Birth Date',
            }),
            'profile_photo': forms.ClearableFileInput(attrs={
            }),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_photo', 'username', 'first_name', 'last_name', 'bio')