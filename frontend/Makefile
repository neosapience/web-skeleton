name := neosapience/appname-ui
tag := 0.0.1
pwd := $(shell pwd)

docker-run-cmd := docker run --name ${name}-dev --rm -it -p 8080:8080 -v ${pwd}/app:/src -w /src node:alpine
docker-cmd := docker run --rm -it -v ${pwd}/app:/src -w /src node:alpine

default: install build

node-install:
	${docker-cmd} npm install

node-build:
	${docker-cmd} npm run build

build:
	docker build . -t ${name}:dev

build-dist:
	docker build . -t ${name}:${tag}

dev:
	${docker-run-cmd} npm run dev

push:
	docker push ${name}:${tag}

ls:
	docker images ${name}
