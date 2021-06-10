from django.contrib import admin

# Locals Models
from .models import Download, Pages, Token


class DownloadAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'weight', 'link', 'published', 'create_at', 'modified_at')
    search_fields = ['provider']

class PagesAdmin(admin.ModelAdmin):
    list_display  = ('slug', 'title', 'published', 'create_at', 'modified_at')
    search_fields = ['slug']

class TokenAdmin(admin.ModelAdmin):
    list_display  = ('token_type', 'user_id', 'status')
    search_fields = ['user_id']

admin.site.register(Download, DownloadAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Token, TokenAdmin)
