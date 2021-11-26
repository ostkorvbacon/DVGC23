FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
    python3 \
    python3-pip \
    build-essential \
    wget \
    usbutils

RUN wget --content-disposition "https://www.kvaser.com/downloads-kvaser/?utm_source=software&utm_ean=7330130980754&utm_status=latest" \ 
    && tar xf linuxcan.tar.gz \
    && cd linuxcan \
    && make \
    && make install

# ADD run_tests.sh .

CMD ["/bin/bash"]