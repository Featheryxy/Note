# 桥接模式

1. 选择桥接模式,
2. 网卡选择和主机网卡相同的一
3. 编辑文件ifcfg-ens33 

```
[root@localhost ~]# vi /etc/sysconfig/network-scripts/ifcfg-ens33


# 将BOOTPROTO设置为static
# 将ONBOOT设置为yes
# 并添加下列信息, 需同网段和网关下
# IPADDR=192.168.1.111
# NETMASK=255.255.255.0
# GATEWAY=192.168.1.1
# DNS1=114.114.114.114
# DNS2=114.114.115.115
# ZONE=public

TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=e51af7d0-3a49-43e8-978c-ea5440ae0be4
DEVICE=ens33
ONBOOT=yes
IPADDR=192.168.1.111
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=114.114.114.114
DNS2=114.114.115.115
ZONE=public
```

重启network

```
service network restart
```

