image_name=e-ink-dash
test_cmd="python dash_tests.py && python integration_tests.py && node generate_diff.js"
docker_run=docker run -it --rm -v $(shell pwd):/home/app -w /home/app $(image_name)-dev

# Can be overridden
TAG:=latest
REPO:=hanneskaeufler

push:
	docker push $(REPO)/$(image_name):$(TAG)

build:
	docker build . -t $(REPO)/$(image_name):$(TAG)

build-dev:
	docker build . -t $(image_name)-dev

code-style:
	$(docker_run) pycodestyle .

test: code-style
	$(docker_run) /bin/sh -c $(test_cmd) && open diff.png

.PHONY: build build-dev test
