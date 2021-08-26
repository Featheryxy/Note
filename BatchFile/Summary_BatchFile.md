# 概述



# 常用命令

```bash
命令 /?  帮助命令
rem 注释
echo 打印
@echo off 关闭盘符输出
pause 暂停,请按任意键继续
exit 退出当前操作，关闭batchfile
echo %path% 打印变量path
chcp 65001 > nul 改为utf-8编码

%1, %2, ... 传参
start 开启新的命令行窗口

SET 显示当前环境变量
SET [variable=[string]]   变量定义与赋值
SET /P variable=[promptString]
%variable%  变量取值
```

# 目录

```
dir 显示当前目录下的文件和目录
CD  显示当前目录名
CD [/D] [drive:][path]  改变当前目录
```

# 端口占用

```
# 查看指定port id的PID
netstat -aon|findstr "port id"

# 查看指定PID的进程
tasklist|findstr "PID"

# 结束进程
taskkill /T /F /PID PID 
 /T 包括子进程
```





```bash
E:\GitHubNote\BatchFile\ch02>type test.bat
@echo off
rem 打印 "hello world"

echo hello world %1
pause>nul
E:\GitHubNote\BatchFile\ch02>test.bat milo
hello world milo
```





