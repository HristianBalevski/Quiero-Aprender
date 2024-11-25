from django.urls import path
from .views import events_api, calendar_view, register_event, my_events, all_events

urlpatterns = [
    path('api/', events_api, name='events_api'),
    path('calendar/', calendar_view, name='calendar_view'),
    path('register/<int:event_id>/', register_event, name='register_event'),
    path('all/', all_events, name='all_events'),
    path('', my_events, name='my_events'),

]
