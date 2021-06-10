"""
    Models
"""

from django.db import models
from django.utils import timezone
from django.conf import settings

# Utils Timezone
from datetime import datetime, timedelta

# Translation
from django.utils.translation import gettext_lazy as _

# From local base models and managers
from ..base import (
    AbstractBaseAccount
)

# Local Manager
from .manager import AccountManager


class AbstractAccount(AbstractBaseAccount):
    login = models.CharField(unique=True, max_length=30)
    real_name = models.CharField(max_length=16, blank=True, null=True)
    social_id = models.CharField(max_length=13)
    email = models.CharField(max_length=64)
    coins = models.IntegerField(default=0)
    address = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(default=timezone.now)
    gold_expire = models.DateTimeField(default=settings.BUFFSTUF)
    silver_expire = models.DateTimeField(default=settings.BUFFSTUF)
    safebox_expire = models.DateTimeField(default=settings.BUFFSTUF)
    autoloot_expire = models.DateTimeField(default=settings.BUFFSTUF)
    fish_mind_expire = models.DateTimeField(default=settings.BUFFSTUF)
    marriage_fast_expire = models.DateTimeField(default=settings.BUFFSTUF)
    money_drop_rate_expire = models.DateTimeField(default=settings.BUFFSTUF)
    token_expire = models.DateTimeField(blank=True, null=True)
    refer_id = models.IntegerField(blank=True, null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['real_name', 'social_id', 'email']

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.login}'


class Account(AbstractAccount):
    """
        You can add more options to account
    """

    class Meta:
        """
            This are a legacy model and no need migrations.
        """
        managed = False
        db_table = 'account'
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
