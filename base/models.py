"""
Database models
"""

from django.db import models


class Setting(models.Model):
    key = models.CharField(max_length=1255)
    value = models.TextField()

    def __str__(self) -> str:
        return self.key