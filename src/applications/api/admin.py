from django.contrib import admin

# Locals Models
from .models import Download


class DownloadAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'weight', 'link', 'published', 'create_at', 'modified_at')
    search_fields = ['provider']
    

admin.site.register(Download, DownloadAdmin)
