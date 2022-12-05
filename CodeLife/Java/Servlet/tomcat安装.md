### 版本

apache-tomcat-9.0.36-windows-x64.

### 目录

```markdown
bin: 存放二进制可执行文件
conf：
- server.xml配置整个服务器信息（如端口号，编码格式），
- web.xml部署描述符文件，该文件种注册了很多MIME类型
- server.xml可以设置端口号、设置域名或IP、默认加载的项目、请求编码
- web.xml可以设置tomcat支持的文件类型
- context.xml可以用来配置数据源之类的
- tomcat-users.xml用来配置管理tomcat的用户与权限
- 在Catalina目录下可以设置默认加载的项目
lib
logs
temp
webapps：存放web项目的目录，其中每个文件夹都是一个项目，可以以文件夹、war包、jar包的形式发布应用；其中ROOT是一个特殊的项目，在地址栏中没有给出项目目录时，对应的就是ROOT项目
work：运行时编译后文件，最终运行的文件都在这里。当客户端用户访问一个JSP文件时，Tomcat会通过JSP生成Java文件，然后再编译Java文件生成class文件，生成的Java和class文件都会存放到这个目录下。清空work目录，然后重启tomcat，可以达到清除缓存的作用。
```

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

Deployment ---> Deploy at the server startup 中添加项目 

ps: 注意href中写的地址应该与web.xml中的mapping路径一致

```html
<a href="/2FirstServletWebApp/anypath1">HelloServlet</a>


<servlet>
    <servlet-name>servlet-name1</servlet-name>
    <servlet-class>HelloServlet</servlet-class>
</servlet>
<servlet-mapping>
    <servlet-name>servlet-name1</servlet-name>
    <!--虚拟路径，代表一个资源的名称，必须以"/"开头, 可以多个-->
    <url-pattern>/anypath1</url-pattern>
</servlet-mapping>
```



>  将Application context（上下文路径）: 设置成 /



