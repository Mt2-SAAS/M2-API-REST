from django.contrib import admin


# Locals Models
from .models import Player, Guild


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_id', 'name', 'level', 'exp', 'last_play', 'ip')
    search_fields = ['name']


class GuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'master', 'level', 'exp')
    search_fields = ['name']


admin.site.register(Player, PlayerAdmin)
admin.site.register(Guild, GuildAdmin)
