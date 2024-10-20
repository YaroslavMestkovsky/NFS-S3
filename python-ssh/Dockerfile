FROM python:3.6.9

# Устанавливаем переменную среды для вывода Python без буферизации
#ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости системы
RUN apt-get update
RUN apt-get install -y postgresql-client
RUN apt-get install -y libffi-dev
RUN apt-get install -y libjpeg-dev
RUN apt-get install -y libfreetype6-dev
RUN apt-get install -y libjpeg-turbo-progs
RUN apt-get install -y libpng-dev
RUN apt-get install -y curl
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libxslt1-dev
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y build-essential
RUN apt-get install -y gcc
RUN apt-get install -y libc-dev
RUN apt-get install -y linux-headers-amd64
RUN apt-get install -y postgresql-server-dev-all

# Опциональная временная установка компиляторов и библиотек для сборки
RUN apt-get install -y --no-install-recommends g++ musl-dev

# Очистка кеша apt-get для уменьшения размера образа
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# OpenSSH сервер
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# Пользователь и sudo
RUN useradd -rm -d /home/python-root -s /bin/bash -g root -G sudo -u 1001 python-root && \
    echo 'python-root:python-root' | chpasswd

# Настройка Python окружения
COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip  \
    && pip3 install -r ./requirements.txt
ENV PYTHONUNBUFFERED 1
## SSH порт
EXPOSE 22
