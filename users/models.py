from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile.pics', blank=True)
    birthdate = models.DateField(default=None, blank=True, null=True)
    bio = models.TextField(default=None, blank=True, null=True)
    external_link = models.URLField(default=None, blank=True, null=True)
    facebook_link = models.URLField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Create your models here.
