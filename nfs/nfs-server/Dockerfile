FROM ubuntu:latest

# Серверные утилиты NFS
RUN apt-get update
RUN apt-get install -y nfs-kernel-server

# Настройка конфига для экспорта директории
RUN echo "/export/data *(rw,sync,no_subtree_check,insecure)" > /etc/exports
