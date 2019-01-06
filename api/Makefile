project := appname
name := ${project}-api
tag := 0.0.1
pwd := $(shell pwd)


build:
	@docker build . -t ${name}:${tag}

dev:
	@docker run --rm -it \
		--name ${name} \
		--network ${project}_backend \
		-v ${pwd}:/code \
		-v ${pwd}/../secrets/api_secret_dev:/run/secrets/api_secret \
		-p 5000:5000 \
		-e SECRET_KEY_FILE=/run/secrets/api_secret \
		${name}:${tag}

test:
	@docker run --rm -it \
		--name ${name} \
		--network ${project}_backend \
		-v ${pwd}:/code \
		-v ${pwd}/../secrets/api_secret_dev:/run/secrets/api_secret \
		-e SECRET_KEY_FILE=/run/secrets/api_secret \
		${name}:${tag} \
		pytest

ls:
	@docker images ${name}

h:
	@docker history ${name}:${tag}

push:
	@docker push ${name}:${tag}
