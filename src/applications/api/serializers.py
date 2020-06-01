from applications.authentication import authenticate
from rest_framework import exceptions, serializers
from django.utils.translation import ugettext_lazy as _

from .state import User
from .tokens import AccessToken


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
        return user

    class Meta:
        model = User
        fields = ('login', 'password', 'email', 'real_name', 'social_id')        
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
