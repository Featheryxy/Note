```shell
[milo@localhost ~]$
[当前用户名@主机名 目前所在目录] 提示字符

~   当前用户目录
/   根目录
#   root用户提示符, 超级用户权限
$   一般用户提示符


```



### 联网

虚拟机设置为NAT模式

>  NAT使用VMnet8网卡，当主机通网时，该机也可通网。默认情况下和物理机同一网络中的其它机器不能访问虚拟机，但虚拟机可以访问其它物理机。可以修改NAT设置，添加主机IP：主机端口与虚拟机IP: 虚拟机端口

如果`ip addr `无网卡信息, 则修改/etc/sysconfig/network-scripts/ifcfg-ens33文件, 将ONBOOT设置为yes 来启动网卡

### 帮助命令

```shell
man [-k] [命令或配置文件] # manual, 命令的具体参数及使用方法
-k 只记得部分命令关键字的场合，我们可通过man -k来搜索

whatis [命令] # 简要说明
info [命令] # 详细的介绍
which [命令] # 命令在哪个位置

```



###  yum

```shell 
yum [option] [查询工作项目] [相关参数]

[option]
-y: 自动yes
--installroot=/some/path: 自定义安装路径

[查询工作项目] [相关参数]
search:
list: 列出yum服务器上提供的所有软件 rpm -qa
info: 查看软件功能 rpm -qai
install:
update:
remove: 卸载

yum list updates: 列出可升级的软件
yum list isntalled: 列出已安装的软件
```

### 目录

```shell
mkdir [目录名]：make directories
rmdir [目录名]: remove empty directories
mv [原文件或目录] [目标目录]: 剪切文件、改名


cp [原文件或目录] [目标目录]: 复制文件或目录
-r 复制目录
-p 保留文件属性（文件最后一次的修改时间）
    
rm: make directories or file
-r 就是向下递归，不管有多少级目录，一并删除
-f 就是直接强行删除，不作任何提示的意思
rm -rf: 删除文件夹及下面所有文件
```



### tar

```shell
压缩：tar [-z-j-J][cv] [-f 待建立的文件名]
查询：tar [-z-j-J][tv] [-f 已有的文件名]
解压缩：tar [-z-j-J][xv] [-f 已有的文件名] [-C 解压到指定目录]

-c 打包
-x 解包
-t 查看文件的内容

-v 显示详细信息
-f 指定解压文件
-C 解压到指定目录

-z 通过gzip解压缩:*.tar.gz
-j 通过bzip2解压缩:*.tar.bz2
-J 通过xz解压缩:*.tar.xz
ps：-z-j-J只能使用一个


```



###  常用

```shell
空格 翻页
q   退出

回车 一行一行浏览
Ctrl + f 键 （f 的英文全拼为：forward）下一页
Ctrl + b 键 （b 的英文全拼为：backward) 上一页
gg				 到第一行
G				 到最后一行

su - [usr]: 切换到user用户下

grep [option] [指定字串] [文件]: 在文件中搜寻字串匹配的行并输出
-i: 不区分大小写
-v: 排除指定字串


date # 日期与时间
cal # 日历
df # 磁盘剩余空间
free # 内存

```

