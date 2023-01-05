"""
Database models
"""

from django.db import models


class Setting(models.Model):
    key = models.CharField(max_length=1255)
    value = models.TextField()

    def __str__(self) -> str:
        return self.key

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='media/portfolio')
    link1 = models.CharField(max_length=500)
    link2 = models.CharField(max_length=500)
    link3 = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.FileField(upload_to='media/blog')

    def __str__(self) -> str:
        return self.name
