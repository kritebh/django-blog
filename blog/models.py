from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('homepage')



class Post(models.Model):
    title = models.CharField(max_length=255)
    featured_image = models.ImageField(null=True,blank=True,upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default=6)
    body = RichTextField(blank=True,null=True)
    post_created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.id) + ' | '+ self.title+' | '+str(self.author)

    def get_absolute_url(self):
        return reverse('homepage')
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title,self.name)