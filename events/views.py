from django.shortcuts import render
from .models import Event, EventType
from django.views.generic import ListView


class EventsListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['date_start']
