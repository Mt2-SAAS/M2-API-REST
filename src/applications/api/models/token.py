"""
    Model for Tokens
    This tokens are used in users activation and password loss
"""
from django.db import models
from django.conf import settings
from core.models import Base

TOKEN_ACTIVATION = settings.TOKEN_ACTIVATION
TOKEN_RESET_PASSWORD = settings.TOKEN_RESET_PASSWORD


class Token(Base):
    TOKEN_TYPE = (
        (TOKEN_ACTIVATION, 'Activation'),
        (TOKEN_RESET_PASSWORD, 'Reset Password'),
    )
    token_type = models.CharField(max_length=20, choices=TOKEN_TYPE)
    user_id = models.IntegerField()
    _status = models.BooleanField(default=False) # Used = True

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        if isinstance(new_status, bool):
            self._status = new_status
        else:
            print('Please enter a valid status')

    @status.deleter
    def status(self):
        return self._status


    @classmethod
    def to_active(cls, user):
        token = cls()
        token.token_type = TOKEN_ACTIVATION
        token.user_id = user.id
        token.save()
        return token

    @classmethod
    def to_reset(cls, user):
        token = cls()
        token.token_type = TOKEN_RESET_PASSWORD
        token.user_id = user.id
        token.save()
        return token
