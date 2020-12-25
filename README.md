[![Build Status](https://travis-ci.org/luisito666/Mt2Web.py-V2.svg?branch=develop)](https://travis-ci.org/luisito666/Mt2Web.py-V2)

*[English](README-en.md) ∙ [Español](README.md)   

# Mt2Web.py-V2

Backend for the project [M2Frontend](https://github.com/luisito666/M2Frontend)

## Motivation.

The main goal of this project is provide a rapid way to implements services for Metin2 PServers.

## Advantage

1. Made with python.
2. Rapid deployment for development and production
3. Easy way to configure donations with paymentwall
4. Easy to configurate thanks to yaml format.
5. Advanced security


## Requirements.

1. git
2. docker
3. docker compose
4. make
5. Operatin system like Linux (Ubuntu, Centos etc..), Mac OS, Windows 10.

## How to Install?

```
git clone git@github.com:New-Blod-Team/M2-API-REST.git
cd M2-API-REST/
make build
```

## ¿How to Start?

Before of start this projects is recomended edit the config.yml file and add the correct parameters.

the file is locate in the next path 'src/config.yml'

```
database:
  user: root
  password: 'your_db_pasword'
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
