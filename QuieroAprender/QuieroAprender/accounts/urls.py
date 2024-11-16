from django.urls import path

from QuieroAprender.accounts.views import RegisterView, LoginUserView, LogoutUserView, UpdateProfileView, \
    profile_view, UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('update/', UpdateProfileView.as_view(), name='update'),
    path('delete/', UserDeleteView.as_view(), name='delete'),
    path('profile/', profile_view, name='profile'),

]