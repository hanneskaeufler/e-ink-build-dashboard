image_name=e-ink-dash
test_cmd="python dash_tests.py && python integration_tests.py && pixelmatch expected.png actual.png diff.png"
docker_run=docker run -it --rm -v $(shell pwd):/home/app -w /home/app $(image_name)-dev

# Can be overridden
TAG:=latest
REPO:=hanneskaeufler

push:
	docker push $(REPO)/$(image_name):$(TAG)

build:
	docker build . -t $(REPO)/$(image_name):$(TAG)

build-dev:
	docker build . -f Dockerfile.dev -t $(image_name)-dev

check-code-style:
	$(docker_run) pycodestyle .

fix-code-style:
	$(docker_run) autopep8 --in-place --recursive .

ci: check-code-style test

test:
	$(docker_run) /bin/sh -c $(test_cmd)

test-coverage:
	$(docker_run) /bin/sh -c "coverage run --source=. --omit=*_tests.py dash_tests.py && coverage report && coverage xml"

.PHONY: build build-dev test ci push check-code-style fix-code-style
