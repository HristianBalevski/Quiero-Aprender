from django.shortcuts import render
from django.urls import path

from QuieroAprender.common.views import (
    about,
    contact_view,
    country_details,
    home,
    privacy,
    terms,
    university,
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("university/", university, name="university"),
    path("contact/", contact_view, name="contact"),
    path("country/<str:country_name>/", country_details, name="country_details"),
    path("terms/", terms, name="terms"),
    path("privacy/", privacy, name="privacy"),
]


def custom_permission_denied_view(request, exception):
    return render(request, "403.html", {"exception": exception}, status=403)


handler403 = "QuieroAprender.common.urls.custom_permission_denied_view"
