from django.urls import path
from .views import calendar_view, register_event, my_events, all_events, manage_events, delete_event, edit_event, \
    add_event

urlpatterns = [
    path('manage-events/', manage_events, name='manage_events_page'),
    path('add-event/', add_event, name='add_event'),
    path('edit-event/<int:event_id>/', edit_event, name='edit_event'),
    path('delete-event/<int:event_id>/', delete_event, name='delete_event'),

    path('calendar/', calendar_view, name='calendar_view'),
    path('register/<int:event_id>/', register_event, name='register_event'),
    path('all-events/', all_events, name='all_events'),
    path('my-events/', my_events, name='my_events'),

]
