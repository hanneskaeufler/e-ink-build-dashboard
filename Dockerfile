FROM arm32v7/python:2.7.16-alpine3.9

RUN apk add build-base linux-headers git zlib-dev jpeg-dev freetype-dev

RUN mkdir /home/build

RUN cd /home/build \
    && git clone https://github.com/lthiery/SPI-Py.git \
    && cd SPI-Py && python setup.py install

RUN pip install rpi.gpio spidev Pillow python-dotenv enum34

COPY dash.py fetch_build_status.py epdif.py epd7in5.py main.py /home/app/
COPY fontawesome /home/app/fontawesome
COPY lato /home/app/lato

ENV DASH_FONTS_DIR=/home/app

WORKDIR "/home/app"

CMD ["python", "main.py"]
