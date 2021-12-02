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


#RUN apt-get -y install tzdata

RUN apt-get update && apt-get install -y \
    linux-headers-virtual usbutils kmod udev libxml2-dev libxml2-dev libssl-dev zlib1g-dev && \
    export KDIR="/lib/modules/*-generic/build"

# från volvo
# https://www.kvaser.com/download/?utm_source=software&utm_ean=7330130980754&utm_status=latest
# https://www.kvaser.com/download/?utm_source=software&utm_ean=7330130981966&utm_status=latest
# RUN apt-get update && apt-get install -y \
#     linux-headers-virtual usbutils kmod udev libxml2-dev && \
#     export KDIR="/lib/modules/*-generic/build" && \
#     wget --content-disposition "https://www.kvaser.com/download/?utm_source=software&utm_ean=7330130980754&utm_status=latest" && \
#     tar xzf linuxcan.tar.gz && \
#     make -C linuxcan all install && \
#     rm -r linuxcan && rm linuxcan.tar.gz && \
#     wget --content-disposition "https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130981966&utm_status=latest" && \
#     tar xzf kvlibsdk.tar.gz && \
#     make -C kvlibsdk all install && \
#     rm -r kvlibsdk && rm kvlibsdk.tar.gz


# "https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130980754&utm_status=latest"
# "https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130981966&utm_status=latest"

RUN wget --content-disposition "https://www.kvaser.com/download/?utm_source=software&utm_ean=7330130980754&utm_status=latest" \ 
   && tar xf linuxcan.tar.gz \
   && cd linuxcan \
   && make \
   && make install



# RUN cd linuxcan/canlib/examples && \
#     ./listChannels

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

# RUN cd linuxcan \
#     && make install \
#     && cd virtualcan \
#     && ./virtualcan.sh \
#     && cd /usr/doc/canlib/examples \
#     && ./listChannels

# RUN modprobe virtualcan \
#     && python3 canfault/main.py

# ADD run_tests.sh .

CMD ["/bin/bash"]