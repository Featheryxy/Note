## 简介

windows 不区分大小写 `eCho` 等价于`echo`

\ 路径

/ 参数

```
echo 输出
@echo off 关闭盘符输出
pause 暂停
exit 退出当前操作，关闭batchfile
%1   传参
SET /P variable=
echo %path%  

`命令 /?`  命令帮助查看


mysql -u root -p密码 #（p后没有空格）

百分号在批处理文件用来表示命令行参数：%1，%2，...
介于两个百分号之间的任何字符将被解释为变量

https://www.cnblogs.com/klchang/p/4771101.html
```

命令分类

- 内部命令：ipconfig, cls
- 外部命令：java, python

## 运算操作

### 算术运算

arithmetic

- 命令模式：`set /a ` 

  ```
  C:\Users\Milo>set /a 1+3
  4
  
  set /a var = 1+2
  echo %var%
  ```

- 文本模式



### 重定向运算

- \> 覆盖原有

- \>> 追加

- type(打字)：文本内容查看

- <

- <<

- 关系运算 

  - < 小于
  - \> 大于

  ```
  F:\Desktop\批处理>echo "hello world" > a.txt
  F:\Desktop\批处理>type a.txt
  "hello world"
  
  F:\Desktop\批处理>echo "hello world" >> a.txt
  
  F:\Desktop\批处理>type a.txt
  "hello world"
  "hello world"
  ```


### 多命令运算

- &&  具有短路，第一个命令错误不会执行第二个命令
- ||

### 管道符号

- |  A|B     先执行A，在A的结果上执行B
  - `dir | find ".txt"`  查找当前路径下的所有带有`.txt`的文件

## 批处理基本命令

### 命令格式

- `命令 子命令 参数 操作 选项`

-  `命令 /?`  命令帮助查看

- `命令 /help` 获取详细的帮助信息

  ```
  F:\Desktop\批处理>net /?
  此命令的语法是:
  
  NET
      [ ACCOUNTS | COMPUTER | CONFIG | CONTINUE | FILE | GROUP | HELP |
        HELPMSG | LOCALGROUP | PAUSE | SESSION | SHARE | START |
        STATISTICS | STOP | TIME | USE | USER | VIEW ]
        
        
  F:\Desktop\批处理>net  user /?
  此命令的语法是:
  
  NET USER
  [username [password | *] [options]] [/DOMAIN]
           username {password | *} /ADD [options] [/DOMAIN]
           username [/DELETE] [/DOMAIN]
           username [/TIMES:{times | ALL}]
           username [/ACTIVE: {YES | NO}]
           
           
  F:\Desktop\批处理>net user test test /add
  发生系统错误 5。
  
  拒绝访问。
  
  F:\Desktop\批处理>net  user /help
  此命令的语法是:
  
  NET USER
  [username [password | *] [options]] [/DOMAIN]
           username {password | *} /ADD [options] [/DOMAIN]
           username [/DELETE] [/DOMAIN]
           username [/TIMES:{times | ALL}]
           username [/ACTIVE: {YES | NO}]
  
  NET USER 将创建并修改计算机上的用户帐户。在不使用命令开关的情况下，
  将列出计算机的用户帐户。用户帐户信息存储在用户帐户数据库中。
  
  username     为可添加、删除、修改或查看的用户帐户的名称。用户帐户名称
               最多可以有 20 个字符。
  password     指定或更改用户帐户的密码。密码的长度必须符合 NET ACCOUNTS
               命令的 /MINPWLEN 选项所设置的最小长度。
               最多可以有 14 个字符。
  *            生成密码提示。在密码提示下键入密码时，将不会显示密码。
  /DOMAIN      在当前域的域控制器上执行此操作。
  /ADD         向用户帐户数据库添加用户帐户。
  /DELETE      从用户帐户数据库删除用户帐户。
  
  选项         如下所示:
  
     选项                       描述
        --------------------------------------------------------------------
     /ACTIVE:{YES | NO}         激活或取消激活帐户。如果该帐户处于非激活状态，
                                用户将无法访问服务器。默认设置为“YES”。
     /COMMENT:"text"            提供有关用户帐户的描述性注释。请将文本用引号
                                括起来。
     /COUNTRYCODE:nnn           使用操作系统国家/地区代码执行指定的语言文件，
                                以显示用户帮助和错误消息。值 0 表示使用默认
                                的国家/地区代码。
     /EXPIRES:{date | NEVER}    如果设置了日期，可导致帐户过期。
                                NEVER 将帐户设置为无时间限制。
                                过期日期采用格式 mm/dd/yy(yy)。
                                月份可以是一个数字、完整字母拼写，
                                或使用三个字母的缩写。年份可以使用两位数字
                                或四位数字。使用斜线(/)(不留空格)
                                将日期的各个部分隔开。
     /FULLNAME:"name"           用户的全名(而不是用户名)。请将该名称用引号
                                括起来。
     /HOMEDIR:pathname          用户的主目录设置路径。该路径必须存在。
     /PASSWORDCHG:{YES | NO}    指定用户是否可以更改其密码。默认设置
                                为“YES”。
     /PASSWORDREQ:{YES | NO}    指定用户帐户是否必须拥有密码。
                                默认设置为“YES”。
     /LOGONPASSWORDCHG:{YES|NO} 指定用户是否应在下次登录时更改其密码。
                                默认设置为“NO”。
     /PROFILEPATH[:path]        为用户登录配置文件设置路径。
     /SCRIPTPATH:pathname       用户登录脚本的位置。
     /TIMES:{times | ALL}       登录小时数。TIMES 表示为
                                day[-day][,day[-day]],time[-time][,time
                                [-time]]，增量限制为 1 小时。
                                日期可以是完整拼写，也可以是缩写。
                                小时可以是 12 或 24 小时表示法。对于
                                12 小时表示法，请使用 am、pm、a.m. 或
                                p.m。ALL 表示用户始终可以登录，
                                空白值表示用户始终不能登录。使用逗号将日期和时
                                间隔开，使用分号将多个日期和时间隔开。
     /USERCOMMENT:"text"        允许管理员添加或更改帐户的用户注释。
     /WORKSTATIONS:{computername[,...] | *}
                                列出用户可用于登录到网络的计算机，最多为八台。
                                如果 /WORKSTATIONS 没有列表，或其列表为 *，
                                则用户可以通过任何计算机登录到网络。
  
  NET HELP 命令 | MORE 显示帮助内容，一次显示一屏。
  ```


