### 版本

apache-tomcat-9.0.36-windows-x64.

### 环境变量设置

CATALINA_HOME

F:\apache-tomcat-9.0.36

增加Path

%CATALINA_HOME%\bin

校验是否成功，在cmd中输入catalina run

```
C:\Users\yt>catalina run
Using CATALINA_BASE:   "F:\apache-tomcat-9.0.36"
Using CATALINA_HOME:   "F:\apache-tomcat-9.0.36"
Using CATALINA_TMPDIR: "F:\apache-tomcat-9.0.36\temp"
Using JRE_HOME:        "D:\Java\jdk1.8.0_151"
```

在浏览器中输入localhost:8080进入Tomcat官网

### tomcat日志乱码

方法一：

修改属性文件：D:\apache-tomcat-9.0.36\conf\logging.properties

将所有的UTF-8换成GBK

```
# java.util.logging.ConsoleHandler.encoding = UTF-8
java.util.logging.ConsoleHandler.encoding = GBK
```

Windows系统的cmd是GBK编码的，所以IDEA的下方log输出的部分的编码也是GBK的，然而Tomcat 9.0 版本默认log输出是UTF-8编码的，采用了两种不同的编码方式就会导致乱码。

方法二：

IDEA修改VM选项

help --> Edit Coustom VM Option 添加-Dfile.encoding=UTF-8 ---> Edit Configuration 

https://www.cnblogs.com/benchover/p/10773098.html

### Idea创建Web项目

New Project ----> Java Enterprise ------->  Web Application

### Idea 设置

run--> Edit Configurations

点击加号---> Tomcat ----> local

Server ---> Application server：中选中本地安装的tomcat路径

Deployment ---> Deploy at the server startup 中添加项目 ---> 将Application context（上下文路径）: 设置成 /



