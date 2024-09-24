"""
    Manager
"""

# From local base models and managers
from ..base import BaseAccountManager


class AccountManager(BaseAccountManager):
    """
        Manager for create users
    """
    def _create_account(self, login, password, email, real_name, social_id):
        """
            Private create account
        """
        if not login:
            raise ValueError("The given login must be set")

        email = self.normalize_email(email)
        user = self.model(
            login=login, email=email, real_name=real_name, social_id=social_id
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_account(
        self, login, password=None, email=None, real_name=None, social_id=None
    ):
        """
            Public create account
        """
        return self._create_account(
            login,
            password,
            email,
            real_name,
            social_id
        )
