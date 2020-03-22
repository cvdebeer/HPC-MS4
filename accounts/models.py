from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    experience = models.TextField(
        name='testimonial', blank=True, editable=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
