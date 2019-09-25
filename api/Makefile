project := appname
name := ${project}-api
tag := 0.0.1
pwd := $(shell pwd)


build:
	@docker build . -t ${name}:dev

build-tag:
	@docker build . -t ${name}:${tag}

ls:
	@docker images ${name}

h:
	@docker history ${name}:dev

push:
	@docker push ${name}:${tag}
