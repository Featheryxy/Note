bash 是最初 Unix 上由 Steve Bourne 写成 shell 程序 sh 的增强版

### 界面

```shell
[milo@localhost ~]$
[当前用户名@主机名 目前所在目录] 提示字符

~   当前用户目录
/   根目录
#   root用户提示符, 超级用户权限
$   一般用户提示符
```

### 命令

```shell
command [-options] parameter1 parameter1 ...
 指令       选项      参数1       参数2	   	

使用反斜杠(\) 跳脱[Enter]符号，使指令连续到下一行。
PS: \ 后立刻接特殊符号

command1; command2; command3... # 按顺序执行 command1，command2，command3... 如cd /; ll

alias # 查看所有定义在系统环境中的别名
alias [-p] [name[=value] ...] # 为命令起别名
unalias # 删除别名
[ta6@10 /]$ alias foo='cd /usr; ls; cd -'
[ta6@10 /]$ foo
bin  etc  games  include  lib  lib64  libexec  local  sbin  share  src  tmp
/
[ta6@10 /]$ unalias foo
[ta6@10 /]$ type foo
-bash: type: foo: 未找到

uname -srm # c
```

### 帮助命令

```shell
type [command] # 显示命令的类型， 可以寻找是否存在改命令
which [命令] # 显示一个可执行程序的位置, 只对可执行程序有效，不包括内建命令和命令别名
whatis [命令] # 显示非常简洁的命令说明

help [command] # shell 内建命令的帮助
man [-k] [命令或配置文件] # manual, 显示程序手册页，命令的具体参数及使用方法,难阅读
-k # 只记得部分命令关键字的场合，我们可通过man -k来搜索
apropos # 显示适当的命令 等价于 man [-k]

[demo@localhost ~]$ mkd 双击tab # 查看已mkd为开头的命令
mkdict    mkdir     mkdosfs   mkdumprd

info [命令] # 详细的介绍


1 用户命令
2 程序接口内核系统调用
3 C 库函数程序接口
4 特殊文件，比如说设备结点和驱动程序
5 文件格式
6 游戏娱乐，如屏幕保护程序
7 其他方面
8 系统管理员命令
```

### 系统目录

```shell
/ # 根目录
/bin # 包含系统启动和运行所必须的二进制程序
/boot # 包含 Linux 内核、初始 RAM 磁盘映像（用于启动时所需的驱动）和启动加载程序。
有趣的文件：
/boot/grub/grub.conf or menu.lst，# 被用来配置启动加载程序。
/boot/vmlinuz # Linux 内核。
/dev # 包含设备结点的特殊目录
/etc # 所有系统层面的配置文件 也包含一系列的 shell 脚本，在系统启动时，这些脚本会开启每个系统服务。 
/etc/crontab，定义自动运行的任务。
/etc/fstab # 包含存储设备的列表，以及与他们相关的挂载点
/etc/passwd # 包含用户帐号列表
/etc/rc.d # 的配置文件和脚本
/home # 系统会在/home 下，给每个用户分配一个目录，如/home/user，可以用~user表示, 普通用户只能在自己的目录下写文件
/lib # 标准程序设计库，又叫动态链接共享库，核心系统程序所使用的共享库文件, 作用类似windows里的.dll文件
/lost+found # 目录平时是空的，系统非正常关机而留下“无家可归”的文件（windows下叫什么.chk）就在这里
/media # 目录会包含可移动介质的挂载点，例如 USB 驱动器，CD-ROMs 等等。这些介质连接到计算机之后，会自动地挂载到这个目录结点下。
/mnt # 在早些的 Linux 系统中，/mnt 目录包含可移动介质的挂载点。
/opt # 被用来安装“可选的”软件。这个主要用来存储可能安装在系统中的商业软件产品。
/proc # 这个/proc 目录很特殊。从存储在硬盘上的文件的意义上说，它不是真正的文件系统。相反，它是一个由 Linux 内核维护的虚拟文件系统。它所包含的文件是内核的窥视孔。这些文件是可读的，它们会告诉你内核是怎样监管计算机的。
/root # 系统管理员的主目录
/sbin # 超级管理命令，这里存放的是系统管理员使用的管理程序
/tmp # 是用来存储由各种程序创建的临时文件的地方。一些配置导致系统每次重新启动时，都会清空这个目录。
/proc 虚拟的目录，是系统内存的映射。可直接访问这个目录来获取系统信息。
/var 某些大文件的溢出区，比方说各种服务的日志文件

/usr # 最庞大的目录，要用到的应用程序和文件几乎都在这个目录 
/usr/bin # 包含系统安装的可执行程序
/usr/lib # 包含由/usr/bin 目录中的程序所用的共享库。
/usr/local #是非系统发行版自带程序的安装目录。通常，由源码编译的程序会安装在/usr/local/bin 目录下。新安装的 Linux 系统中会存在这个目录，并且在管理员安装程序之前，这个目录是空的。
/usr/sbin # 包含许多系统管理程序。
/usr/share #包含许多由/usr/bin 目录中的程序使用的共享数据。其中包括像默认的配置文件、图标、桌面背景、音频文件等等。
/usr/share/doc # 大多数安装在系统中的软件包会包含一些文档。在/usr/share/doc 目录下，我们可以找到按照软件包分类的文档。
/var # 除了/tmp 和/home 目录之外，相对来说，目前我们看到的目录是静态的，这是说，它们的内容不会改变。/var 目录存放的是动态文件。各种数据库，假脱机文件，用户邮件等等，都位于在这里。
/var/log # 这个/var/log 目录包含日志文件、各种系统活动的记录。这些文件非常重要，并且应该时时监测它们。其中最重要的一个文件是/var/log/messages。注意，为了系统安全，在一些系统中，你必须是超级用户才能查看这些日志文件。

usr是user的缩写，是曾经的HOME目录，然而现在已经被/home取代了，现在usr被称为是Unix System Resource，即Unix系统资源的缩写。
```

