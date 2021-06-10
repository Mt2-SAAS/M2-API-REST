"""
    Py
"""
from applications.authentication import get_user_model
from django.conf import settings

from .backends import TokenBackend

User = get_user_model()
token_backend = TokenBackend(settings.ALGORITHM, settings.SIGNING_KEY,
                             settings.VERIFYING_KEY, settings.AUDIENCE, settings.ISSUER)
