[![Build Status](https://travis-ci.org/luisito666/Mt2Web.py-V2.svg?branch=develop)](https://travis-ci.org/luisito666/Mt2Web.py-V2)

*[Español](README.md) ∙ [English](README-en.md) 

# Mt2Web.py-V2

Nueva generacion de web's para servidores de metin2

## Motivación.

La principal motivación que da surgimiento a este proyecto, es tener una web de Metin2 con los estándares actualizados, un código limpio y fácil de leer y mantener.

## Caracteristicas principales.

1. Hecha en python con ayuda de un framework llamado Django.
2. Implementacion de Docker y Docker Compose para la automatización del despliegue.
3. Implementacion de redis y celery para tareas programadas.
4. Facil configuracion con ayuda del formato yaml.
5. Seguridad avanzada.

## Requerimientos.

1. git
2. docker
3. docker compose
4. make
5. Sistema operativo Linux (Ubuntu, Centos etc..), Mac OS

## ¿Como instalar?

```
git clone git@github.com:luisito666/Mt2Web.py-V2.git
cd Mt2Web.py/
make build
```

## ¿Como Iniciar?

Antes de iniciar el proyecto es necesario editar el archivo config.yml y agregar los parametros necesarios para el funcionamiento.

el archivo se encuentra en la siguiente ruta 'src/config.yml'

```
database:
  user: root
  password: 
  host: 
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

Nota: Es recomendado usar este comando cuando vamos a montar la pagina para su uso.

