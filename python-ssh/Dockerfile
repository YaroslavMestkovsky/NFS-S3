FROM python:3.6.9

# OpenSSH сервер
RUN apt-get update && \
    apt-get install -y openssh-server nfs-common && \
    mkdir /var/run/sshd && \
    mkdir -p /mnt/nfs-share

# Пользователь и sudo
RUN useradd -rm -d /home/python-root -s /bin/bash -g root -G sudo -u 1001 python-root && \
    echo 'python-root:python-root' | chpasswd

# Настройка Python окружения
COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip  \
    && pip3 install -r ./requirements.txt

## SSH порт
EXPOSE 22
