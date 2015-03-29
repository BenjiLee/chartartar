from django.db import models


class Blog(models.Model):
    """Model la Blog"""
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField('date published')


