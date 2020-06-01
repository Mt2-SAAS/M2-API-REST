# Copyright (c) 2017-2018 luispenagos91@gmail.com
# Distribuido bajo la licencia MIT Software Licence
# Mas informacion http://www.opensource.org/licenses/mit-license.php

# imporacion por defecto
from django.urls import path

from . import views

urlpatterns = [
    path('token/', views.TokenObtainView.as_view(), name='login'),
    path('signup/', views.RegisterGeneric.as_view(), name='signup'),
    path('guild_rank/', views.RankingGuilds.as_view(), name='guild_rank'),
    path('player_rank/', views.RankingPlayers.as_view(), name='player_rank'),
    path('current_user/', views.CurrentUserView.as_view(), name='current_user'),
    path('current_players/', views.CurrentUserPlayersView.as_view(), name='current_user'),
    path('change_pass/', views.ChangePassword.as_view(), name='change_pass' ),
    path('info/<str:username>', views.Info.as_view(), name='info')
]
