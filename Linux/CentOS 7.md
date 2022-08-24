### 常用

```shell
[milo@localhost ~]$
[当前用户名@主机名 目前所在目录] 提示字符

~   当前用户目录
/   根目录
#   root用户提示符, 超级用户权限
$   一般用户提示符

command [-options] parameter1 parameter1 ...
 指令       选项      参数1       参数2	   	

使用反斜杠(\) 跳脱[Enter]符号，使指令连续到下一行。
PS: \ 后立刻接特殊符号
```





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

### 目录与文件

- 隐藏文件：以 “.” 字符开头的文件名。这仅表示，ls 命令不能列出它们，用 ls -a 命令就可以了
- Linux 没有“文件扩展名”的概念
- 文件名可能包含空格，标点符号，但标点符号仅限使用“.”，“－”，下划线

```shell
ls [dictory1] [dictory2]# list：显示目录文件
-a （all）显示所有文件，包括隐藏文件（以 . 开头）
-l （long）详细信息显示
-d （directory）查看目录本身属性 
-h （human） 人性化显示
-i （iNode） 文件的id节点号
-t  (time) 按修改时间降序排列	
-r  (reverse) 反转
ls -l /etc 查看/etc下的文件信息
ls -ld /etc 查看/etc文件本身信息

[root@localhost ~]# ls -al
total 28
dr-xr-x---.  2 	 	   root    root      135      Aug  4 17:27 .
dr-xr-xr-x. 17 	  	   root    root      224      Aug  4 16:49 ..
...
-rw-r--r--.  1 	  	   root    root      100      Dec 29  2013 .cshrc
-rw-r--r--.  1 	  	   root    root      129      Dec 29  2013 .tcshrc
[   权限  ] [硬链接数目][拥有者] [所属用户组][文件大小]  [最后修改修改日期]    [文件名称]

文件大小默认以bytes为单位
.tcshrc 表示该文件是隐藏文件

-           rw-            r--          r--
[文件类型][文件拥有者权限][文件所属群组权限][其他人权限]

文件类型：
d 目录
- 文件
	1. ASSII 文件，可以使用cat查看
	2. binary 文件，可执行文件（scripts），如cat
	3. 数据格式文件（data）, 拥有特定格式的文件
l 连结档link file，相当于Windows下的快捷方式
b 可供存储的接口设备（可随机存取装置）
c 串行端口设备，如键盘，鼠标（一次性读取装置）

权限：
| r    | 读   | 可以查看文件内容 | 列出目录中的内容       |
| w    | 写   | 可以修改文件内容 | 在目录中创建，删除文件 |
| x    | 执行 | 可以执行文件     | 进入目录               |

权限的数字表示
r ---- 4
w ---- 2
x ---- 1

0 ---- 什么都不执行

文件的执行主要看文件的权限，而不看文件名。通常我们使用*.sh表示批处理文件（scripts）;*.tar为压缩文件

pwd # print working directory: 显示当前工作目录
cd # change directory
cd [/path] # /path
cd [./path] # . 工作目录   ./可省略 等价 cd path
cd [..] # .. 工作目录的父目录
cd # 回到home目录
cd - # 更改工作目录到先前的工作目录

file [dictory] # 确定文件类型
less [dictory] # 浏览文件内容


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

