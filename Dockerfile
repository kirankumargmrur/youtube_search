FROM python:3.9
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y software-properties-common
RUN apt-get install -y python3-pip libpq-dev python-dev python3-setuptools
RUN python3 -m pip install pip
RUN python3 -m pip install setuptools-rust
ENV PYTHONUNBUFFERED 1
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN python3 -m pip install -r requirements.txt