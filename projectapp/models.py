from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='project/', null=True)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
