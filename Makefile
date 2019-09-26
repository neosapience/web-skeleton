docker-compose-test := docker-compose -f docker-compose.yml -f docker-compose.prod.yml

up:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

test:
	@docker-compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.test.yml up -d

logs:
	@docker-compose logs -f api

down:
	@docker-compose down

stop:
	@docker-compose stop ${service}

ps:
	@docker-compose ps

build:
	@make -C api build
	@make -C frontend build

dist:
	@make -C api build-dist
	@make -C frontend build-dist

push:
	@make -C api push
	@make -C frontend push

ls:
	@make -C api ls
	@make -C frontend ls
