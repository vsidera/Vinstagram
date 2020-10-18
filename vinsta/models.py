from django.db import models
from django.contrib.auth.models import User
import PIL.Image
from django.urls import reverse
# Create your models here.
class Image(models.Model):
    ''' a model for Image posts '''
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    profile = models.ForeignKey('Profile', default='1', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('vinsta-home')

class Profile(models.Model):
    ''' a model for profile '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos/',default='default.jpg')
    bio = models.TextField(max_length=500, blank=True, default=f'I love vinstagram!')   

    def __str__(self):
        return f'{self.user.username}' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # img = Image.open(self.image.path)
        img = PIL.Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)    

class Comment(models.Model):
    ''' a model for comments'''
    related_post = models.ForeignKey('Image', on_delete=models.CASCADE)
    name = models.ForeignKey('Profile', on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    
    def __str__(self):
        return f'Comment by {self.name}'            