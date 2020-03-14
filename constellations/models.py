from django.db import models
from django.utils import timezone


class MailingList(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    accept_tc = models.BooleanField(name='Accept terms and conditions')
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.full_name
