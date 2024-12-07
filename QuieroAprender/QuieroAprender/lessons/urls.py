from django.urls import include, path
from rest_framework.routers import DefaultRouter

from QuieroAprender.lessons.views import (
    WordOfTheDayViewSet,
    delete_flashcard_view,
    flashcard_view,
    lesson_detail,
    translate_view,
    view_flashcards,
    word_of_the_day_view, ListWordsView,
)


router = DefaultRouter()
router.register(r"word-of-the-day", WordOfTheDayViewSet, basename="word-of-the-day")
urlpatterns = [
    path("api/", include(router.urls)),
    path("translate/", translate_view, name="translate"),
    path("flashcards/", flashcard_view, name="flashcards"),
    path("flashcards/view/", view_flashcards, name="view_flashcards"),
    path(
        "flashcards/delete/<int:index>/", delete_flashcard_view, name="delete_flashcard"
    ),
    path("<int:lesson_id>/<slug:slug>/", lesson_detail, name="lesson-detail"),
    path("word-of-the-day/", word_of_the_day_view, name="daily-word"),
    path("words/", ListWordsView.as_view(), name="word-of-the-day-list"),
    path('words/<int:pk>/', ListWordsView.as_view(), name='detail_update_delete_word'),
]

