from django.shortcuts import render
from django.http import JsonResponse
from .models import Event
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.attendees.add(request.user)
    return redirect('calendar_view')


def events_api(request):
    events = Event.objects.all()
    events_list = [{
        'id': event.id,
        'title': event.title,
        'start': event.start_time.isoformat(),
        'end': event.end_time.isoformat(),
        'description': event.description
    } for event in events]
    return JsonResponse(events_list, safe=False)

def calendar_view(request):
    return render(request, 'events/calendar.html')


@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.attendees.add(request.user)
    return redirect('calendar_view')

@login_required
def my_events(request):
    user_events = request.user.events.all()
    return render(request, 'events/my_events.html', {'events': user_events})

def all_events(request):
    events = Event.objects.all()

    for event in events:
        event.is_registered = (
            request.user.is_authenticated and
            event.attendees.filter(id=request.user.id).exists()
        )
    context = {'events': events}
    return render(request, 'events/events.html', context)
