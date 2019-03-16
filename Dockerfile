FROM python:3.7.2-alpine3.9

# Install dependencies for Pillow, as well as install node and npm
RUN apk update && apk add build-base zlib-dev jpeg-dev freetype-dev nodejs nodejs-npm

# Pillow is needed to generate the image in python
RUN pip install Pillow

# Pixelmatch is just a test-time dependency
RUN npm install --global pixelmatch@4.0.2

CMD ["/bin/bash"]
