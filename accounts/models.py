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

    '''
    Code below is from a tutorial by Corey Shafer to scale down images that are uploaded by the user -https://www.youtube.com/watch?v=CQ90L5jfldw 
    '''

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
