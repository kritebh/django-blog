from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user         = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio          = models.CharField(max_length=500)
    profile_pic  = models.ImageField(null=True,blank=True,upload_to="images/profile")
    twitter      = models.URLField(max_length=250,null=True,blank=True)
    instagram    = models.URLField(max_length=250,null=True,blank=True)
    linkedin     = models.URLField(max_length=250,null=True,blank=True)
    facebook     = models.URLField(max_length=250,null=True,blank=True)
    pinterest    = models.URLField(max_length=250,null=True,blank=True)
    github       = models.URLField(max_length=250,null=True,blank=True)
    def __str__(self):
        return str(self.user)