## Docker

Docker：Build，Ship and Run Any App,Anywhere

根据镜像image创建容器container，同一个image可以创建多个container

dockerfile ---build-->image--run-->container

```
# 启动
systemctl start docker 

docker version 

docker --help
```

## Image

```
# 列出本地主机镜像
docker images 
-a, --all             Show all images (default hides intermediate images)
--digests         Show digests
-f, --filter filter   Filter output based on conditions provided
--format string   Pretty-print images using a Go template
--no-trunc        Don't truncate output
-q, --quiet           Only show numeric IDs


docker search <image_name>
docker pull <image_name> [:TAG]  # TAG默认为 last 
docker rmi <image_id> 或 <image_name>  # 删除镜像
docker rmi -f $(docker images -qa) # 删除所有镜像


docker run [options]  IMAGE [COMMAND]   # 新建并启动容器
--name="容器新名字": 为容器指定一个名称；
-d: 后台运行容器，并返回容器ID，也即启动守护式容器；
-i：以交互模式运行容器，通常与 -t 同时使用；
-t：为容器重新分配一个伪输入终端，通常与 -i 同时使用；
-P: 随机端口映射；
-p: 指定端口映射，有以下四种格式
      ip:hostPort:containerPort
      ip::containerPort
      hostPort:containerPort
      containerPort
-e, --env list                       Set environment variables

```

## Container

```
 docker ps [OPTIONS]  # 列出当前所有正在运行的容器
-a : 列出当前所有正在运行的容器+历史上运行过的
-l : 显示最近创建的容器。
-n：显示最近n个创建的容器。
-q :静默模式，只显示容器编号。
--no-trunc :不截断输出。


exit  # 容器停止退出
ctrl + P + Q # 容器不停止退出

docker start  ＜container id＞   或＜container name＞ # 启动容器
docker restart ＜container id＞ 或＜container name＞
docker stop ＜container id＞或＜container name＞ # 停止容器（关机）
docker kill ＜container id＞ 或＜container name＞  # 强制停止容器（拔电源）
docker rm ＜container id＞ # 删除已停止的容器
# 一次性删除多个容器 
docker rm -f $(docker ps -a -q) 
docker ps -a | xargs docker rm

docker attach ＜container id＞ # 重新进入后台容器
docker exec -it ＜container id＞   # 进入正在运行的容器并以命令交互
```

