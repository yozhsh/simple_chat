.DEFAULT_GOAL := help
DOCKERFILE=docker-compose.dev.yml

dc-build:
	docker-compose -f $(DOCKERFILE) build

dc-up:
	docker-compose -f $(DOCKERFILE) up

dc-up-api:
	docker-compose -f $(DOCKERFILE) up api

dc-build-api:
	docker-compose -f $(DOCKERFILE) build api
