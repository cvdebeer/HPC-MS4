from django.contrib import admin
from .models import AttendeeType, EventType, Event

admin.site.register(AttendeeType)
admin.site.register(EventType)
admin.site.register(Event)
