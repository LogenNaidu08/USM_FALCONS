# backend/core/models.py
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='teams/')
    founded = models.DateField()
    stadium = models.CharField(max_length=100)

    def __str__(self):
        return self.name