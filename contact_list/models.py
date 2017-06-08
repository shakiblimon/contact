from django.db import models

# Create your models here.
from django.forms import CharField


class Blog_post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
