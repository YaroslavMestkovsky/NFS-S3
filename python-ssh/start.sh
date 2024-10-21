#!/bash

chmod -R 775 /app
chown -R python-root:root /app

echo 'mounting NFS-folder...'
# Ждем, пока заведется NFS-сервер
sleep 3
mount -o nolock,proto=tcp nfs-server:/export/data /mnt/nfs-share
# Проверяем, что папка смонтировалась
df -h | grep "nfs-server"
echo 'done.'

# Старт SSH-сервера
echo 'starting SSH-server...'
echo 'done' # Детач же, ну ¯\_(ツ)_/¯
/usr/sbin/sshd -D
