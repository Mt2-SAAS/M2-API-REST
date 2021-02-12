"""
    Model for Custom Pages
"""
from django.db import models
from core.models import Base
from .queryset import PublishedQuerySet


class Pages(Base):
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=True)

    objects = PublishedQuerySet.as_manager()

    def __str__(self):
        return f'<Page ({self.title})>'

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
