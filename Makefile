docker-compose-dev := docker-compose -f docker-compose.yml -f docker-compose.dev.yml
docker-compose-prod := docker-compose -f docker-compose.yml -f docker-compose.prod.yml

up:
	@${docker-compose-dev} up -d

down:
	@${docker-compose-dev} down

stop:
	@${docker-compose-dev} stop ${service}

ps:
	@${docker-compose-dev} ps

deploy:
	@${docker-compose-prod} config > deploy.yml

build:
	@make -C api build
	@make -C frontend fake

push:
	@make -C api push
	@make -C frontend push

ls:
	@make -C api ls
	@make -C frontend ls
