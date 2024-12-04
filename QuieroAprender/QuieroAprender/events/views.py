from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.dateparse import parse_datetime

from .models import Event


def is_super_admin(user):
    return user.is_superuser or user.groups.filter(name="Super Admins").exists()


def is_staff_admin(user):
    return user.groups.filter(name="Staff Admins").exists()


@login_required
def manage_events(request):
    has_permission = request.user.has_perm("events.delete_event")

    if not (is_super_admin(request.user) or is_staff_admin(request.user)):
        raise PermissionDenied("You do not have the required role to manage events.")

    if not request.user.has_perm("events.view_event"):
        raise PermissionDenied("You do not have permission to view events.")

    total_events = Event.objects.all().order_by("-id")
    paginator = Paginator(total_events, 3)
    page_number = request.GET.get("page")
    events = paginator.get_page(page_number)

    context = {"events": events, "has_permission": has_permission}

    return render(request, "events/manage_events.html", context)


@login_required
def add_event(request):
    if not (is_super_admin(request.user) or is_staff_admin(request.user)):
        raise PermissionDenied("You do not have the required role to add events.")

    if not request.user.has_perm("events.add_event"):
        raise PermissionDenied("You do not have permission to add events.")

    if request.method == "POST":
        title = request.POST.get("title")
        start = request.POST.get("start")
        end = request.POST.get("end")
        description = request.POST.get("description", "")

        if not title or not start or not end:
            return render(
                request, "events/add_event.html", {"error": "All fields are required!"}
            )

        start_time = parse_datetime(start)
        end_time = parse_datetime(end)

        if not start_time or not end_time:
            return render(
                request, "events/add_event.html", {"error": "Invalid date format!"}
            )

        if start_time >= end_time:
            return render(
                request,
                "events/add_event.html",
                {
                    "error": "Start time must be earlier than end time!",
                    "title": title,
                    "description": description,
                    "start": start,
                    "end": end,
                },
            )

        Event.objects.create(
            title=title, start_time=start, end_time=end, description=description
        )
        return redirect("all_events")

    return render(request, "events/add_event.html")


@login_required
def edit_event(request, event_id):
    if not (is_super_admin(request.user) or is_staff_admin(request.user)):
        raise PermissionDenied("You do not have the required role to edit events.")

    if not request.user.has_perm("events.change_event"):
        raise PermissionDenied("You do not have permission to edit events.")

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.title = request.POST.get("title", event.title)
        event.start_time = request.POST.get("start", event.start_time)
        event.end_time = request.POST.get("end", event.end_time)
        event.description = request.POST.get("description", event.description)

        if event.start_time >= event.end_time:
            return render(
                request,
                "events/edit_event.html",
                {"event": event, "error": "Start time must be earlier than end time."},
            )

        event.save()
        return redirect("all_events")

    return render(request, "events/edit_event.html", {"event": event})


@login_required
def delete_event(request, event_id):
    if not (is_super_admin(request.user) or is_staff_admin(request.user)):
        raise PermissionDenied("You do not have the required role to delete events.")

    if not request.user.has_perm("events.delete_event"):
        raise PermissionDenied("You do not have permission to delete this event.")

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.delete()
        return redirect("manage_events_page")

    context = {
        "event": event,
    }

    return render(request, "events/delete_event.html", context)


@login_required
def register_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    event.attendees.add(request.user)
    return redirect("my_events")


@login_required
def my_events(request):

    user_events = request.user.events.all()
    return render(request, "events/my_events.html", {"events": user_events})


@login_required
def all_events(request):

    events = Event.objects.all().order_by("id")

    for event in events:
        event.is_registered = (
            request.user.is_authenticated
            and event.attendees.filter(id=request.user.id).exists()
        )
    context = {"events": events}
    return render(request, "events/events.html", context)


@login_required
def calendar_view(request):
    return render(request, "events/calendar.html")


@login_required
def events_api(request):

    events = Event.objects.all()
    events_list = [
        {
            "id": event.id,
            "title": event.title,
            "start": event.start_time.isoformat(),
            "end": event.end_time.isoformat(),
        }
        for event in events
    ]
    return JsonResponse(events_list, safe=False)
