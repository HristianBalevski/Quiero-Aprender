from django import forms
from django.contrib import admin

from .models import Lesson, WordOfTheDay
from .widgets import CKEditor5Widget


class LessonAdminForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"
        widgets = {
            "content": CKEditor5Widget(),
        }


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    form = LessonAdminForm
    list_display = ["title", "course", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title"]


@admin.register(WordOfTheDay)
class WordOfTheDayAdmin(admin.ModelAdmin):
    list_display = ["spanish_word", "translation", "example_sentence", "date"]