- 软件包目录：/opt/setups
- 解压后软件包目录: /usr/program

### 文件类型

```shell
[root@localhost ~]# ls -al
total 28
dr-xr-x---.  2 	 	   root    root      135      Aug  4 17:27 .
dr-xr-xr-x. 17 	  	   root    root      224      Aug  4 16:49 ..
...
-rw-r--r--.  1 	  	   root    root      100      Dec 29  2013 .cshrc
-rw-r--r--.  1 	  	   root    root      129      Dec 29  2013 .tcshrc
[   权限  ] [硬链接数目][拥有者] [所属用户组][文件大小]  [最后修改修改日期]    [文件名称]

文件大小默认以bytes为单位
隐藏文件：以 “.” 字符开头的文件名。这仅表示，ls 命令不能列出它们，用 ls -a 命令就可以了, 如.tcshrc
Linux 没有“文件扩展名”的概念
文件名可能包含空格，标点符号，但标点符号仅限使用“.”，“－”，下划线


-           rw-            r--          r--
[文件类型][文件拥有者权限][文件所属群组权限][其他人权限]

文件类型：
d 目录
- 文件
	1. ASSII 文件，可以使用cat查看
	2. binary 文件，可执行文件（scripts），如cat
	3. 数据格式文件（data）, 拥有特定格式的文件
l 符号链接（也称为软链接或者 symlink ） 相当于Windows下的快捷方式
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

文件的执行主要看文件的权限，而不看文件名。
命名习惯:
*.sh表示批处理文件（scripts）
*.tar为压缩文件
```

### 操作文件和目录

```shell
pwd # print working directory: 显示当前工作目录

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

cd # change directory
cd [/path] # /path
cd [./path] # . 工作目录   ./可省略 等价 cd path
cd [..] # .. 工作目录的父目录
cd # 回到home目录
cd - # 更改工作目录到先前的工作目录

file [dictory] # 确定文件类型
less [dictory] # 浏览文件内容
zless [dictory] # 可以显示由 gzip 压缩的文本文件的内容

mkdir [目录名1] [目录名2] # make directories
rmdir [目录名]: remove empty directories
mv [原文件或目录] [目标目录] # 移动/重命名文件和目录


cp [原文件或目录] [目标目录]# 复制文件或目录
-r 复制目录
-p 保留文件属性（文件最后一次的修改时间）
cp /etc/passwd . # 复制文件到当前目录下


rm [dictoryname] [filename]# 删除文件和目录, 
删除前先使用ls 命令查看无误后再删除
-r (recursive) # 就是向下递归，不管有多少级目录，一并删除
-f (force) # 就是直接强行删除，不作任何提示的意思
rm -rf # 删除文件夹及下面所有文件

ln [target] [link-name]# 创建硬链接和符号链接
一个文件至少有一个硬链接，因为文件名就是由链接创建的
假设文件由两部分组成：包含文件内容的数据部分和持有文件名的名字部分,我们创建文件硬链接的时候，实际上是
为文件创建了额外的名字部分，并且这些名字都关联到相同的数据部分.这时系统会分配一连串的磁盘块给所谓的索引节点，然后索引节点与文件名字部分相关联。因此每一个硬链接都关系到一个具体的包含文件内容的索引节点。
[root@VM-0-12-centos playgroud]# ll -i
total 24
658354 drwxr-xr-x 2 root root 4096 Aug 24 22:49 dir1
658355 drwxr-xr-x 2 root root 4096 Aug 24 22:50 dir2
658357 drwxr-xr-x 2 root root 4096 Aug 24 22:52 dir3
658356 -rw-r--r-- 4 root root 1141 Aug 24 22:42 fun
658356 -rw-r--r-- 4 root root 1141 Aug 24 22:42 fun-hard
658358 -rw-r--r-- 1 root root    2 Aug 24 22:53 hello

硬链接不能跨越物理设备，硬链接不能关
联目录，只能是文件。符号链接是文件的特殊类型，它包含一个指向目标文件或目录的文本指
针。
```

