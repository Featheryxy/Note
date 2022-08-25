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

[demo@localhost ~]$ mkd 双击tab 
mkdict    mkdir     mkdosfs   mkdumprd

info [命令] # 详细的介绍
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



```shell
ps  # (process status) 查看进程,只是列出与当前终端会话相关的进程
ps x # 展示所有进程，不管它们由什么终端（如果有的话）控制
ps aux # 显示属于每个用户的进程信息.
top # 以进程活动顺序显示连续更新的系统进程列表。（默认情况下，每三秒钟更新一次）
Ctrl-c # 终止一个程序. 终端发送一个叫做 INT（Interrupt, 中断）的信号给程序
Ctrl-z # 停止一个进程, 隐藏到后端. 终端发送一个叫做 TSTP（Terminal Stop,终端停止）的信号给程序
command & # 在后端启动任务
jobs # 
fg [jobspec] # foreground 前台 显示到前台 jobspec = %1
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

[root@VM-0-12-centos ~]# top &
[2] 13493
任务控制 (job control), shell 告诉我们再后台(background)已经启动了任务号 (job number) 为 2（“［2］”），PID 为 13493 的程序

[root@VM-0-12-centos ~]# jobs
[1]-  Stopped                 top
[2]+  Stopped                 top

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

### 缩写

```shell
-f # force
-v # verbose
-d # directory
ps # process status
s #
TTY # Teletype 电传打字机 终端
up # 持续
q # quit
h # help human
fg # foreground 前台
```

