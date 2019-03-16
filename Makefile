image_name=e-ink-dash
test_cmd="python dash_tests.py && python integration_tests.py && node generate_diff.js"

build:
	docker build . -t $(image_name)

test:
	docker run -it --rm -v $(shell pwd):/home/app -w /home/app $(image_name) /bin/sh -c $(test_cmd) && open diff.png

.PHONY: build test