### 硬链接和符号链接

```shell
ln [target] [link-name]# 创建硬链接和符号链接
一个文件至少有一个硬链接，因为文件名就是由链接创建的
假设文件由两部分组成：包含文件内容的数据部分和持有文件名的名字部分,我们创建文件硬链接的时候，实际上是
为文件创建了额外的名字部分，并且这些名字都关联到相同的数据部分.这时系统会分配一连串的磁盘块给所谓的索引节点，然后索引节点与文件名字部分相关联。因此每一个硬链接都关系到一个具体的包含文件内容的索引节点。

[root@VM-0-12-centos playgroud]# ll -i
total 24
658354 drwxr-xr-x 2 root root 4096 Aug 24 22:49 dir1
658355 drwxr-xr-x 2 root root 4096 Aug 24 22:50 dir2
658357 drwxr-xr-x 2 root root 4096 Aug 24 22:52 dir3
658356 -rw-r--r-- 4 root root 1141 Aug 24 22:42 fun
658356 -rw-r--r-- 4 root root 1141 Aug 24 22:42 fun-hard
658358 -rw-r--r-- 1 root root    2 Aug 24 22:53 hello
第一字段表示文件索引节点号,正如我们所见到的，fun 和 fun-hard共享一样的索引节点号，这就证实这两个文件是同一个文件

硬链接不能跨越物理设备，硬链接不能关联目录，只能是文件。符号链接是文件的特殊类型，它包含一个指向目标文件或目录的文本指
针。

ln -s fun fun-sym
```

### 进程管理

当系统启动的时候，内核先把一些它自己的活动初始化为进程，然后运行一个叫做 init 的程序。init，依次地，再运行一系列的称为 init 脚本的 shell 脚本（位于/etc），它们可以启动所有的系统服务。其中许多系统服务以守护（daemon）程序的形式实现，守护程序仅在后台运行，没有任何用户接口 (User Interface)。这样，即使我们没有登录系统，至少系统也在忙于执行一些例行事务。一个程序可以发动另一个程序被表述为一个父进程可以产生一个子进程。系统分配给每个进程一个数字，这个数字叫做进程 (process) ID 或 PID。PID 号按升序分配，init 进程的 PID 总是 1.内核也对分配给每个进程的内存和就绪状态进行跟踪以便继续执行这个进程。像文件一样，进程也有所有者和用户 ID，有效用户 ID，等等。

用户使用shell将我们输入的指令与Kernel沟通

每一个进程都有一个唯一的PID来标识

程序（program)：通常为binary program, 放置再存储媒介中

进程（process）：程序被触发后，执行者的权限与属性、程序代码和所需数据等被加载到内存中，操作系统并给予这个内存内的单元一个标识符（PID）

子进程：在父进程中创建新的进程， 拥有PPID(Parent PID)，杀死子进程，过一段时间可能会新起一个同名但是不同PID的子进程，所以删除进程时应删除父进程

一个service需要一个daemon进程，通常以{xxx}d命名

