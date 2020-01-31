from django.db import models
from django.conf import settings

# CNN rss model
class Cnn(models.Model):
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=100)
    content = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title