### 参数传递 

- .bat文件接受参数使用%num
- `net user %1 %2 /add`

### 注释符

- `rem comment`

```
@echo off
rem program for add new user

echo %1
echo %2

rem use: & '.\net user add.bat'  admin 123
net user %1 %2 /add
pause
```

### 炫酷命令

- 颜色命令 `color`
  - `color 0a`
-  `title` 设置窗口title
  - `title 'hack'`

### 时间

- date

  ```
  F:\Desktop\批处理>date /T
  2020-10-28
  ```

- time

  ```
  F:\Desktop\批处理>time /T
  15:57
  ```

### 启动

- start

  ```
  F:\Desktop\批处理>start /?
  启动一个单独的窗口以运行指定的程序或命令。
  
  B           启动应用程序，但不创建新窗口。
  ```

### 调用其他bat文件

- `call 路径`

1.bat

```
@echo off
echo %1

call 2.bat %1
pause
```

2.bat

```
@echo off
net user %1

pause
```

```
F:\Desktop\批处理\ch02>1.bat milo
milo
用户名                 Milo
全名
注释
用户的注释
国家/地区代码          000 (系统默认值)
帐户启用               Yes
帐户到期               从不

上次设置密码           2020-08-11 13:13:18
密码到期               从不
密码可更改             2020-08-11 13:13:18
需要密码               No
用户可以更改密码       Yes

允许的工作站           All
登录脚本
用户配置文件
主目录
上次登录               2020-10-28 15:17:36
```

### 任务列表查看

- `tasklist`  该工具显示在本地或远程机器上当前运行的进程列表

  ```
  F:\Desktop\批处理\ch02>tasklist /FI "PID eq 16108"
  
  映像名称                       PID 会话名              会话#       内存使用
  ========================= ======== ================ =========== ============
  chrome.exe                   16108 Console                    1     33,912 K
  ```

### 任务关闭

- `taskkill`  使用该工具按照进程 ID (PID) 或映像名称终止任务。

