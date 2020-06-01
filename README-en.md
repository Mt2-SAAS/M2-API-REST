[![Build Status](https://travis-ci.org/luisito666/Mt2Web.py-V2.svg?branch=develop)](https://travis-ci.org/luisito666/Mt2Web.py-V2)

[Español](README.md) ∙ *[English](README-en.md) 

# Mt2Web.py-V2

New generatios of Web's for Metin2 PServer

## Motivation.

The main goal of this project is get a Metin2 Web page with the last standars of the web development industry, and a code easy to read and mantain.

## Caracteristicas principales.

1. Made with python and django.
2. Implements docker for development and production environment.
3. Implements redis and celery for async task and schedule task.
4. Easy to configurate thanks to yaml format.
5. Advanced security


## Requirements.

1. git
2. docker
3. docker compose
4. make
5. Operatin system like Linux (Ubuntu, Centos etc..), Mac OS

## How to Install?

```
git clone git@github.com:luisito666/Mt2Web.py-V2.git
cd Mt2Web.py/
make build
```

## ¿How to Start?

Before of start this projects is recomended edit the config.yml file and add the correct parameters.

the file is locate in the next path 'src/config.yml'

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

After to this run the startup command.

```
make run
```

Nota: the previous command run the project in development environment.

### Run production mode

```
make run-prod
```

Nota: this command is recomend to run the project in the production envionment
