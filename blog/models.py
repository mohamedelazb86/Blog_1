from django.db import models
from taggit.managers import TaggableManager

from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author=models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    content=models.TextField(max_length=1500)
    image=models.ImageField(upload_to='image_post',null=True,blank=True)
    draft=models.BooleanField(default=True)
    tags = TaggableManager()
    category=models.ForeignKey('Category',related_name='post_category',on_delete=models.SET_NULL,null=True,blank=True)
    publish_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name=models.CharField(max_length=120)

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='comment_author',on_delete=models.SET_NULL,null=True,blank=True)
    comment=models.TextField(max_length=750)
    publish_date=models.DateTimeField(default=timezone.now)
    rate=models.CharField(max_length=20,choices=[(i,i) for i in range(1,6)])

    def __str__(self):
        return str(self.post)