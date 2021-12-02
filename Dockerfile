FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
    linux-headers-`uname -r` \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    wget \
    usbutils \
    kmod \
    tzdata

RUN apt-get update && apt-get install -y \
    linux-headers-virtual usbutils kmod udev libxml2-dev libxml2-dev libssl-dev zlib1g-dev && \
    export KDIR="/lib/modules/*-generic/build"

RUN wget --content-disposition "https://www.kvaser.com/download/?utm_source=software&utm_ean=7330130980754&utm_status=latest" \ 
   && tar xf linuxcan.tar.gz \
   && cd linuxcan \
   && make \
   && make install

RUN wget --content-disposition "https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130981966&utm_status=latest" \
    && tar xf kvlibsdk.tar.gz \
    && cd kvlibsdk \
    && make \
    && make install

RUN apt-get update && apt-get install -y \
    unzip \
    && wget --content-disposition "https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130981911&utm_status=latest" \
    && unzip -q pycanlib.zip \
    && cd pycanlib \
    && pip install canlib-*.whl

RUN pip install --upgrade pip && \
    pip install bitarray \
    && pip install coverage

ADD canfault canfault

WORKDIR /canfault

CMD ["/bin/sh", "run.sh"]