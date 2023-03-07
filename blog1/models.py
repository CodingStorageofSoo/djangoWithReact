from operator import mod
from turtle import tilt, update
from venv import create
from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)