```
 TASKKILL /IM notepad.exe
    TASKKILL /PID 1230 /PID 1241 /PID 1253 /T
    TASKKILL /F /IM cmd.exe /T
    TASKKILL /F /FI "PID ge 1000" /FI "WINDOWTITLE ne untitle*"
    TASKKILL /F /FI "USERNAME eq NT AUTHORITY\SYSTEM" /IM notepad.exe
    TASKKILL /S system /U 域\用户名 /FI "用户名 ne NT*" /IM *
    TASKKILL /S system /U username /P password /FI "IMAGENAME eq note*"
```

### 文件夹结构查看

- `tree`

  ```
  以图形显示驱动器或路径的文件夹结构。
  
  TREE [drive:][path] [/F] [/A]
  
     /F   显示每个文件夹中文件的名称。
     /A   使用 ASCII 字符，而不使用扩展字符。
  
  F:\Desktop\批处理>tree /A
  卷 办公 的文件夹 PATH 列表
  卷序列号为 A081-59AB
  F:.
  +---ch01
  \---ch02
  
  F:\Desktop\批处理>tree /A /F
  卷 办公 的文件夹 PATH 列表
  卷序列号为 A081-59AB
  F:.
  |   批处理脚本.md
  |
  +---ch01
  |       1.txt
  |       2.txt
  |
  \---ch02
          1.bat
          2.bat
  ```

### 关机

- `shutdown`

  ```
     /i         显示图形用户界面(GUI)。这必须是第一个选项。 远程关闭
      /l         注销。这不能与 /m 或 /d 选项一起使用。
      /s         关闭计算机。
  ```

### 计划任务

- `at`  命令安排在特定日期和时间运行命令和程序。
  - AT 命令已弃用。请改用 schtasks.exe。

### 环境变量

- `set`

  ```
  显示、设置或删除 cmd.exe 环境变量。
  
  SET [variable=[string]]
  
    variable  指定环境变量名。
    string    指定要指派给变量的一系列字符串。
  
  要显示当前环境变量，键入不带参数的 SET。
  
  F:\Desktop\批处理>echo %OS%
  Windows_NT
  ```

## 文件夹或文件相关命令

默认不显示隐藏目录

### 目录显示

- `dir`

```
DIR [drive:][path][filename] [/A[[:]attributes]] [/B] [/C] [/D] [/L] [/N]
  [/O[[:]sortorder]] [/P] [/Q] [/R] [/S] [/T[[:]timefield]] [/W] [/X] [/4]

  [drive:][path][filename]
              指定要列出的驱动器、目录和/或文件。

  /A          显示具有指定属性的文件。
  属性         D  目录                R  只读文件
               H  隐藏文件            A  准备存档的文件
               S  系统文件            I  无内容索引文件
               L  重新分析点          O  脱机文件
```

### 目录创建

- `mkdir` --> `md`

### 目录删除

- `rmdir` --> `rd`

### 目录切换

- `cd`

### 目录重命名

- `rename` -- > `ren`

### 目录复制

- `copy`

### 文件删除

- `del`

  `del c:\1\*.txt`

### 文件剪切

- `move`

## 网络相关命令

### 用户操作

- `net user`  查看用户
- `net user 用户名`  查看用户详细信息
- `net user 用户名 密码 /add`
- `net user 用户名 /delete`

### 用户组操作

- `net localgroup` 查看用户组
- `net localgroup administratiors 用户名 /add`  将用户添加到administratiors 用户组
- `net localgroup users 用户名 /delete` 将用户从users用户组删除

### 网络联通测试

- `ping`

  ```
  目的dao就是检测本机的回du路是否正常，如果正zhi常，则说明本机的TCP/IP协议安装正常
  
  F:\Desktop\批处理>ping 127.0.0.1
  
  正在 Ping 127.0.0.1 具有 32 字节的数据:
  来自 127.0.0.1 的回复: 字节=32 时间<1ms TTL=128
  来自 127.0.0.1 的回复: 字节=32 时间<1ms TTL=128
  来自 127.0.0.1 的回复: 字节=32 时间<1ms TTL=128
  来自 127.0.0.1 的回复: 字节=32 时间<1ms TTL=128
  
  127.0.0.1 的 Ping 统计信息:
      数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
  往返行程的估计时间(以毫秒为单位):
      最短 = 0ms，最长 = 0ms，平均 = 0ms
  ```


