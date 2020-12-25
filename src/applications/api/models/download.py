"""
    Download Model for the API
"""
from datetime import timezone
from django.db import models
from core.models import Base


class DownloadQuerySet(models.QuerySet):
    def publish(self):
        return self.filter(published=True)


class Download(Base):
    provider = models.CharField(max_length=30)
    weight = models.DecimalField(max_digits=5, decimal_places=3)
    link = models.CharField(max_length=100)
    published = models.BooleanField(default=True)

    objects = DownloadQuerySet.as_manager()

    def __str__(self):
        return f'<Download ({self.link})>'

    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'
