[![Build Status](https://travis-ci.org/luisito666/Mt2Web.py-V2.svg?branch=develop)](https://travis-ci.org/luisito666/Mt2Web.py-V2)

[English](README.md) ∙ *[Español](README-es.md) 

# Mt2Web.py-V2

WebServices (Backend) Para exponer REST APIs de Juegos Online.

## Motivación.

El objetivo principal de este proyecto es proporcionar una API para la creacion de paginas web para PServers

## Ventajas.

1. Hecha en python.
2. Rapida implementacion de entornos de desarrollo y producion
3. Facil de configurar donaciones gracias a PaymentWall
4. Facil configuracion con ayuda del formato yaml.
5. Seguridad avanzada.

## Requerimientos.

1. git
2. docker
3. docker compose
4. make
5. Sistema operativo Linux (Ubuntu, Centos etc..), Mac OS, Windows 10

## ¿Como instalar?

```
git clone git@github.com:New-Blod-Team/M2-API-REST.git
cd M2-API-REST/
make build
```

## ¿Como Iniciar?

Antes de iniciar el proyecto es necesario editar el archivo de configuracion y agregar los parametros necesarios para el funcionamiento.
el archivo se encuentra en la siguiente ruta.

Hay dos archivos, uno para produccion y otro para desarrollo.

Desarrollo '.environment/development/.django'

Produccion '.environment/production/.django'

```
# Env File For APP

# Database Config
DATABASE_USER=root
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=3306

# Server Config
SERVER_NAME="Metin2 XxX"
SERVER_URL=https://wwww.example.com
SERVER_DOMAIN=example.com
SERVER_TIMEZONE=America/Bogota
SERVER_SECRET=some-secret-please_change
SERVER_LOCALADDR=

# PaymentWall Config
PAYMENTWALL_PUBLIC=
PAYMENTWALL_PRIVATE=

# Email Config
MAIL_HOST=
MAIL_PORT=25
MAIL_PASSWORD=
MAIL_USER=
MAIL_SEND_ACTIVATION=0

# Cors Config
CORS_ORIGIN_ALLOW=
```

Despues de lo anterior se ejecuta este comando para iniciar el proyecto.

```
make run
```

Nota: El comando anterior ejecutar el proyecto en modo desarrollador.

### Iniciar modo produccion.

```
make run-prod
```

Nota: Es recomendado usar este comando cuando vamos a usar el servicio en producion.
