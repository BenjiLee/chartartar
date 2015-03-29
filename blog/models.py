from django.db import models
import datetime


class Post(models.Model):
    """Post model."""
    title = models.CharField(max_length=200)
    # author
    body = models.TextField()
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
