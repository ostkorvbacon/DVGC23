FROM ubuntu:latest

RUN qpt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
    python3 \
    python3-pip \
    make

# RUN pip3 isntall -U pytest

# ADD run_tests.sh .

CMD ["./run_tests.sh"]