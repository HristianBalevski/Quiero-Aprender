from .models import Lesson
from .services import translate_with_mymemory
import json

from django.shortcuts import redirect, get_object_or_404
from .services import delete_flashcard, create_flashcard, save_flashcard
from django.shortcuts import render

from ..courses.models import Course


def translate_view(request):
    text = request.GET.get('text', '')
    translation = None
    error_message = None

    if text:
        try:
            translation = translate_with_mymemory(text)
        except Exception as e:
            error_message = str(e)

    context = {
        'text': text,
        'translation': translation,
        'error_message': error_message
    }
    return render(request, 'lessons/api-translator.html', context)



def flashcard_view(request):
    text = request.GET.get('text', '')
    flashcard = None
    error_message = None

    if text:
        try:

            flashcard = create_flashcard(text, from_lang="en", to_lang="es")
            save_flashcard(flashcard)
        except Exception as e:
            error_message = str(e)

    context = {
        'text': text,
        'flashcard': flashcard,
        'error_message': error_message
    }
    return render(request, 'lessons/flashcard.html', context)


def view_flashcards(request):
    try:
        with open("flashcards.json", "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []

    return render(request, 'lessons/view_flashcards.html', {'flashcards': flashcards})


def delete_flashcard_view(request, index):
    if delete_flashcard(index):
        return redirect('view_flashcards')
    else:
        return redirect('view_flashcards')


def lessons_by_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course).select_related('course').order_by('created_at')
    context = {
        'course': course,
        'lessons': lessons
    }

    return render(request, 'lessons/lessons-by-course.html', context)


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    context = {'lesson': lesson}

    return render(request, 'lessons/lesson-detail.html', context)



