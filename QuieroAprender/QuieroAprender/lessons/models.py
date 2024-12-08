from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from QuieroAprender.utils import generate_unique_slug


class Lesson(models.Model):
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(null=True, blank=True, max_length=80, unique=True)
    content = RichTextUploadingField()
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="lessons"
    )
    image = models.ImageField(upload_to="lesson_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Lesson, self.title, max_length=80)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class WordOfTheDay(models.Model):
    spanish_word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example_sentence = models.TextField()
    date = models.DateField(unique=True)

    def __str__(self):
        return self.spanish_word
