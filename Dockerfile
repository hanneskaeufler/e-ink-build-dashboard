FROM arm32v7/python:2.7.16-alpine3.9

RUN apk add build-base linux-headers git zlib-dev jpeg-dev freetype-dev tzdata
RUN rm -rf /var/cache/apk/*

RUN mkdir /home/build

RUN cd /home/build \
    && git clone https://github.com/lthiery/SPI-Py.git \
    && cd SPI-Py && python setup.py install

RUN pip install rpi.gpio spidev Pillow python-dotenv enum34

# Setup app
COPY dash.py fetch_build_status.py epdif.py epd7in5.py main.py /home/app/
COPY run.sh /home/app/
COPY fontawesome /home/app/fontawesome
COPY lato /home/app/lato

# Setup cron
COPY crontab /etc/cron.d/e-ink-dash
RUN chmod 0644 /etc/cron.d/e-ink-dash && crontab /etc/cron.d/e-ink-dash
RUN touch /var/log/cron.log

ENV DASH_FONTS_DIR=/home/app
ENV TZ=Europe/Berlin

WORKDIR "/home/app"

CMD ["sh", "run.sh"]
