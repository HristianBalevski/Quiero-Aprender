from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("QuieroAprender.common.urls")),
    path("accounts/", include("QuieroAprender.accounts.urls")),
    path("course/", include("QuieroAprender.courses.urls")),
    path("lesson/", include("QuieroAprender.lessons.urls")),
    path("forum/", include("QuieroAprender.forum.urls")),
    path("blog/", include("QuieroAprender.blog.urls")),
    path("events/", include("QuieroAprender.events.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
