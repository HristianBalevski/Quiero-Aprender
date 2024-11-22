from django.urls import path

from QuieroAprender.lessons.views import translate_view, flashcard_view, view_flashcards, delete_flashcard_view, \
    lesson_detail

urlpatterns = [

    path('translate/', translate_view, name='translate'),
    path('flashcards/', flashcard_view, name='flashcards'),
    path('flashcards/view/', view_flashcards, name='view_flashcards'),
    path('flashcards/delete/<int:index>/', delete_flashcard_view, name='delete_flashcard'),

    path('<int:lesson_id>/', lesson_detail, name='lesson-detail'),
]