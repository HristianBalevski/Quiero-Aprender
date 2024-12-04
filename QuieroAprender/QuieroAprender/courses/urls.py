from django.urls import path

from QuieroAprender.courses.views import course_detail, course_list
from QuieroAprender.lessons.views import lessons_by_course

urlpatterns = [
    path("all/", course_list, name="all-courses"),
    path("<int:pk>/", course_detail, name="course-detail"),
    path("<int:course_id>/lessons/", lessons_by_course, name="lessons-by-course"),
]
