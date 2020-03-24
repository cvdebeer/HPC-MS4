from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import AttendeeType, Event, EventType


class EventsListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['date_start']
