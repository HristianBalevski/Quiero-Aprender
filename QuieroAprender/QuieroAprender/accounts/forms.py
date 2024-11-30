from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .validators import validate_image_size
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    profile_photo = forms.ImageField(required=False, validators=[validate_image_size])
    bio = forms.CharField(required=False)
    birth_date = forms.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile_photo', 'bio', 'birth_date')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Create a password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
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
                'rows': 5,
                'placeholder': 'Tell us a little about yourself',
                'class': 'bio-textarea',
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Update Birth Date',
            }),
            'profile_photo': forms.ClearableFileInput(),
        }

    def clean_profile_photo(self):
        profile_photo = self.cleaned_data.get('profile_photo')

        if profile_photo:
            validate_image_size(profile_photo)
        return profile_photo


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_photo', 'username', 'first_name', 'last_name', 'bio')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), required=True)

