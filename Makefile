# Basic commands
build:
	export COMPOSE_FILE=docker-compose-dev.yml; docker-compose build

run:
	export COMPOSE_FILE=docker-compose-dev.yml; docker-compose up

purge:
	export COMPOSE_FILE=docker-compose-dev.yml; docker-compose down

# Dev commands
shell:
	export COMPOSE_FILE=docker-compose-dev.yml; docker-compose run --rm django python manage.py shell

enter:
	export COMPOSE_FILE=docker-compose-dev.yml; docker-compose run --rm django sh

# Production commands

build-prod:
	export COMPOSE_FILE=docker-compose-prod.yml; docker-compose build

run-prod:
	export COMPOSE_FILE=docker-compose-prod.yml; docker-compose up


