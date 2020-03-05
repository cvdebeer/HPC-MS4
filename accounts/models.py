from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    experience = models.TextField(name='Testimonial', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
