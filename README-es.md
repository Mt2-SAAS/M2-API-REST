[![Build Status](https://travis-ci.org/luisito666/Mt2Web.py-V2.svg?branch=develop)](https://travis-ci.org/luisito666/Mt2Web.py-V2)

[English](README-en.md) ∙ *[Español](README.md) 

# Mt2Web.py-V2

Backend para el proyecto [M2Frontend](https://github.com/luisito666/M2Frontend)

## Motivación.

El objetivo principal de este proyecto es proporcionar una forma rápida de implementar servicios para Servidores Privados de Metin2.

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

Antes de iniciar el proyecto es necesario editar el archivo config.yml y agregar los parametros necesarios para el funcionamiento.

el archivo se encuentra en la siguiente ruta 'src/config.yml'

```
database:
  user: root
  password: 'tu_pasword'
  host: 0.0.0.0
  port: 3306
server:
  name: 'Metin2 XxX'
  url: 'https://www.example.com'
  domain: 'example.com'
  timezone: 'America/Bogota'
paymentwall:
  public_key: ''
  private_key: ''
captcha:
  enable: False
  public_key: ''
  private_key: ''
mail:
  host: 0.0.0.0
  port: 25
  password: 'tu_pasword'
  user: 'tu_usuario@example.com'
register:
  mail_activate_account: False
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
