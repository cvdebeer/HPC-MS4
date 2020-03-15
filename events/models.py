from django.db import models
from django.db.models import Q
from django.utils import timezone


class AttendeeType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EventTypeManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(description__icontains=query) |
                         Q(category__icontains=query)
                         )
            # distinct() is often necessary with Q lookups
            qs = qs.filter(or_lookup).distinct()
        return qs


class EventType(models.Model):
    Categories = models.TextChoices('Categories', 'Training Workshop')

    name = models.CharField(max_length=100)
    category = models.CharField(
        blank=True, choices=Categories.choices, max_length=20)
    attendee = models.ForeignKey(AttendeeType, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2)

    objects = EventTypeManager()

    def __str__(self):
        return "{0} - {1}".format(self.name, self.attendee)


'''
The entire Search app was copied and adjusted for this project from a tutorial by codingforentrepeneurs.com - https://www.codingforentrepreneurs.com/blog/a-multiple-model-django-search-engine/

An issue creating an "Related Field has invalid lookup: icontains" was resolved with the help of stack overflow- https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains
'''


class EventManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(event__name__icontains=query) |
                         Q(date_start__icontains=query) |
                         Q(facilitator__icontains=query) |
                         Q(location__icontains=query)
                         )
            # distinct() is often necessary with Q lookups
            qs = qs.filter(or_lookup).distinct()
        return qs


class Event(models.Model):
    event = models.ForeignKey(EventType, on_delete=models.CASCADE)
    date_start = models.DateField(default=timezone.now)
    date_end = models.DateField(default=timezone.now)
    time_start = models.TimeField(default=timezone.now)
    time_end = models.TimeField(default=timezone.now)
    location = models.CharField(
        default='The Ridge Wellness Center, 1 Ateljee Street, Randpark Ridge', max_length=255)
    facilitator = models.CharField(default='Sonja Simak', max_length=50)
    max_attendees = models.IntegerField(default=15)

    objects = EventManager()

    def __str__(self):
        return "{0}, {1}".format(self.date_start, self.event.name)
