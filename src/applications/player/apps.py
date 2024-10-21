"""
    Esta APP se usa basicamente de router, y gracias a esta nos podemos conectar
    a la base de datos de metin2 para registrar cuentas, extraer datos y mostrarlos.
"""
from django.apps import AppConfig


class PlayerConfig(AppConfig):
    """
        Player config
    """
    name = "player"
