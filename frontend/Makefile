name := appname-frontend
tag := 0.0.1
pwd := $(shell pwd)

docker-run-cmd := docker run --name ${name}-dev --rm -it -p 8080:8080 -v ${pwd}/app:/src -w /src node:alpine
docker-cmd := docker run --rm -it -v ${pwd}/app:/src -w /src node:alpine

fake:
	docker build . -t ${name}:${tag}-local
	docker build . -t ${name}:${tag}-dev

default: install build

dist: build-dev build

install:
	${docker-cmd} npm install

build:
	${docker-cmd} npm run build
	docker build . -t ${name}:${tag}-local

build-dev:
	${docker-cmd} npm run build-dev
	docker build . -t ${name}:${tag}-dev

#build-live:
#	${docker-cmd} npm run build-live
#	docker build . -t ${name}:${tag}-live

dev:
	${docker-run-cmd} npm run dev

push:
	docker push ${name}:${tag}-dev
	#docker push ${name}:${tag}-live

ls:
	docker images ${name}
