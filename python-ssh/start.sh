#!/bin/bash

# Старт SSH-сервера
/usr/sbin/sshd -D

chmod -R 775 /app
chown -R python-root:root /app
