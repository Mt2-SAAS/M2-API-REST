from datetime import timezone
from django.db import models
from core.models import Base

# Translation
from django.utils.translation import gettext_lazy as _


IMAGE_LOGO = 'logo'
IMAGE_BG = 'background'


class Image(Base):
    IMAGE_TYPE = (
        (IMAGE_LOGO, _('Logo')),
        (IMAGE_BG, _('Imagen Fondo')),
    )
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/upload')
    types = models.CharField(max_length=20, choices=IMAGE_TYPE)


    def __str__(self):
        return f'<Image ({self.name})>'

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'


class Site(Base):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    images = models.ManyToManyField(Image)
    initial_level = models.CharField(max_length=10)
    max_level = models.CharField(max_length=10)
    rates = models.CharField(max_length=255)
    facebook_url = models.CharField(max_length=255)
    facebook_enable = models.BooleanField(default=False)
    footer_menu = models.ManyToManyField('Pages')
    footer_info = models.CharField(max_length=255)
    footer_menu_enable = models.BooleanField(default=False)
    footer_info_enable = models.BooleanField(default=False)
    forum_url = models.CharField(max_length=255)
    last_online = models.BooleanField(default=False)

    def __str__(self):
        return f'<Site ({self.slug})>'

    class Meta:
        verbose_name = 'Sitio'
        verbose_name_plural = 'Sitios'   
