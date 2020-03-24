from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, User


'''
This code comes from the tutorial by Corey Schafer - https://www.youtube.com/watch?v=FdVuKt_iuSI
It allows us to create a profile, every time a user is created
'''


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
