from django.shortcuts import render

from QuieroAprender.courses.models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course-list.html", {"courses": courses})


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    context = {"course": course}

    return render(request, "courses/course-detail.html", context)
