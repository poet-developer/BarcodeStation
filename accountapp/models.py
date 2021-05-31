from django.db import models

# Create your models here.

class TextDB(models.Model):
    text = models.CharField(max_length=200, null=False)