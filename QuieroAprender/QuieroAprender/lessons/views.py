import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import CanSeeApiPermission
from ..courses.models import Course
from .models import Lesson, WordOfTheDay
from .serializers import WordOfTheDaySerializer
from .services import (
    create_flashcard,
    delete_flashcard,
    save_flashcard,
    translate_with_mymemory,
)

import requests
from django.conf import settings

API_BASE_URL = getattr(settings, "API_BASE_URL", "http://127.0.0.1:8000")


def is_teacher(user):
    return user.groups.filter(name="Teachers").exists()


@login_required
def translate_view(request):
    text = request.GET.get("text", "")
    translation = None
    error_message = None

    if text:
        try:
            translation = translate_with_mymemory(text)
        except Exception as e:
            error_message = str(e)

    context = {"text": text, "translation": translation, "error_message": error_message}
    return render(request, "lessons/api-translator.html", context)


@login_required
def flashcard_view(request):
    text = request.GET.get("text", "")
    flashcard = None
    error_message = None

    if text:
        try:
            flashcard = create_flashcard(text, from_lang="en", to_lang="es")
            save_flashcard(flashcard, user_id=request.user.id)
        except Exception as e:
            error_message = str(e)

    context = {"text": text, "flashcard": flashcard, "error_message": error_message}
    return render(request, "lessons/flashcard.html", context)


@login_required
def view_flashcards(request):
    user_id = request.user.id
    file_path = f"flashcards_{user_id}.json"

    try:
        with open(file_path, "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []

    return render(request, "lessons/view_flashcards.html", {"flashcards": flashcards})


@login_required
def delete_flashcard_view(request, index):
    user_id = request.user.id
    if delete_flashcard(index, user_id):
        return redirect("view_flashcards")
    else:
        return redirect("view_flashcards")


@login_required
def lessons_by_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = (
        Lesson.objects.filter(course=course)
        .select_related("course")
        .order_by("created_at")
    )
    context = {"course": course, "lessons": lessons}

    return render(request, "lessons/lessons-by-course.html", context)


@login_required
def lesson_detail(request, lesson_id, slug):
    lessons = Lesson.objects.all().order_by("id")

    lessons_per_page = 1
    paginator = Paginator(lessons, lessons_per_page)

    page_number = request.GET.get("page")

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
        "lesson": lesson,
        "page_obj": page_obj,
        "previous_lesson": previous_lesson,
        "next_lesson": next_lesson,
        "first_lesson": first_lesson,
        "last_lesson": last_lesson,
    }

    return render(request, "lessons/lesson-detail.html", context)


class WordOfTheDayViewSet(ReadOnlyModelViewSet):
    queryset = WordOfTheDay.objects.all()
    serializer_class = WordOfTheDaySerializer

    def get_queryset(self):
        today = now().date()
        return self.queryset.filter(date=today)


class ListWordsView(APIView):
    permission_classes = [IsAuthenticated, CanSeeApiPermission]

    def get(self, request, pk=None):
        if pk:
            try:
                word = WordOfTheDay.objects.get(pk=pk)
                serializer = WordOfTheDaySerializer(word)
                return Response(serializer.data)
            except WordOfTheDay.DoesNotExist:
                return Response(
                    {"error": "Word not found."}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            words = WordOfTheDay.objects.all()
            serializer = WordOfTheDaySerializer(words, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = WordOfTheDaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "Method PUT not allowed without an ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            word = WordOfTheDay.objects.get(pk=pk)
        except WordOfTheDay.DoesNotExist:
            return Response(
                {"error": "Word not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = WordOfTheDaySerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "Method DELETE not allowed without an ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            word = WordOfTheDay.objects.get(pk=pk)
            word.delete()
            return Response(
                {"message": "Word deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except WordOfTheDay.DoesNotExist:
            return Response(
                {"error": "Word not found."}, status=status.HTTP_404_NOT_FOUND
            )


@login_required
def word_of_the_day_view(request):
    api_url = f"{settings.API_BASE_URL}/lesson/api/word-of-the-day/"

    try:
        response = requests.get(api_url)

        response.raise_for_status()

        word_of_the_day = response.json()

        context = {"word": word_of_the_day[0] if word_of_the_day else None}
    except requests.exceptions.RequestException as e:

        context = {"word": None, "error": f"Could not fetch data: {str(e)}"}

    return render(request, "lessons/word-of-the-day.html", context)
