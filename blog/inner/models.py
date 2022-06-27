from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
    images=models.ImageField(upload_to='images')
    

class Comment(models.Model):
    comment = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    
class Popular(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
    images=models.ImageField(upload_to='images')
    is_popular= models.BooleanField(default=False)