```shell
ps  # (process status) 查看进程,只是列出与当前终端会话相关的进程
ps x # 展示所有进程，不管它们由什么终端（如果有的话）控制
ps aux # 显示属于每个用户的进程信息.
ps -ef # 显示属于每个用户的进程信息.
top # 以进程活动顺序显示连续更新的系统进程列表。（默认情况下，每三秒钟更新一次）
Ctrl-c # 终止一个程序. 终端发送一个叫做 INT（Interrupt, 中断）的信号给程序
Ctrl-z # 停止一个进程, 隐藏到后端. 终端发送一个叫做 TSTP（Terminal Stop,终端停止）的信号给程序
command & # 在后端启动任务
jobs # 
fg [jobspec] # foreground 前台 显示到前台 jobspec = %1
kill %1 jobspec
kill [-signal] PID... # 默认情况下，终端发送 TERM（Terminate，终止）信号给程序
kill -l # 显示所有信号
killall [-u user] [-signal] name...# 给匹配特定程序或用户名的多个进程发送信号


信号是操作系统与程序之间进行通信时所采用的几种方式中的一种
1 # HUP 挂起（Hangup）。这是美好往昔的残留部分，那时候终端机通过电话线和调制解调器连接到远端的计算机。这个信号被用来告诉程序，控制的终端机已经“挂断”。通过关闭一个终端会话，可以展示这个信号的作用。在当前终端运行的前台程序将会收到这个信号并终止。许多守护进程也使用这个信号，来重新初始化。这意味着，当一个守护进程收到这个信号后，这个进程会重新启动，并且重新读取它的配置文件。Apache网络服务器守护进程就是一个例子。
2 # INT 中断。实现和 Ctrl-c 一样的功能，由终端发送。通常，它会终止一个程序。
9 # KILL 杀死。这个信号很特别。尽管程序可能会选择不同的方式来处理发送给它的信号，其中也包含忽略信号，但是 KILL 信号从不被发送到目标程序。而是内核立即终止这个进程。当一个进程以这种方式终止的时候，它没有机会去做些“清理”工作，或者是保存工作。因为这个原因，把 KILL 信号看作最后一招，当其它终止信号失败后，再使用它。
15 # TERM 终止。这是 kill 命令发送的默认信号。如果程序仍然“活着”，可以接受信号，那么这个它会终止。
18 #CONT 继续。在一个停止信号后，这个信号会恢复进程的运行。
19 # STOP 停止。这个信号导致进程停止运行，而不是终止。像KILL 信号，它不被发送到目标进程，因此它不能被忽略。
3 # QUIT 退出
11 # SEGV段错误 (Segmentation Violation)。如果一个程序非法使用内存，就会发送这个信号。也就是说，程序试图写入内存，而这个内存空间是不允许此程序写入的
20 # TSTP 终端停止 (Terminal Stop)。当按下 Ctrl-z 组合键后，终端发送这个信号。不像 STOP 信号，TSTP 信号由目标进程接收，且可能被忽略。
28 # WINCH 改变窗口大小 (Window Change)。当改变窗口大小时，系统会发送这个信号。一些程序，像 top 和 less程序会响应这个信号，按照新窗口的尺寸，刷新显示的内容。

pstree # 输出一个树型结构的进程列表 (processtree)，这个列表展示了进程间父/子关系。
vmstat # 输出一个系统资源使用快照，包括内存，交换分区和磁盘 I/O。为了看到连续的显示结果，则在命令名后加上更新操作延时的时间（以秒为单位）。例如，“vmstat 5”。，按下 Ctrl-c组合键, 终止输出。

[root@VM-0-12-centos etc]# ps
  PID TTY          TIME CMD
 8801 pts/0    00:00:00 bash
 9832 pts/0    00:00:00 ps
PID #  process id
TTY # Teletype 电传打字机 终端
TIME # 表示进程所消耗的 CPU 时间数量

[root@VM-0-12-centos etc]# ps x
  PID TTY      STAT   TIME COMMAND
    1 ?        Ss     0:16 /usr/lib/systemd/systemd --switched-root --system --deserialize 22
    2 ?        S      0:00 [kthreadd]
    4 ?        S<     0:00 [kworker/0:0H]
TTY # TTY一栏中出现的 “?” ，表示没有控制终端   
STAT # state 进程当前状态
R # 运行中。这意味着，进程正在运行或准备运行。
S # 正在睡眠。进程没有运行，而是，正在等待一个事件，比如说，一个按键或者网络分组。
D # 不可中断睡眠。进程正在等待 I/O，比方说，一个磁盘驱动器的 I/O。
T # 已停止. 已经指示进程停止运行。稍后介绍更多。
Z # 一个死进程或“僵尸”进程。这是一个已经终止的子进程，但是它的父进程还没有清空它。（父进程没有把子进程从进程表中删除）
< # 一个高优先级进程。这可能会授予一个进程更多重要的资源，给它更多的 CPU 时间。进程的这种属性叫做 niceness。具有高优先级的进程据说是不好的（less nice），因为它占用了比较多的 CPU 时间，这样就给其它进程留下很少时间。
N # 低优先级进程。一个低优先级进程（一个“nice”进程）只有当其它高优先级进程被服务了之后，才会得到处理器时间。

只查阅当前bash的进程
[milo@localhost /]$ ps -l
F S   UID    PID   PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000  22764  22762  0  80   0 - 28886 do_wai pts/1    00:00:00 bash
0 S  1000  36246  22764  0  80   0 - 28917 do_wai pts/1    00:00:00 bash
0 R  1000  36531  36246  0  80   0 - 38331 -      pts/1    00:00:00 ps
UID/PID/PPID: 该进程被该UID所拥有/进程的PID号/该进程的父进程PID号
C: CPU使用率，%
PRI/NI: Priority/Nice 的缩写,代表此进程被CPU所执行的优先级，数值越小代表该进程越快被CPU执行。
ADDR/SZ/WCHAN:都与内存有关，ADDR 是kernel function，指出该进程在内存的哪个部分，如果是个
running的进程，一般显示[-]; /SZ 该进程占用的内存；/WCHAN 该进程是否运作，[-]表示运作中
TTY:登入者的终端机位置，若为远程登录则使用动态终端接口(pts/n); .
CMD: 触发此进程的程序指令
TIME:使用掉的CPU时间，注意，是此进程实际花费CPU运作的时间，而不是系统时间;

F: 进程标志
	- 4：此进程的权限为root
	- 1：此子进程仅进行复制（fork）而没有实际执行（exec）
	
[root@VM-0-12-centos ~]# top &
[2] 13493
任务控制 (job control), shell 告诉我们再后台(background)已经启动了任务号 (job number) 为 2（“［2］”），PID 为 13493 的程序

[root@VM-0-12-centos ~]# jobs
[1]-  Stopped                 top
[2]+  Stopped                 top

```



