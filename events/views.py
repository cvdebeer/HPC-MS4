from django.shortcuts import render, get_object_or_404
from .models import Event, EventType, AttendeeType
from django.views.generic import ListView


class EventsListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['date_start']
    paginate_by = 5
