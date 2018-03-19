from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)
    neighborhood = models.ForeignKey(Hood, null=True) 


    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

class Hood(models.Model):
    image = models.ImageField(upload_to = 'images/', null = True)
    name = models.CharField(max_length=30)
    status = models.TextField()
    occupants = models.IntegerField(default=0)

class Business(models.Model):
    name = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, null=True) 
    neighborhood = models.ForeignKey(Hood, null=True) 
