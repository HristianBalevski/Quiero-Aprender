from django.urls import path

from QuieroAprender.accounts.views import (
    LoginUserView,
    LogoutUserView,
    RegisterView,
    UpdateProfileView,
    UserDeleteView,
    profile_view,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("update/<str:username>/", UpdateProfileView.as_view(), name="update"),
    path("delete/<str:username>/", UserDeleteView.as_view(), name="delete"),
    path("profile/<str:username>/", profile_view, name="profile"),
]
