name := neosapience/appname-api
tag := v0.0.1
pwd := $(shell pwd)


build:
	@docker build . -t ${name}:dev --build-arg MYAPP_API_VERSION=${name}:dev

build-dist:
	@docker build . -t ${name}:${tag} --build-arg MYAPP_API_VERSION=${name}:${tag}

ls:
	@docker images ${name}

h:
	@docker history ${name}:dev

push:
	@docker push ${name}:${tag}
