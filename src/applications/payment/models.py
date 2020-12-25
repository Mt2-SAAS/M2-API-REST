# Copyright (c) 2017-2018 luispenagos91@gmail.com
# Distribuido bajo la licencia MIT Software Licence
# Mas informacion http://www.opensource.org/licenses/mit-license.php

from django.db import models

from core.models import Base


class PaymentLogs(Base):
    reference_id = models.CharField(max_length=100)
    account_id = models.IntegerField()
    username = models.CharField(max_length=30)
    coins = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'<PaymentLogs ({self.pk})>'

    class Meta:
        verbose_name = 'Payment Log'
        verbose_name_plural = 'Payment Logs'


class PaymentCode(Base):
    status = models.BooleanField(default=False)
    coins = models.IntegerField()
    user_claim = models.CharField(max_length=100, null=True, blank=True)
    account_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'<PaymentCodes ({self.pk})>'

    class Meta:
        verbose_name = 'PaymentCode'
        verbose_name_plural = 'PaymentCodes'

    def use_code(self, user):
        user.coins = user.coins + self.coins
        user.save()
        self.user_claim = user.login
        self.account_id = user.id
        self.status = True
        self.save()
