from django.urls import path

from .views import blog_detail, blog_list

urlpatterns = [
    path("all/", blog_list, name="blog_list"),
    path("<slug:slug>/", blog_detail, name="blog_detail"),
]
