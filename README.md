[![Build Status](https://travis-ci.org/luisito666/Mt2Web.py-V2.svg?branch=develop)](https://travis-ci.org/luisito666/Mt2Web.py-V2)

*[English](README.md) ∙ [Español](README-es.md)   

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

Before starting the project, it is necessary to edit the configuration file and add the necessary parameters for operation.
the file is in the following path.

There are two files, one for production and one for development.

Development '.environment/development/.django'

Production '.environment/production/.django'

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
