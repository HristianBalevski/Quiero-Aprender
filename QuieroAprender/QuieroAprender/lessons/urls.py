from django.urls import path

from QuieroAprender.lessons.views import translate_view

urlpatterns = [
    path('sentences/', translate_view, name='translate'),
]