### 网络链接

- `telnet`  已启用

### 路由信息查看

- `tracert`

```
C:\Users\Milo>tracert www.baidu.com

通过最多 30 个跃点跟踪
到 www.a.shifen.com [180.101.49.12] 的路由:

  1     3 ms     4 ms     2 ms  192.168.10.1
  2     2 ms     2 ms     2 ms  192.168.72.1
  3     7 ms     5 ms     7 ms  124.74.48.46
  4    39 ms     6 ms     7 ms  124.74.48.41
  5     7 ms    12 ms    14 ms  101.95.41.201
  6    12 ms     8 ms    12 ms  61.152.25.66
  7    27 ms    40 ms    18 ms  202.97.74.146
  8    22 ms     *       12 ms  58.213.94.114
  9     *       14 ms     *     58.213.94.86
 10    17 ms    17 ms    15 ms  58.213.96.90
 11     *        *        *     请求超时。
 12     *        *        *     请求超时。
 13     *        *        *     请求超时。
 14     *        *        *     请求超时。
 15    48 ms    11 ms    11 ms  180.101.49.12
```

### 网络适配器

- `ipconfig`

### ARP信息

- `arp` 显示和修改地址解析协议(ARP)使用的“IP 到物理”地址转换表。

## 条件判断结构

文件路径中不能有中文

### if-else

```
@echo off
rem 演示if-else 结构 判断字符串是否为规定的字符串

rem v == hello wrong,不能有空格
set v=hello 

rem if else 必须在同一行
if %v%==hello (echo ok) else (echo no)  

pause>nul

-------------------
@echo off
if "%1"=="ker" ( 
 echo kernel
) else (
 echo dtbc
)
```

### 文件是否存在

- `exist`

```
@echo off

rem 程序用来判断当前1.bat是否存在
rem 文件路径中不能有中文
if exist F:\Desktop\批处理\ch03\12.bat (echo ok) else (echo no)

pause>nul
```

### 文件判断删除

```
@echo off
if exist F:\Desktop\a.txt (
	echo file is find!
	del F:\Desktop\a.txt
) else (
	echo file is not find
)
pause>nul
```

## 循环结构

### 遍历目录

-  `for /d %%名称 in(路径/*) do 具体操作`

  ```
  @echo off
  rem for test
  
  for /d %%a in (F:\Desktop\*) do if %%a==test rd %%a
  
  for /d %%a in (F:\Desktop\*) do echo %%a
  
  pause>nul
  ```

### 遍历删除文件

- `for /r "目录路径" %%v in (匹配规则 例如*.py) do 执行操作 %%v`

  ```
  @echo off
  rem for test
  
  for /r "F:\Desktop" %%v in (*.test) do echo %%v
  
  echo delete all *.py
  
  
  for /r "F:\Desktop" %%v in (*.test) do del %%v
  
  
  pause>nul
  ```

### 遍历数字

- `for /L %%v in (start,step,end) do 具体操作`

  ```
  @echo off
  
  for /L %%v in (1,1,20) do ping %1.%%v
  
  pause
  ```

### 遍历文件内容

- `for /F %%v in (文件名) do 具体操作`

### 目录重复新建

```
@echo off

cd cd F:\Desktop

:loop
md Virus
cd Virus
goto loop

pause>nul
exit
```

## 案例

### 交互操作

```
@echo off

echo 1.a
echo 2.b
echo 3.c
echo 4.d

:first
echo Enter you option:
rem 设置变量，使用opt接受用户的输入
set /p opt=
if %opt%==1 goto one
if %opt%==2 goto two
if %opt%==3 goto three
if %opt%==4 goto four
echo Invalid option
goto first

:one
echo your choose one
pause>nul
exit


:two
echo your choose teo
pause>nul
exit

:three
echo your choose three
pause>nul
exit

:four
echo your choose four
pause>nul
exit
```

### Bat转EXE程序

Bat to Exe Converter



## goto

```
E:\安装包>type fun.bat
@echo off
chcp 65001
call:pig
call:dog

:cat
echo 猫叫
goto:eof

:dog
echo 狗叫
goto:eof


:pig
echo 猪叫
goto:eof

pause
E:\安装包>fun.bat
Active code page: 65001
猪叫
狗叫
猫叫


```

 