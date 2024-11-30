from django.urls import path

from QuieroAprender.courses.views import course_list, course_detail
from QuieroAprender.lessons.views import lessons_by_course

urlpatterns = [
    path('all/', course_list, name='all-courses'),
    path('<int:pk>/', course_detail, name='course-detail'),
    path('<int:course_id>/lessons/', lessons_by_course, name='lessons-by-course'),
]
