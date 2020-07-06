.DEFAULT_GOAL := help
DOCKERFILE=docker-compose.dev.yml

dc-build:
	docker-compose -f $(DOCKERFILE) build

dc-up:
	docker-compose -f $(DOCKERFILE) up

# API Service
dc-api-up:
	docker-compose -f $(DOCKERFILE) up api

dc-api-build:
	docker-compose -f $(DOCKERFILE) build api

dc-api-makemigrations:
	docker-compose -f $(DOCKERFILE) run api python manage.py makemigrations

dc-api-migrate:
	docker-compose -f $(DOCKERFILE) run api python manage.py migrate

dc-api-test:
	docker-compose -f $(DOCKERFILE) run api pytest

# MIX makemigrations and migrate command
dc-api-makeandmigrate: dc-api-makemigrations dc-api-migrate

dc-api-createsuperuser:
	docker-compose -f $(DOCKERFILE) run api python manage.py createsuperuser

dc-api-exec:
	docker-compose -f $(DOCKERFILE) exec api /bin/bash