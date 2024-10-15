#!/bin/bash

# Ждем, пока заведется сервер
echo 'sleep 3...'
sleep 3
# Монтируем папку с сервера
mount -o nolock,proto=tcp nfs-server:/export/data /mnt/nfs-share

# Проверяем, что папка смонтировалась
df -h | grep "nfs-server"

tail -f /dev/null
