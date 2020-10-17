from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Image(models.Model):
    ''' a model for Image posts '''
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    profile = models.ForeignKey('Profile', default='1', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    ''' a model for profile '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos/',default='default.jpg')
    bio = models.TextField(max_length=500, blank=True, default=f'I love vinstagram!')   

    def __str__(self):
        return f'{self.user.username}' 

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)    