from django.contrib import admin


# Locals Models
from .models import Player, Guild


class PlayerAdmin(admin.ModelAdmin):
    """
        Player Admin
    """
    list_display = ("id", "account_id", "name", "level", "exp")
    search_fields = ["name"]


class GuildAdmin(admin.ModelAdmin):
    """
        Guild Admin
    """
    list_display = ("id", "name", "master", "level", "exp")
    search_fields = ["name"]


admin.site.register(Player, PlayerAdmin)
admin.site.register(Guild, GuildAdmin)
