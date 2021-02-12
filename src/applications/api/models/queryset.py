"""
    Default querysets
"""
from django.db import models


class PublishedQuerySet(models.QuerySet):
    """
        Return only published rows
    """
    def publish(self):
        """
            Filter for published
        """
        return self.filter(published=True)
