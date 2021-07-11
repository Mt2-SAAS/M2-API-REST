"""
    Serializers
"""

from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from applications.authentication import authenticate
from rest_framework import exceptions, serializers

from .state import User
from .tokens import AccessToken
from .utils import get_string_and_html
from .models import Pages, Token, Site, Image

class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'password'
        kwargs['write_only'] = True

        super().__init__(*args, **kwargs)


class TokenObtainSerializer(serializers.Serializer):
    username_field = User.USERNAME_FIELD

    default_error_messages = {
        'no_active_account': _('No active account found with the given credentials')
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField()

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        # Prior to Django 1.10, inactive users could be authenticated with the
        # default `ModelBackend`.  As of Django 1.10, the `ModelBackend`
        # prevents inactive users from authenticating.  App designers can still
        # allow inactive users to authenticate by opting for the new
        # `AllowAllUsersModelBackend`.  However, we explicitly prevent inactive
        # users from authenticating to enforce a reasonable policy and provide
        # sensible backwards compatibility with older Django versions.
        if self.user is None:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}

    @classmethod
    def get_token(cls, user):
        raise NotImplementedError('Must implement `get_token` method for `TokenObtainSerializer` subclasses')


class TokenObtainPairSerializer(TokenObtainSerializer):
    """
        Helper class for create token
    """

    @classmethod
    def get_token(cls, user):
        return AccessToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)

        return data


class RegisterSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_account(**validated_data)
        user.save()
        token = Token.to_active(user)
        self.send_activation_email(user, token)
        return user

    def send_activation_email(self, user, token):
        html_content, string_content = get_string_and_html('email/email_confirmation.html', {'user': user, 'token': token})
        subject = _('Bienvenido a ') + settings.SERVERNAME
        email = EmailMultiAlternatives(subject, string_content, settings.EMAIL_HOST_USER, [user.email])
        email.attach_alternative(html_content, "text/html")
        email.send()

    class Meta:
        model = User
        fields = ('login', 'password', 'email', 'real_name', 'social_id', 'answer1')
        extra_kwargs = {'password': {'write_only': True}}


class CurrentUserSerializer(serializers.ModelSerializer):
    """
        Current user serializer
    """
    class Meta:
        model = User
        fields = ('login', 'status', 'real_name',
        'email', 'coins', 'create_time')


class RankingPlayerSerializer(serializers.Serializer):
    """
        Serializer For Players
    """
    account_id = serializers.IntegerField()
    name = serializers.CharField()	
    level = serializers.IntegerField()
    exp = serializers.IntegerField()	


class RankingGuildSerializer(serializers.Serializer):
    """
        Serializer for Guilds
    """
    name = serializers.CharField()
    level = serializers.IntegerField()
    exp = serializers.IntegerField()
    ladder_point = serializers.IntegerField()


class ChangePasswordSerializer(serializers.Serializer):
    """
    """
    current_password = PasswordField()
    new_password = PasswordField()
    new_password_again = PasswordField()

    def validate(self, data):
        if data['new_password'] != data['new_password_again']:
            raise serializers.ValidationError('password must be equal')
        return data


class ResetPasswordSerializer(serializers.Serializer):
    """
    """
    new_password = PasswordField()
    new_password_again = PasswordField()

    def validate(self, data):
        if data['new_password'] != data['new_password_again']:
            raise serializers.ValidationError('password must be equal')
        return data


class DownloadSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    provider = serializers.CharField(max_length=30)
    weight = serializers.DecimalField(max_digits=5, decimal_places=3)
    link = serializers.CharField(max_length=100)
    create_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()


class PagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = ('slug', 'title', 'content',
        'published', 'create_at', 'modified_at')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class RequestPasswordSerializer(serializers.Serializer):
    login = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(login=data['login'])
            token = Token.to_reset(user)
            self.send_rest_password_email(user, token)
            return data
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found in database')

    def send_rest_password_email(self, user, token):
        html_content, string_content = get_string_and_html('email/reset_password.html', {'user': user, 'token': token})
        subject = _('Olvido de Contraseña - ') + settings.SERVERNAME
        email = EmailMultiAlternatives(subject, string_content, settings.EMAIL_HOST_USER, [user.email])
        email.attach_alternative(html_content, "text/html")
        email.send()


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('name', 'image', 'types')


class SiteSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True)
    footer_menu = PagesSerializer(many=True)

    class Meta:
        model = Site
        fields = ('name', 'slug', 'images', 'initial_level',
        'max_level', 'rates', 'facebook_url', 'facebook_enable',
        'footer_menu', 'footer_info', 'footer_menu_enable', 'footer_info_enable', 
        'forum_url', 'last_online')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
