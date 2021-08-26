sz：将选定的文件发送（send）到本地机器
 rz：运行该命令会弹出一个文件选择窗口，从本地选择文件上传到服务器(receive)
 rz，sz是便是Linux/Unix同Windows进行ZModem文件传输的命令行工具，windows端需要支持ZModem的telnet/ssh客户端（比如SecureCRT）。注意：该方法的传输速度比较慢，推荐使用中小文件的传输。

```
[root@localhost ~]# rz
-bash: rz: command not found
[root@localhost ~]# ls
anaconda-ks.cfg

[root@localhost ~]# yum install lrzsz
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * extras: mirrors.cn99.com
 * updates: mirrors.cn99.com
base                                                                        | 3.6 kB  00:00:00     
docker-ce-stable                                                            | 3.5 kB  00:00:00     
extras                                                                      | 2.9 kB  00:00:00     
updates                                                                     | 2.9 kB  00:00:00     
Resolving Dependencies
--> Running transaction check
---> Package lrzsz.x86_64 0:0.12.20-36.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================
 Package             Arch                 Version                         Repository          Size
===================================================================================================
Installing:
 lrzsz               x86_64               0.12.20-36.el7                  base                78 k

Transaction Summary
===================================================================================================
Install  1 Package

Total download size: 78 k
Installed size: 181 k
Is this ok [y/d/N]: y
Downloading packages:
lrzsz-0.12.20-36.el7.x86_64.rpm                                             |  78 kB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : lrzsz-0.12.20-36.el7.x86_64                                                     1/1 
  Verifying  : lrzsz-0.12.20-36.el7.x86_64                                                     1/1 

Installed:
  lrzsz.x86_64 0:0.12.20-36.el7                                                                    

Complete!
```

rz的用法
 在命令终端输入rz回车后，就会出现文件选择对话框，选择需要上传文件，一次可以指定多个文件，上传到服务器的路径为当前执行rz命令的目录。