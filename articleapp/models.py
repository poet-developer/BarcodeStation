from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    wrtier = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='article')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='article')
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='article/',null=False)
    created_at = models.DateField(auto_now_add=True,null=True)