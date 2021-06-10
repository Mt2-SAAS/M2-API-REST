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
    phone1 = models.CharField(max_length=16, blank=True, null=True)
    phone2 = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    zipcode = models.CharField(max_length=7, blank=True, null=True)
    create_time = models.DateTimeField(default=timezone.now)
    question1 = models.CharField(max_length=48, blank=True, null=True)
    answer1 = models.CharField(max_length=48, blank=True, null=True)
    question2 = models.CharField(max_length=48, blank=True, null=True)
    answer2 = models.CharField(max_length=48, blank=True, null=True)
    is_testor = models.IntegerField(default=0)
    securitycode = models.CharField(max_length=192, blank=True, null=True)
    newsletter = models.IntegerField(blank=True, null=True)
    empire = models.IntegerField(default=0)
    name_checked = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    cash = models.IntegerField(default=0)
    gold_expire = models.DateTimeField(default=settings.BUFFSTUF)
    silver_expire = models.DateTimeField(default=settings.BUFFSTUF)
    safebox_expire = models.DateTimeField(default=settings.BUFFSTUF)
    autoloot_expire = models.DateTimeField(default=settings.BUFFSTUF)
    fish_mind_expire = models.DateTimeField(default=settings.BUFFSTUF)
    marriage_fast_expire = models.DateTimeField(default=settings.BUFFSTUF)
    money_drop_rate_expire = models.DateTimeField(default=settings.BUFFSTUF)
    ttl_cash = models.IntegerField(default=0)
    ttl_mileage = models.IntegerField(default=0)
    channel_company = models.CharField(max_length=30, default='')
    last_play = models.DateTimeField(default=settings.ACTIVATE)
    ticket_id = models.CharField(max_length=30)
    coins = models.IntegerField(default=0)
    drs = models.IntegerField(default=0)
    web_admin = models.IntegerField(default=0)
    web_ip = models.CharField(max_length=15)
    web_aktiviert = models.CharField(max_length=32)
    user_admin = models.CharField(max_length=15)
    passlost_token = models.CharField(max_length=32, blank=True, null=True)
    passchange_token = models.CharField(max_length=32, blank=True, null=True)
    emailchange_token = models.CharField(max_length=32, blank=True, null=True)
    new_email_change = models.CharField(max_length=32, blank=True, null=True)
    new_email_change2 = models.CharField(max_length=32, blank=True, null=True)
    stergere_account = models.CharField(max_length=32, blank=True, null=True)
    unban_date = models.CharField(max_length=32, blank=True, null=True)
    motiv_ban = models.CharField(max_length=132, blank=True, null=True)
    jcoins = models.CharField(max_length=32, blank=True, null=True)
    reason = models.CharField(max_length=256, blank=True, null=True)
    donation = models.FloatField(default=0)
    type1_active = models.IntegerField(default=0)
    kwix_coins = models.IntegerField(blank=True, null=True)
    kwix_admin = models.IntegerField(default=0)
    kwix_chm = models.CharField(max_length=255, default='')
    kwix_chm_code = models.CharField(max_length=255, default='')
    last_ip = models.CharField(max_length=255, default='')
    register_ip = models.CharField(max_length=256, default='')
    user_level = models.SmallIntegerField(default=0)
    ban_reason = models.CharField(max_length=256)
    ban_expire = models.CharField(max_length=10)
    referrer_link = models.CharField(max_length=256)
    referrer = models.CharField(max_length=256)
    rb_points = models.IntegerField(default=0)
    ysifre = models.CharField(max_length=255)
    yemail = models.CharField(max_length=255)
    ylogin = models.CharField(max_length=255)
    tkod = models.CharField(max_length=10)
    ypass = models.CharField(max_length=255)
    ban_neden = models.CharField(max_length=255)
    durum = models.IntegerField(default=0)
    davet = models.IntegerField(default=0)
    davet_durum = models.IntegerField(default=0)
    ip = models.CharField(max_length=40)
    tel_degisim = models.CharField(max_length=255)
    mac = models.CharField(max_length=250)
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
