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
		-p 5000:5000 \
		${name}:${tag}

test:
	@docker run --rm -it \
		--name ${name} \
		--network ${project}_backend \
		-v ${pwd}:/code \
		-p 5000:5000 \
		${name}:${tag} \
		python -m unittest discover 

ls:
	@docker images ${name}

h:
	@docker history ${name}:${tag}

push:
	@docker push ${name}:${tag}
