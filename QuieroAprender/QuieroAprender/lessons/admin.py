from django.contrib import admin
from django import forms
from .models import Lesson
from .widgets import CKEditor5Widget

class LessonAdminForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(),
        }

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    form = LessonAdminForm
