from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from QuieroAprender.utils import generate_unique_slug


class BlogPost(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=80, blank=True, null=True, unique=True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(BlogPost, self.title, max_length=80)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Title: {self.title}"
