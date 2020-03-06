from django.db import models
from datetime import date, datetime


class EventType(models.Model):
    Categories = models.TextChoices('Categories', 'Training Workshop')
    AttendeeType = models.TextChoices(
        'AttendeeType', 'Participant Non-Participant Trainee')

    name = models.CharField(max_length=100)
    category = models.CharField(
        blank=True, choices=Categories.choices, max_length=8)
    description = models.CharField(max_length=150)
    cost_participant = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2)
    cost_non_participant = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2)
    cost_trainee = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Event(models.Model):
    event = models.ForeignKey(EventType, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    location = models.CharField(
        default='The Ridge Wellness Center, 1 Ateljee Street, Randpark Ridge', max_length=255)
    facilitator = models.CharField(default='Sonja Simak', max_length=50)
    max_attendees = models.IntegerField(default=15)

    def __str__(self):
        return "{0}, {1}".format(self.date_start, self.event.name)
