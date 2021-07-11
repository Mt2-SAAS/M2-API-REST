"""
    API Views
"""
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from applications.player.models import Player, Guild
from applications.authentication.models import Account
from . import serializers
from .base import (
    TokenViewBase,
    BaseInfo,
    BaseActiveAccount,
    BaseResetPassword,
    BaseGetTokenResetPassword
)
from .pagination import RankinPageNumber
from .stats import Stats
from .models import Download, Pages, Token, Site


class TokenObtainView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.TokenObtainPairSerializer


class RankingGuilds(generics.ListAPIView):
    """ 
        Ranking information for Guild
    """
    queryset = Guild.objects.all().order_by('-level', '-exp', '-win', '-ladder_point')
    serializer_class = serializers.RankingGuildSerializer
    pagination_class = RankinPageNumber


class RankingPlayers(generics.ListAPIView):
    """ 
        Ranking information for Players
    """
    queryset = Player.objects.all().exclude(Q(name__contains='[')).order_by('-level', '-exp')
    serializer_class = serializers.RankingPlayerSerializer
    pagination_class = RankinPageNumber


class DownloadApiView(generics.ListAPIView):
    """
        Downloads Links
    """
    permission_classes = (AllowAny,)
    queryset = Download.objects.publish()
    serializer_class = serializers.DownloadSerializer


class PagesApiView(generics.RetrieveAPIView):
    """
        Custom Pages
    """
    permission_classes = (AllowAny,)
    queryset = Pages.objects.publish()
    serializer_class = serializers.PagesSerializer
    lookup_field = 'slug'


class SiteApiView(generics.RetrieveAPIView):
    """
        Custom Pages
    """
    permission_classes = (AllowAny,)
    queryset = Site.objects.all()
    serializer_class = serializers.SiteSerializer
    lookup_field = 'slug'


class Info(BaseInfo):
    """
        Verify is user exist in database
    """
    permission_classes = (AllowAny,)
    model_class = Account


class ActiveAccount(BaseActiveAccount):
    """
        Active Account
    """
    throttle_scope = 'register'
    permission_classes = (AllowAny,)
    model_class = Account
    token_class = Token


class ResetPassword(BaseResetPassword):
    """
        Active Account
    """
    throttle_scope = 'register'
    permission_classes = (AllowAny,)
    serializer_class = serializers.ResetPasswordSerializer
    model_class = Account
    token_class = Token


class GetTokenResetPassword(BaseGetTokenResetPassword):
    """
        Active Account
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.RequestPasswordSerializer
    model_class = Account
    token_class = Token


class RegisterGeneric(generics.CreateAPIView):
    """
        Register Users into database.
    """
    throttle_scope = 'register'
    queryset = Account.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = (AllowAny,)


class CurrentUserView(APIView):
    """
        Return current user
    """
    serializer_class = serializers.CurrentUserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)


class CurrentUserPlayersView(APIView):
    """
        Show player for current user login
    """
    serializer_class = serializers.RankingPlayerSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        userid = request.user.id
        players = Player.objects.filter(account_id=userid)
        serializer = self.serializer_class(players, many=True)
        return Response(serializer.data)


class ChangePassword(APIView):
    """
        Change Password for current user
    """
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user
        if serializer.is_valid(raise_exception=True):
            if user.check_password(serializer.validated_data['current_password']):
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({'message': 'Change success'})
            return Response({'meesage': 'Password dont match'}, status=status.HTTP_401_UNAUTHORIZED)


class ServerStats(APIView):
    """
        Show player for current user login
    """

    def get(self, request):
        """
            Endpoint use for view stats from database
        """
        query = Stats()
        stats = query.get_format_stats()
        return Response(stats)