###  软件包管理

- RPM(RedHat Package Manage)
- YUM(Yellow dog Updater Modified)：解决了RPM的属性依赖问题，通过依赖rpm软件包管理器，实现了rpm软件包管理器在功能上的扩展，因此yum是不能脱离rpm而独立运行的

```shell 
yum [options] command [package ...]
yum search package_name # 在yum服务器上查找包
yum -y install package_name 
yum list updates # 列出可升级的软件
yum erase package_name # 卸载软件
yum list installed 等于 rpm -qa # 列出已安装的软件
rpm -qa package_name # 是否安装了一个软件包
yum info package_name # 显示所安装软件包的信息
rpm -qf file_name # 查找安装了某个文件的软件包

[options]
-y # 自动回答yes
--installroot=/some/path: 自定义安装路径

[查询工作项目] [相关参数]
search:
list: 列出yum服务器上提供的所有软件 rpm -qa


yum list isntalled: 列出已安装的软件
```

### 网络系统

Listening: 监听状态（即等待接入请求）的套接字

```shell
ifconfig # interface configure 网卡名称 IP地址
ping id_address
traceroute id_address # 路由跟踪,显示数据包到主机间的路径

netstat # 显示网络相关信息
netstat -a # 列出所有当前的连接
netstat -at #  -t 选项列出 TCP 协议的连接
netstat -au #  -u 选项列出 UDP 协议的连接
netstat -an # numeric 直接使用IP地址，而不通过域名服务器
netstat -tnl # -t 只列出监听中的连接, 不能使用-a, 
netstat -tnlp # -p 查看进程信息, netstat 必须运行在 root 权限之下，不然它就不能得到运行在 root 权限下的进程名，而很多服务包括 http 和 ftp 都运行在 root 权限之下
netstat -tlep # -ep 同时查看进程名和用户名,  -n 和 -e 选项一起使用，User 列的属性就是用户的 ID 号，而不是用户名
netstat -s # 列出所有网络包的统计情况
netstat -rn # 显示Routing Table
wget [URL] # 非交互网络下载器
```



