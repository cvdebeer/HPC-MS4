from django.db import models
from django.utils import timezone


class AttendeeType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EventType(models.Model):
    Categories = models.TextChoices('Categories', 'Training Workshop')

    name = models.CharField(max_length=100)
    category = models.CharField(
        blank=True, choices=Categories.choices, max_length=20)
    attendee = models.ForeignKey(AttendeeType, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.attendee)


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

    def __str__(self):
        return "{0}, {1}".format(self.date_start, self.event.name)
