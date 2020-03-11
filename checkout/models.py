from django.db import models
from events.models import Event, EventType


class Booking(models.Model):
    full_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=254)
    add_to_mailing_list = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class BookingLineItem(models.Model):
    booking = models.ForeignKey(Booking, null=False, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}, {3}, {4}".format(self.quantity, self.event.event.name, self.event.event.cost_participant, self.event.event.cost_non_participant, self.event.event.cost_trainee)
