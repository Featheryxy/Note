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

clear or Ctrl+L  清屏 
[tab] 命令补全，文件补齐 
Ctrl+c  中断目前程序
exit 退出当前机器
Ctrl+d  End Of File, EOF or End Of Input, 可代替exit
shift+page up 向上翻页
shift+page down 向下翻页




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


```





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

