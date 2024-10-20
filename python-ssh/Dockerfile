#FROM python:3.10-slim
#
## OpenSSH сервер
#RUN apt-get update && \
#    apt-get install -y openssh-server && \
#    mkdir /var/run/sshd
#
## Пользователь и sudo
#RUN useradd -rm -d /home/python-root -s /bin/bash -g root -G sudo -u 1001 python-root && \
#    echo 'python-root:python-root' | chpasswd
#
## Вход по SSH
#RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
#    echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config
#
## Настройка Python окружения
#COPY requirements.txt ./requirements.txt
#RUN pip3 install --upgrade pip  \
#    && pip3 install -r ./requirements.txt
#
## SSH порт
#EXPOSE 22

FROM python:3.7.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache postgresql-client python3-dev \
  libffi-dev jpeg-dev freetype-dev libjpeg-turbo-dev libpng-dev \
  curl libxml2-dev libxslt-dev libstdc++
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
  g++

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