```shell
[root@VM-0-12-centos ~]# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.12  netmask 255.255.240.0  broadcast 172.17.15.255
        inet6 fe80::5054:ff:fe26:7351  prefixlen 64  scopeid 0x20<link>
        ether 52:54:00:26:73:51  txqueuelen 1000  (Ethernet)
        RX packets 2152519  bytes 497701765 (474.6 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1904673  bytes 295675469 (281.9 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 440  bytes 56320 (55.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 440  bytes 56320 (55.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        
 eth0，是以太网接口，和第二个，叫做 lo，是内部回环网络接口，它是一个虚拟接口 
 
[root@VM-0-12-centos ~]# netstat -rn
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         172.17.0.1      0.0.0.0         UG        0 0          0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U         0 0          0 eth0
172.17.0.0      0.0.0.0         255.255.240.0   U         0 0          0 eth0

第二行显示了目的地 169.254.0.0。IP 地址以零结尾是指网络，而不是独立主机，所以这个目的地意味着局域网中的任何一台主机
下一个字段，Gateway，是网关（路由器）的名字或 IP 地址，用它来连接当前的主机和目的地的网络。若这个字段显示一个星号，则表明不需要网关。
```

### SHELL环境

shell 在 shell 会话中保存着大量信息， 这些信息被称为环境变量。一些程序会根据环境变量来调整他们的行为。可以使用`echo $环境变量命` 来打印变量值。

环境存放下面两种信息

- shell 变量：bash 存放的少量数据
- 环境变量

```shell
printenv # 只显示环境变量
set # 可以显示shell 变量和环境变量
export [-fnp][变量名称]=[变量设置值] # 设置或显示环境变量,仅限于该次登陆操作
source FILENAME # 用于保留、更改当前shell中的环境变量,在当前shell中运行execute命令。
echo $PATH # 打印可执行程序路径，由冒号分开的目录列表，当你输入可执行程序名后，会搜索这个目录列表。
```

当我们登录系统后，bash 程序启动，并且会读取一系列称为启动文件的配置脚本，这些文件定义了默认的可供所有用户共享的 shell 环境。然后是读取更多位于我们自己家目录中的启动文件，这些启动文件定义了用户个人的shell 环境。

1. /etc/profile 应用于所有用户的全局配置脚本。
2. ˜/.bash_profile 用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。
3. ˜/.bash_login 如果文件 ˜/.bash_profile 没有找到，bash 会尝试读取这个脚本
4. ˜/.profile 如果文件 ˜/.bash_profile 或文件 ˜/.bash_login 都没有找到，bash 会试图读取这个文件。这是基于 Debian 发行版的默认设置，比方说 Ubuntu。
5. ˜/.bashrc 用户个人的启动文件。可以用来扩展或重写全局配置脚本中的设置。

### echo

```shell
echo (1)             - display a line of text
echo * #  打印当前目录下的文件 shell 在 echo 命令被执行前把 “*” 展开成了当前工作目录下的文件名字
echo .* # 打印当前目录下以.开头的文件或目录
echo $((expression)) # 只支持整数
echo 报头{}附言 
echo $变量名
echo "*" # 只打印*, 双引号表示使用普通字符,但是$，\ (反斜杠），和 ‘（倒引号）除外
双引号(" "): 只展开 $，\ (反斜杠），和 ‘（倒引号）
单引号(' '): 禁止所有的展开
转义字符(\): 1. 阻止展开特殊字符 2. 控制码, 如\b \n \r \t 如  echo -e "time's\r\n up "
[root@VM-0-12-centos ~]#  echo Front-{A,B,C}-Back
Front-A-Back Front-B-Back Front-C-Back

[root@VM-0-12-centos ~]#  echo Number_{1..5}
Number_1 Number_2 Number_3 Number_4 Number_5

# 删除多余的空格
[root@VM-0-12-centos /]# echo this is a            text
this is a text

单词分割机制会在单词中寻找空格，制表符，和换行符，并把它们看作单词之间的界定符。这意味着无引用的空格，制表符和换行符都不是文本的一部分，它们只作为分隔符使用。由于它们把单词分为不同的参数.如果我们加上双引号,，内嵌的空格也不会被当作界定符，它们成为参数的一部分。一旦加上双引号，我们的命令行就包含一个带有一个参数的命令。


[root@VM-0-12-centos /]# echo $(cal)
September 2022 Su Mo Tu We Th Fr Sa 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
[root@VM-0-12-centos /]# echo "$(cal)"
   September 2022
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

没有引用的命令替换导致命令行包含 38 个参数
在第二个例子中，命令行只有一个参数，参数中包括嵌入的空格和换行符。

[root@VM-0-12-centos /]# echo "dolloar $5.00"
dolloar .00
[root@VM-0-12-centos /]# echo "dolloar \$5.00"
dolloar $5.00

```



