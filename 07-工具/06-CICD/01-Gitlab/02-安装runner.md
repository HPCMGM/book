# 1. docker安装

```shell
docker run -d --name gitlab-runner -p 8043:8043 --restart always \
  -v /home/hpcm/gitlab-runner/config:/etc/gitlab-runner \
  -v /home/hpcm/gitlab-runner/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

