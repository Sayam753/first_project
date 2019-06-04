from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#one to many relation to user and posts.
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) #we have not used timezone.now() to call the function just pass the exact function as the value
    author = models.ForeignKey(User,on_delete = models.CASCADE) # this will help in deleting all the posts of the user when a user is deleted.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
