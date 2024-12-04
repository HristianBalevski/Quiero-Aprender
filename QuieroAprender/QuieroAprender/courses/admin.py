from django.contrib import admin

from QuieroAprender.courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "created_at", "updated_at")
    list_filter = ("level",)
    search_fields = ("title",)
