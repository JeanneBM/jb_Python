FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install PyYAML pytest

WORKDIR /script

COPY hello.py /script/hello.py

ENV NAME="User"

CMD ["python3", "/script/hello.py"]
