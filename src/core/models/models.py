"""
    Base models
"""
import uuid
from django.db import models


class Base(models.Model):
    """
    Base model that provide all necesary functionality.
    """

    id = models.UUIDField(primary_key=True, default=None, editable=False)

    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def _set_pk(self):
        self.pk = uuid.uuid4()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self._set_pk()

        return super(Base, self).save(*args, **kwargs)


class BaseDelete(Base):
    _deleted = models.BooleanField(default=False)

    class Meta(Base.Meta):
        abstract = True

    def delete(self):
        self._deleted = True
        self.save()
