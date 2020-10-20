from django.db import models
from django.contrib.auth.models import User
import PIL.Image
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    ''' a model for Image posts '''
    image = CloudinaryField('image')
    caption = models.TextField()
    profile = models.ForeignKey('Profile', default='1', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('vinsta-home')

    def save_image(self):
        ''' method to save an image post instance '''
        self.save()

    def delete_image(self):
        '''method to delete an image post instance '''
        self.delete()

    def update_caption(self, new_caption):
        ''' method to update an image's caption '''
        self.caption = new_caption
        self.save()
        
    @classmethod    
    def get_user_images(cls, user_id):
        ''' method to retrieve all images'''
        img = Image.objects.filter(profile=user_id).all()
        sort = sorted(img, key=lambda t: t.created_on)
        return sort    

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

    def save_profile(self):
        ''' method to save a user's profile '''
        self.save()

    def delete_profile(self):
        '''method to delete a user's profile '''
        self.delete()

    def update_bio(self, new_bio):
        ''' method to update a users profile bio '''
        self.bio = new_bio
        self.save()

    def update_image(self, user_id, new_image):
        ''' method to update a users profile image '''
        user = User.objects.get(id=user_id)
        self.photo = new_image
        self.save()        

class Comment(models.Model):
    ''' a model for comments'''
    related_post = models.ForeignKey('Image', on_delete=models.CASCADE)
    name = models.ForeignKey('Profile', on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    
    def save_comments(self):
        ''' method to save comment instance '''
        self.save()

    def delete_comment(self):
        '''method to delete comment instance '''
        self.delete()
    
    def edit_comment(self, new_comment):
        ''' method to edit a comment '''
        self.comment_body = new_comment
        self.save()

    def __str__(self):
        return f'Comment by {self.name}'