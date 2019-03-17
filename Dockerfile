FROM arm32v7/python:3.7.2-alpine3.9

RUN apk add build-base git sudo bash

# Install gpio
RUN cd /home \
    && git clone git://git.drogon.net/wiringPi \
    && cd wiringPi \
    && ./build \
    && gpio -v

# ADD http://www.airspayce.com/mikem/bcm2835/bcm2835-1.45.tar.gz /home
# RUN cd /home && tar --extract --file=/home/bcm2835-1.45.tar.gz
# RUN cd /home/bcm2835-1.45 && ./configure && make && make check; cat ./src/test-suite.log # make install

# Install python bindings for linux spi access
# RUN pip install spidev

# COPY dash.py fetch_build_status.py main.py epd7in5.py epdif.py /home/app/

CMD ["/bin/sh", "echo 'lol'"]
