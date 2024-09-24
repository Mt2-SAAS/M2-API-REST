"""
    Models
"""

from django.db import models
from django.utils import timezone
from django.conf import settings

# Translation
from django.utils.translation import gettext_lazy as _

# From local base models and managers
from ..base import AbstractBaseAccount

# Local Manager
from ._manager import AccountManager


class AbstractAccount(AbstractBaseAccount):
    """
        Abstract Account
    """
    login = models.CharField(unique=True, max_length=30)
    real_name = models.CharField(max_length=16, blank=True, null=True)
    social_id = models.CharField(max_length=13)
    email = models.CharField(max_length=64)
    coins = models.IntegerField(default=0)
    create_time = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["social_id", "email"]

    class Meta:
        """
            Meta Class Config
        """
        abstract = True

    def __str__(self):
        return f"{self.login}"


class Account(AbstractAccount):
    """
    You can add more options to account
    """

    class Meta:
        """
        This are a legacy model and no need migrations.
        """

        managed = False
        db_table = "account"
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