### SSH

SSH 协议替代了 telnet（端口 23）和 ftp（端口21）两个协议的，使用22端口

SSH: Secure Shell 

- 认证远端主机是否为它所知道的那台主机（这样就阻止了所谓的“中间人”的攻击）
- 它加密了本地与远程主机之间所有的通讯信息

组成

1. SSH 服务端运行在远端主机上，在端口 22 上监听收到的外部连接
2. SSH 客户端用在本地系统中，用来和远端服务器通信

> 大多数 Linux 发行版自带一个提供 SSH 功能的软件包，叫做 OpenSSH. 一些发行版默认包含客户端和服务端两个软件包（例如 Red Hat）

```shell
ssh remote-sys # 以当前用户连接远端主机
ssh user@remote-sys # 以user用户连接远端主机
```

### SFTP

FTP（它的原始形式）以明码形式发送帐号的姓名和密码

SFTP（Secure File Transfer Protocol，安全文件传输协议） 

> sftp 在OpenSSH包下?
>
>  sftp 不需要远端系统中运行 FTP 服务端。它仅仅需要 SSH 服务端。这意味着任何一台能用 SSH 客户端连接的远端机器，也可当作类似于 FTP 的服务器来使用

```shell
1. 连接远程服务器
sftp remote_user@remote_host
2. 使用端口进行连接
sftp -P remote_port remote_user@remote_host
3. 从远程服务器拉取文件
get /path/remote_file
get -r ./. # 拉取远程的 当前目录下的 所有 子目录及里面的 文件
4. 上传本地文件到服务器
put local_file
5. 查看远程服务器目录内容
ls
6.查看本地目录内容
lls  # l = local
7.执行本地 Shell 命令
![command]
```

### 查找文件

```shell
locate [file_name] # 通过名字来查找文件
find [file_name] # 在一个目录层次结构中搜索文件
xargs # 从标准输入生成和执行命令行
touch # 更改文件时间
stat# 显示文件或文件系统状态
```

> locate 数据库由另一个叫做 updatedb 的程序创建。通常，这个程序作为一个定时任务（jobs）周期性运转；也就是说，一个任务在特定的时间间隔内被 cron 守护进程执行。大多数装有 locate的系统会每隔一天运行一回 updatedb 程序。因为数据库不能被持续地更新，所以当使用 locate 时，你会发现目前最新的文件不会出现。为了克服这个问题，通过更改为超级用户身份，在提示符下运行 updatedb 命令，可以手动运行 updatedb 程序。
>
> /tmp下的文件不在文件资料库下

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

### 正则表达式



```shell
grep # global regular expression prin 在文本文件中查找一个指定的正则表达式，并把匹配行输出到标准输出
grep [options] regex [file...]
-i # 忽略大小写。不会区分大小写字符。也可用--ignore-case 来指定。
-v # 不匹配。通常，grep 程序会打印包含匹配项的文本行。这个选项导致 grep 程序只会打印不包含匹配项的文本行。也可用--invert-match 来指定。
-c # 打印匹配的数量（或者是不匹配的数目，若指定了-v 选项），而不是文本行本身。也可用--count 选项来指定。
-l # 打印包含匹配项的文件名，而不是文本行本身，也可用--files-with-matches 选项来指定。
-L # 相似于-l 选项，但是只是打印不包含匹配项的文件名。也可用--files-without-match 来指定。
-n # 在每个匹配行之前打印出其位于文件中的相应行号。也可用--line-number 选项来指定。
-h # 应用于多文件搜索，不输出文件名。也可用--no-filename 选项来指定。
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

### 缩写

```shell
-a # all
-c # continue 持续输出
-d # directory
-e # extend 扩展信息
-f # force
-i # interface
-r # route 

-s # state 状态信息 statistics 统计信息
-v # verbose
-l # listing
-n # numeric 数字的
-p # process 进程 programs 程序
-q # query 查询
ps # process status
TTY # Teletype 电传打字机 终端
up # 持续
q # quit
h # help human
fg # foreground 前台
grep # global regular expression print

^ # Ctrl
```

