from django.contrib import admin

# Locals Models
from .models import Download, Pages, Token, Site, Image

# Translation
from django.utils.translation import gettext_lazy as _


class DownloadAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'weight', 'link', 'published', 'create_at', 'modified_at')
    search_fields = ['provider']

class PagesAdmin(admin.ModelAdmin):
    list_display  = ('slug', 'title', 'published', 'create_at', 'modified_at')
    search_fields = ['slug']

class TokenAdmin(admin.ModelAdmin):
    list_display  = ('token_type', 'user_id', 'status')
    search_fields = ['user_id']

class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'initial_level', 'max_level', 'rates')
    fieldsets = (
        (_('Nombre del sitio'), {'fields': ('name',)}),
        (_('URL Slug'), {'fields': ('slug',)}),
        (_('Level info'), {'fields': ('initial_level', 'max_level',)}),
        (_('Rates'), {'fields': ('rates',),}),
        (_('Imagenes'), {'fields': ('images',),}),
        (_('Facebook'), {'fields': ('facebook_url', 'facebook_enable')}),
        (_('Footer info'), {'fields': ('footer_menu_enable', 'footer_menu', 'footer_info_enable', 'footer_info',)}),
        (_('Foro'), {'fields': ('forum_url',)}),
        (_('Ultimos 24 horas'), {'fields': ('last_online',)}),
    )

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'types')


admin.site.register(Site, SiteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Download, DownloadAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(Token, TokenAdmin)
