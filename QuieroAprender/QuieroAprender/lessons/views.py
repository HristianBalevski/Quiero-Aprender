from .models import Lesson
from .services import translate_with_mymemory
import json, requests
from django.shortcuts import redirect, get_object_or_404, render
from .services import delete_flashcard, create_flashcard, save_flashcard


from ..courses.models import Course

from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import WordOfTheDay
from .serializers import WordOfTheDaySerializer
from django.utils.timezone import now
from django.core.paginator import Paginator


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
            save_flashcard(flashcard, user_id=request.user.id)
        except Exception as e:
            error_message = str(e)

    context = {
        'text': text,
        'flashcard': flashcard,
        'error_message': error_message
    }
    return render(request, 'lessons/flashcard.html', context)


def view_flashcards(request):

    user_id = request.user.id
    file_path = f"flashcards_{user_id}.json"

    try:
        with open(file_path, "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []

    return render(request, 'lessons/view_flashcards.html', {'flashcards': flashcards})


def delete_flashcard_view(request, index):

    user_id = request.user.id
    if delete_flashcard(index, user_id):
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

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lesson_detail(request, lesson_id, slug):
    lessons = Lesson.objects.all().order_by('id')

    lessons_per_page = 1
    paginator = Paginator(lessons, lessons_per_page)

    page_number = request.GET.get('page')

    if not page_number:
        current_lesson = get_object_or_404(Lesson, id=lesson_id, slug=slug)
        lesson_index = list(lessons).index(current_lesson)
        page_number = (lesson_index // lessons_per_page) + 1

    page_obj = paginator.get_page(page_number)
    lesson = page_obj.object_list[0]

    previous_lesson = None
    next_lesson = None

    if page_obj.has_previous():
        previous_lesson = lessons[page_obj.previous_page_number() - 1]

    if page_obj.has_next():
        next_lesson = lessons[page_obj.next_page_number() - 1]

    first_lesson = lessons.first()
    last_lesson = lessons.last()

    context = {
        'lesson': lesson,
        'page_obj': page_obj,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson,
        'first_lesson': first_lesson,
        'last_lesson': last_lesson,
    }

    return render(request, 'lessons/lesson-detail.html', context)




class WordOfTheDayViewSet(ReadOnlyModelViewSet):
    queryset = WordOfTheDay.objects.all()
    serializer_class = WordOfTheDaySerializer

    def get_queryset(self):
        today = now().date()
        return self.queryset.filter(date=today)


def word_of_the_day_view(request):
    api_url = 'http://127.0.0.1:8000/lessons/api/word-of-the-day/'
    response = requests.get(api_url)
    word_of_the_day = response.json() if response.status_code == 200 else []

    context = {
        'word': word_of_the_day[0] if word_of_the_day else None
    }
    return render(request, 'lessons/word-of-the-day.html', context)
