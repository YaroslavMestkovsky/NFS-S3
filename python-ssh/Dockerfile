FROM python:3.10-slim

# OpenSSH сервер
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# Пользователь и sudo
RUN useradd -rm -d /home/python-root -s /bin/bash -g root -G sudo -u 1001 python-root && \
    echo 'python-root:python-root' | chpasswd

# Вход по SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config

# Настройка Python окружения
COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip  \
    && pip3 install -r ./requirements.txt

# SSH порт
EXPOSE 22

# Запуск SSH при старте контейнера
CMD ["/usr/sbin/sshd", "-D"]
