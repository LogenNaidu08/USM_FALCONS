# backend/news/models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title