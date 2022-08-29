1 查看防火墙状态

 [root@lvxinghao ~]# **systemctl status firewalld**

 

 2 查看开机是否启动防火墙服务
 [root@lvxinghao ~]# **systemctl is-enabled firewalld**

 

 3 关闭防火墙
 [root@lvxinghao ~]# **systemctl stop firewalld**
 [root@lvxinghao ~]# **systemctl status firewalld**

 4 禁用防火墙（系统启动时不启动防火墙服务）
 [root@lvxinghao ~]# **systemctl disable firewalld**
 [root@lvxinghao ~]# **systemctl is-enabled firewalld**

