## Docker

Docker：Build，Ship and Run Any App,Anywhere. 将环境进行打包,从而做到一次封装，到处运行

根据镜像image创建容器container，同一个image可以创建多个container

dockerfile ---build-->image--run-->container

```
# 安装
yum install -y docker

# 启动
systemctl start docker 

docker version 

docker --help
```

## Image

镜像是一种轻量级、可执行的独立软件包，用来**打包软件运行环境**和**基于运行环境开发的软件**，它包含运行某个软件所需的所有内容，包括代码、运行时、库、环境变量和配置文件。

```shell
# 列出本地主机镜像
docker images [options]
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

```

## Container

镜像image的实例

```shell
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


 docker ps [OPTIONS]  # 列出当前所有正在运行的容器
-a : 列出当前所有正在运行的容器+历史上运行过的
-l : 显示最近创建的容器。
-n：显示最近n个创建的容器。
-q :静默模式，只显示容器编号。
--no-trunc :不截断输出。




docker start  ＜container id＞   或＜container name＞ # 启动容器
docker restart ＜container id＞ 或＜container name＞
docker stop ＜container id＞或＜container name＞ # 停止容器（关机）
docker kill ＜container id＞ 或＜container name＞  # 强制停止容器（拔电源）
docker rm ＜container id＞ # 删除已停止的容器
# 一次性删除多个容器 
docker rm -f $(docker ps -a -q) 
docker ps -a | xargs docker rm

docker inspect  ＜container id＞ ----------------- 查看容器内部细节
docker attach ＜container id＞ # 直接进入容器启动命令的终端，不会启动新的进程
docker exec -it ＜container id＞   # 进入正在运行的容器并以命令交互,在容器中打开新的终端，并且可以启动新的进程
exit  # 容器停止退出
ctrl + P + Q # 容器不停止退出
docker cp  容器ID:容器内路径  目的主机路径  -------------- 从容器中拷贝文件到目的主机
docker cp  目的主机路径  容器ID:容器内路径 -------------- 从目的主机拷贝文件到容器中

```

##  DataVolume

有时候我们希望容器产生的数据也能持久化, 我们可以docker commit生成新的镜像从而进行持久化. 但是有时候我们只希望保存数据, 所以我们使用卷（Volume）

```shell
docker run -it -v 宿主机绝对路径目录:容器内目录   镜像名
docker inspect   <container id>  查看是否挂载成功  

[root@localhost /]# docker run -it -v /myDataVolume:/dataVolumeContainer centos
[root@localhost /]# docker inspect 1dc3fa167441

....
"Binds": [
                "/myDataVolume:/dataVolumeContainer"
            ],
....

```

##  Dockerfile

Dockerfile是用来构建Docker镜像的构建文件