中央处理器（Cenntral Processing Unit, CPU）：含有微指令集

- 算数逻辑单元：负责程序运算与逻辑判断
- 控制单元：协调各周边组件与各单元间的工作



指令集

- 精简指令集（RISC）
- 复杂指令集（CISC）,x86架构

64位CPU代表其一次性可以读取64bits的数据



指令周期：1Hz，1次/秒

网络传输：Mbits per second, Mbps, 20M/5M



```shell

[milo@localhost ~]$
[当前用户名@主机名 目前所在目录] 提示字符

~   当前用户目录
/   根目录
#   root用户提示符
$   一般用户提示符

[milo@localhost network-scripts]$ cd ~
[milo@localhost ~]$ pwd
/home/milo

[milo@localhost ~]$ command [-options] parameter1 parameter1 ...
					  指令       选项      参数1       参数2	   	

使用反斜杠(\) 跳脱[Enter]符号，使指令连续到下一行。
PS: \ 后立刻接特殊符号



clear or Ctrl+L  清屏 
[tab] 命令补全，文件补齐 
Ctrl+c  中断目前程序
exit 退出当前机器
Ctrl+d  End Of File, EOF or End Of Input, 可代替exit
shift+page up 向上翻页
shift+page down 向下翻页

command --help 简要说明
man command (man: manual) 详细说明
info command 详细说明,以分页形式展示


查看已ca为开头的命令
[milo@localhost /]$ ca[tab][tab]
cacertdir_rehash     cache_writeback      case
cache_check          cal                  cat
cache_dump           ca-legacy            catchsegv
cache_metadata_size  caller               catman
cache_repair         capsh
cache_restore        captoinfo

----------------------------------------------------------
[milo@localhost ~]$ man date
DATE(1)                          User Commands                         DATE(1)

NAME
       date - print or set the system date and time
...

【DATE(1)】括号中的代号
1. 用户在shell 环境中可以操作的指令或可执行文件
5. 配置文件或者是某些文件的格式
8. 系统管理员可用的管理指令
-----------------------------------------------------------

sync 将数据同步写入硬盘中，已集成到shutdown,reboot命令中
shutdown 关机
reboot  重启
```



文件拥有者， 群组， 其他人

User, Group, Others



```shell
su - username  切换用户

[milo@localhost etc]$ su - root
Password:
Last login: Wed Aug  4 17:26:56 CST 2021 on tty1

[root@localhost ~]# ls -al
total 28
dr-xr-x---.  2 	  root   root   135     Aug  4 17:27 .
dr-xr-xr-x. 17 	  root   root   224     Aug  4 16:49 ..
...
-rw-r--r--.  1 	  root   root   100     Dec 29  2013 .cshrc
-rw-r--r--.  1 	  root   root   129     Dec 29  2013 .tcshrc
[   权限  ] [连结][拥有者] [群组][文件大小]  [修改日期]    [文件名称]

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
```



Filesystem Hierarchy Standard(FHS)

|                    | 可分享的（shareable）     | 不可分享的（unshareable） |
| ------------------ | ------------------------- | ------------------------- |
| 不变的（static）   | /usr(软件放置处)          | /etc(配置文件)            |
| 不变的（static）   | /opt(第三方协力软件)      | /boot(开机与核心档)       |
| 可变的（variable） | /var/mail（使用者邮箱）   | /var/run(程序相关)        |
| 可变的（variable） | /var/spool/news（新闻组） | /var/lock(程序相关)       |

软件安装路径  /usr/local

/(root)：与开机系统有光

/usr(Unix System Resource) ：与软件安装/执行相关

/var(variable)：与系统运作过程相关



    起别名 alias
    alias lm='ls -al'
    通配符 *




用户使用shell将我们输入的指令与Kernel沟通

每一个进程都有一个唯一的PID来标识

程序（program)：通常为binary program, 放置再存储媒介中

进程（process）：程序被触发后，执行者的权限与属性、程序代码和所需数据等被加载到内存中，操作系统并给予这个内存内的单元一个标识符（PID）



子进程：在父进程中创建新的进程， 拥有PPID(Parent PID)，杀死子进程，过一段时间可能会新起一个同名但是不同PID的子进程，所以删除进程时应删除父进程

```shell
只查阅当前bash的进程
[milo@localhost /]$ ps -l
F S   UID    PID   PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000  22764  22762  0  80   0 - 28886 do_wai pts/1    00:00:00 bash
0 S  1000  36246  22764  0  80   0 - 28917 do_wai pts/1    00:00:00 bash
0 R  1000  36531  36246  0  80   0 - 38331 -      pts/1    00:00:00 ps

F: 进程标志
	- 4：此进程的权限为root
	- 1：此子进程仅进行复制（fork）而没有实际执行（exec）
S: 进程状态（STAT)
	- R(Running)
	- S(Sleep): 正在睡眠（idle）,但是可以被唤醒
	- D: 不可被唤醒的状态，通常这支程序可能在等待I/O的情况
	- T: 停止状态（stop），可能在工作控制（背景涨停）或除错（traced）状态
	- Z(Zombie): 僵尸状态，进程已经终止却没法被移除至内存外
	
UID/PID/PPID: 该进程被该UID所拥有/进程的PID号/该进程的父进程PID号
C: CPU使用率，%
PRI/NI: Priority/Nice 的缩写,代表此进程被CPU所执行的优先级，数值越小代表该进程越快被CPU执行。
ADDR/SZ/WCHAN:都与内存有关，ADDR 是kernel function，指出该进程在内存的哪个部分，如果是个
running的进程，一般显示[-]; /SZ 该进程占用的内存；/WCHAN 该进程是否运作，[-]表示运作中
TTY:登入者的终端机位置，若为远程登录则使用动态终端接口(pts/n); .

TIME:使用掉的CPU时间，注意，是此进程实际花费CPU运作的时间，而不是系统时间;

CMD: 触发此进程的程序指令



进程之间通过一个讯号（signal）来通信
kill -signal PID
sighup: 代号1，启动被终止的进程，可让该PID重新读取自己的配置文件，类似重新启动
sigkill: 代号9，强制中断一个进程，如果该进程进行到一般，那尚未完成的部分可能会有半个副产品产生
sigterm: 代号15，正常的结束进程
sigstop: 代号19，等价与ctrl+z，暂停一个进程

查看内存使用情况
free [-b|-k|-m|-g|-h] [-t],
-b: 直接输入free时，显示的单位时Kbytes，使用b(bytes), m(Mbytes)
```



一个service需要一个daemon进程，通常以{xxx}d命名



Tarball 文件，先将原始码文件进行tar打包，然后进行压缩，如gzip

RPM(RedHat Package Manager)

```shell
安装软件
rpm -ivh package_name
-i: install
-v: verbose
-h: 以安装信息列显示安装进度

rpm -qa
-q: 查询软件，后接软件名称
-qa: 查询所有已安装软件


grep -iv [指定字串] [文件]
功能描述：在文件中搜寻字串匹配的行并输出
-i: 不区分大小写
-v: 排除指定字串
```

