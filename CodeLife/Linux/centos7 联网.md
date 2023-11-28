网络配置

桥接：使用本机的真实网卡，同网段的其他主机可以访问

NAT：VMnet8，当主机通网时，该机也可通网

Host-only：VMnet1，虚拟机只与主机通信

```
ifconfig eth0 192.168.2.2（不能设为192.168.2.1）

centos 7
ip add

本地地址：192.168.2.223
需要在同一个网段2下

临时连接网络，永久配置需要在配置文件中修改

ifconfig(interface 网卡)
eth0(ethernet 以太网， 第一块网卡)
```

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

### 联网

虚拟机设置为NAT模式

>  NAT使用VMnet8网卡，当主机通网时，该机也可通网。默认情况下和物理机同一网络中的其它机器不能访问虚拟机，但虚拟机可以访问其它物理机。可以修改NAT设置，添加主机IP：主机端口与虚拟机IP: 虚拟机端口

如果`ip addr `无网卡信息, 则修改/etc/sysconfig/network-scripts/ifcfg-ens33文件, 将ONBOOT设置为yes 来启动网卡
