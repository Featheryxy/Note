```shell

jps -l: 显示当前所有java进程的pid
jmap -heap pid: 查看堆使用情况



-Xmx：最大堆大小
-Xms：初始堆大小
```

ava整个堆大小设置，Xmx 和 Xms设置为老年代存活对象的3-4倍，即FullGC之后的老年代内存占用的3-4倍

永久代 PermSize和MaxPermSize设置为老年代存活对象的1.2-1.5倍。

年轻代Xmn的设置为老年代存活对象的1-1.5倍。

老年代的内存大小设置为老年代存活对象的2-3倍。



**如何触发FullGC ？**

​        使用jmap工具可触发FullGC 

​        jmap -dump:live,format=b,file=heap.bin <pid> 将当前的存活对象dump到文件，此时会触发FullGC

​        jmap -histo:live <pid> 打印每个class的实例数目,内存占用,类全名信息.live子参数加上后,只统计活的对象数量. 此时会触发FullGC

Reference

https://blog.csdn.net/weixin_29062865/article/details/114058225

https://blog.csdn.net/zfgogo/article/details/81260172

