"""
    Forms
"""
# Django
from django import forms
from django.utils.translation import ugettext_lazy as _

# Errors and Validations
from . import errors
from . import validations

# Local Models
from ..models import Account


class AccountCreationForm(forms.ModelForm):
    login = forms.CharField(
        label=_('Nombre de usuario'),
        min_length=4,
        max_length=30,       
        error_messages=errors.MESSAGES_USER,
        validators=[validations.white_spaces]
    )
    password = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.PasswordInput(),
        error_messages=errors.MESSAGES_PASSWORD,
        validators=[validations.white_spaces]
    )
    real_name = forms.CharField(
        label=_('Nombre real'),
        min_length=4,
        max_length=50,
        error_messages=errors.MESSAGES_GENERAL
    )
    email = forms.EmailField(
        max_length=50,
        error_messages=errors.MESSAGES_EMAIL
    )
    social_id = forms.IntegerField(
        label=_('Codigo de borrado'),
        error_messages=errors.MESSAGES_GENERAL,
        validators=[validations.seven_characters]
    )

    class Meta:
        model = Account
        fields = [
            'login',
            'password',
            'status',
            'real_name',
            'email',
            'social_id',
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        # user.set_key()
        if commit:
            user.save()
        return user

class AccountEditForm(forms.ModelForm):
    login = forms.CharField(
        label=_('Nombre de usuario'),
        min_length=4,
        max_length=30,       
        error_messages=errors.MESSAGES_USER,
        validators=[validations.white_spaces]
    )
    real_name = forms.CharField(
        label=_('Nombre real'),
        min_length=4,
        max_length=50,
        error_messages=errors.MESSAGES_GENERAL
    )
    email = forms.EmailField(
        max_length=50,
        error_messages=errors.MESSAGES_EMAIL
    )
    social_id = forms.IntegerField(
        label=_('Codigo de borrado'),
        error_messages=errors.MESSAGES_GENERAL,
        validators=[validations.seven_characters]
    )

    class Meta:
        model = Account
        fields = [
            'login',
            'status',
            'real_name',
            'email',
            'coins',
            'social_id',
        ]
