"""
    Base For Some API Views
"""
from django.core import exceptions
from django.conf import settings

from rest_framework.response import Response
from rest_framework import generics, status

from .authentication import AUTH_HEADER_TYPES
from .exceptions import InvalidToken, TokenError
from . import serializers


class TokenViewBase(generics.GenericAPIView):
    """
        Base class for generate Token for Auth
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = None

    www_authenticate_realm = 'api'

    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(
            AUTH_HEADER_TYPES[0],
            self.www_authenticate_realm,
        )

    def post(self, request):
        """
            Handler for method post
        """
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as token_error:
            raise InvalidToken(token_error.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class BaseInfo(generics.GenericAPIView):
    """
        Class for validate if user exist in database.
    """
    permission_classes = ()
    authentication_classes = ()
    model_class = None

    def get(self, request, **kwargs):
        """
            Handle get
        """
        try:
            self.model_class.objects.get(login=kwargs.get('username'))
            return Response({'status': True})
        except self.model_class.DoesNotExist:
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND)


class BaseActiveAccount(generics.GenericAPIView):
    """
        Base class for activate and account
    """
    permission_classes = ()
    authentication_classes = ()
    token_class = None
    model_class = None

    def get(self, request, **kwargs):
        """
            Handle get
        """
        try:
            token = self.token_class.objects.get(id=kwargs.get('token'))
            if not token.status and token.token_type == settings.TOKEN_ACTIVATION:
                account = self.model_class.objects.get(id=token.user_id)
                account.set_active_user()
                token.status = True
                token.save()
                account.save()
                user = serializers.CurrentUserSerializer(account)
                return Response({'status': True, 'user': user.data })
            return Response({'status': False}, status=status.HTTP_403_FORBIDDEN)
        except self.token_class.DoesNotExist:
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND)
        except exceptions.ValidationError:
            return Response({'status': False, 'message': 'Please send a valid UUID token'}, status=status.HTTP_404_NOT_FOUND)


class BaseResetPassword(generics.GenericAPIView):
    """
        Class for reset password in case of lost
    """
    
    serializer_class = None
    token_class = None
    model_class = None

    def get(self, request, **kwargs):
        """
            Helful response for frontend
        """
        try:
            token = self.token_class.objects.get(id=kwargs.get('token'))
            if not token.status and token.token_type == settings.TOKEN_RESET_PASSWORD:
                return Response({'status': True}, status=status.HTTP_202_ACCEPTED)
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND) 
        except self.token_class.DoesNotExist:
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND) 

    def post(self, request, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            token = self.token_class.objects.get(id=kwargs.get('token'))
            if not token.status and token.token_type == settings.TOKEN_RESET_PASSWORD:
                account = self.model_class.objects.get(id=token.user_id)
                account.set_password(serializer.validated_data['new_password'])
                token.status = True
                account.save()
                token.save()
                return Response({'status': True}, status.HTTP_202_ACCEPTED)
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND) 
        except self.token_class.DoesNotExist:
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND) 



class BaseGetTokenResetPassword(generics.GenericAPIView):
    serializer_class = None # Username 
    token_class = None
    model_class = None

    def get(self, request, **kwargs):
        try:
            token = self.token_class.objects.get(id=kwargs.get('token'))
            if not token.status and token.token_type == settings.TOKEN_ACTIVATION:
                return Response({'status': True}, status=status.HTTP_202_ACCEPTED)
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND) 
        except self.token_class.DoesNotExist:
            return Response({'status': False}, status=status.HTTP_404_NOT_FOUND) 

    def post(self, request, **kwargs):
        """
            Create token and send Email.
        """
        # Get data from the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'status': True}, status=status.HTTP_202_ACCEPTED)

        