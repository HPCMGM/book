# 1. docker安装

```shell
docker run \
    --detach \
    --publish 443:443 \
    --publish 80:80 \
    --name gitlab \
    --restart unless-stopped \
    -v /home/hpcm/gitlab/etc:/etc/gitlab \
    -v /home/hpcm/gitlab/log:/var/log/gitlab \
    -v /home/hpcm/gitlab/data:/var/opt/gitlab \
    beginor/gitlab-ce:11.0.1-ce.0
```

