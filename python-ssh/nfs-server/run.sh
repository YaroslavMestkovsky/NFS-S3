#!/bin/bash

# Старт служб NFS-сервера
echo 'starting daemon...'
/usr/sbin/rpcbind
/etc/init.d/nfs-kernel-server start

tail -f /dev/null
