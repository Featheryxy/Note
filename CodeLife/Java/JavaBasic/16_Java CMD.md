# Java命令

```shell
java [options] <主类> [args...]

# 编译java文件，生成.class文件
javac Hello.java
# 运行
java Hello

# cp:classpath 
# -d 编译文件输出路径
java -d out_dir -encoding gb2312 -cp pathToJar Hello

java -jar demo.jar
```

Java是通过java虚拟机来装载和执行编译文件（class文件）的，java虚拟机通过命令java 　option 来启动，-option为虚拟机参数，通过这些参数可对虚拟机的运行状态进行调整.

**一、如何查看参数列表**:

虚拟机参数分为基本和扩展两类，在命令行中输入java 可得到基本参数列表，java 　X 则可得到扩展参数列表。

**注**：以上假设已经把JAVA_HOME\bin路径加入到了path路径

**二、基本参数说明**：

**1. -classpath,-cp**

虚拟机在运行一个类时，需要将其装入内存，虚拟机搜索类的方式和顺序如下：

Bootstrap classes，Extension classes，User classes。

Bootstrap 中的路径是虚拟机自带的jar或zip文件，虚拟机首先搜索这些包文件，用System.getProperty("sun.boot.class.path")可得到虚拟机搜索的包名。

Extension是位于jre"lib"ext目录下的jar文件，虚拟机在搜索完Bootstrap后就搜索该目录下的jar文件。用System. getProperty("java.ext.dirs”)可得到虚拟机使用Extension搜索路径。

User classes搜索顺序为当前目录、环境变量 CLASSPATH、-classpath。

-cp 和 -classpath 是同义词，参数意义是一样的。classpath参数太长了，所以提供cp作为缩写形式,它们用于告知虚拟机搜索目录名、jar文档名、zip文档名，之间用分号;分隔。

例如当你自己开发了公共类并包装成一个common.jar包，在使用 common.jar中的类时，就需要用-classpath common.jar 告诉虚拟机从common.jar中查找该类，

否则虚拟机就会抛出java.lang.NoClassDefFoundError异常，表明未找到类定义。

在运行时可用System.getProperty(“java.class.path”)得到虚拟机查找类的路径。

使用-classpath后虚拟机将不再使用CLASSPATH中的类搜索路径，如果-classpath和CLASSPATH都没有设置，则虚拟机使用当前路径(.)作为类搜索路径。

推荐使用-classpath来定义虚拟机要搜索的类路径，而不要使用环境变量 CLASSPATH的搜索路径，以减少多个项目同时使用CLASSPATH时存在的潜在冲突。

例如应用1要使用a1.0.jar中的类G，应用2要使用 a2.0.jar中的类G,a2.0.jar是a1.0.jar的升级包，当a1.0.jar，a2.0.jar都在CLASSPATH中，虚拟机搜索到第一个包中的类G时就停止搜索，

如果应用1应用2的虚拟机都从CLASSPATH中搜索，就会有一个应用得不到正确版本的类G。

**实例1**：java -classpath lib\Launcher.jar com.teleca.robin.Launcher getProcessState.bat 5000

**实例2**：java -classpath classes com.teleca.robin.Launcher getProcessState.bat 5000

如果需要指定各个JAR文件具体的存放路径，相同路径有多个可使用通配符。

**示例1**：

java -cp .;c:\classes\myClass.jar;d:\classes\*.jar packname.mainclassname

**实例3**：

java -cp lib\*.jar com.teleca.robin.Launcher getProcessState.bat 5000

**实例3-1：**

java -cp Util.jar**;**lib\sqljdbc.jar com.harry.j2se.AppEntrance

**2.-D<propertyName>=value**

在虚拟机的系统属性中设置属性名/值对，运行在此虚拟机之上的应用程序可用System.getProperty(“propertyName”)得到value的值。

如果value中有空格，则需要用双引号将该值括起来，如-Dname=”space string”。

该参数通常用于设置系统级全局变量值，如配置文件路径，应为该属性在程序中任何地方都可访问。

**示例1**：

设置虚拟机使用的Extension搜索路径

java -Djava.ext.dirs=lib MyClass

**3. -client，-server**

这两个参数用于设置虚拟机使用何种运行模式，client模式启动比较快，但运行时性能和内存管理效率不如server模式，通常用于客户端应用程序。相反，server模式启动比client慢，但可获得更高的运行性能。

在windows上，缺省的虚拟机类型为client模式，如果要使用 server模式，就需要在启动虚拟机时加-server参数，以获得更高性能，对服务器端应用，推荐采用server模式，尤其是多个CPU的系统。在 Linux，Solaris上缺省采用server模式。

**4. -hotspot**

含义与client相同，jdk1.4以前使用的参数，jdk1.4开始不再使用，代之以client。

**5. -verbose[:class|gc|jni]**

在输出设备上显示虚拟机运行信息。

verbose和verbose:class含义相同，输出虚拟机装入的类的信息，显示的信息格式如下：

[Loaded java.io.FilePermission$1 from shared objects file]

当虚拟机报告类找不到或类冲突时可用此参数来诊断来查看虚拟机从装入类的情况。

**6. -verbose:gc**

在虚拟机发生内存回收时在输出设备显示信息，格式如下：

[Full GC 268K->168K(1984K), 0.0187390 secs]

该参数用来监视虚拟机内存回收的情况。

**7.-verbose:jni**

在虚拟机调用native方法时输出设备显示信息，格式如下：

[Dynamic-linking native method HelloNative.sum ... JNI]

该参数用来监视虚拟机调用本地方法的情况，在发生jni错误时可为诊断提供便利。

**9.-version**

显示可运行的虚拟机版本信息然后退出。一台机器上装有不同版本的JDK时

**10.-showversion**

显示版本信息以及帮助信息。

**11.-ea[:<packagename>...|:<classname>]**和**-enableassertions[:<packagename>...|:<classname>]**

从JDK1.4开始，java可支持断言机制，用于诊断运行时问题。通常在测试阶段使断言有效，在正式运行时不需要运行断言。断言后的表达式的值是一个逻辑值，为true时断言不运行，为false时断言运行，抛出java.lang.AssertionError错误。

上述参数就用来设置虚拟机是否启动断言机制，缺省时虚拟机关闭断言机制，用-ea 可打开断言机制，不加<packagename>和classname时运行所有包和类中的断言，如果希望只运行某些包或类中的断言，可将包名或类名加到-ea之后。例如要启动包com.foo.util中的断言，可用命令 　ea:com.foo.util 。

**注**：ea是enableassertions的缩写

**12**.**-da[:<packagename>...|:<classname>]**和-**disableassertions[:<packagename>...|:<classname>]**

用来设置虚拟机关闭断言处理，packagename和classname的使用方法和-ea相同。

**注**：da应该是disableassertions的缩写

**13**.**-esa** 和**-enablesystemassertions**

设置虚拟机显示系统类的断言。

**注**：esa是enablesystemassertions的缩写

**15.-dsa** 和**-disablesystemassertions**

设置虚拟机关闭系统类的断言。

**注**：dsa是disablesystemassertions的缩写

**16.-agentlib:<libname>[=<options>]**

该参数是JDK5新引入的，用于虚拟机装载本地代理库。

Libname为本地代理库文件名，虚拟机的搜索路径为环境变量PATH中的路径，options为传给本地库启动时的参数，多个参数之间用逗号分隔。在Windows平台上虚拟机搜索本地库名为libname.dll的文件，在Unix上虚拟机搜索本地库名为libname.so的文件，搜索路径环境变量在不同系统上有所不同，Linux、SunOS、IRIX上为LD_LIBRARY_PATH，AIX上为LIBPATH，HP-UX上为SHLIB_PATH。

例如可使用-agentlib:hprof来获取虚拟机的运行情况，包括CPU、内存、线程等的运行数据，并可输出到指定文件中，可用-agentlib:hprof=help来得到使用帮助列表。在jre"bin目录下可发现hprof.dll文件。

**17. -agentpath:<pathname>[=<options>]**

设置虚拟机按全路径装载本地库，不再搜索PATH中的路径。其他功能和agentlib相同。

**18.-javaagent:<jarpath>[=<options>]**

虚拟机启动时装入java语言设备代理。Jarpath文件中的mainfest 文件必须有Agent-Class属性。代理类要实现public static void premain(String agentArgs, Instrumentation inst)方法。当虚拟机初始化时，将按代理类的说明顺序调用premain方法。

**三、扩展参数说明**

**1.-Xmixed**

设置-client模式虚拟机对使用频率高的方式进行Just-In-Time编译和执行，对其他方法使用解释方式执行。该方式是虚拟机缺省模式。

**2.-Xint**

设置-client模式下运行的虚拟机以解释方式执行类的字节码，不将字节码编译为本机码。

**3. -Xbootclasspath:path和-Xbootclasspath/a:path**及**-Xbootclasspath/p:path**

改变虚拟机装载缺省系统运行包rt.jar而从-Xbootclasspath中设定的搜索路径中装载系统运行类。除非你自己能写一个运行时，否则不会用到该参数。

/a:将在缺省搜索路径后加上path 中的搜索路径。

/p:在缺省搜索路径前先搜索path中的搜索路径。

**4.-Xnoclassgc**

关闭虚拟机对class的垃圾回收功能。

**5.-Xincgc**

启动增量垃圾收集器，缺省是关闭的。增量垃圾收集器能减少偶然发生的长时间的垃圾回收造成的暂停时间。但增量垃圾收集器和应用程序并发执行，因此会占用部分CPU在应用程序上的功能。

**6.-Xloggc:<file>**

将虚拟机每次垃圾回收的信息写到日志文件中，文件名由file指定，文件格式是平文件，内容和-verbose:gc输出内容相同。

**7.-Xbatch**

虚拟机的缺省运行方式是在后台编译类代码，然后在前台执行代码，使用-Xbatch参数将关闭虚拟机后台编译，在前台编译完成后再执行。

**8-Xms<size>**

设置虚拟机可用内存堆的初始大小，缺省单位为字节，该大小为1024的整数倍并且要大于1MB，可用k(K)或m(M)为单位来设置较大的内存数。初始堆大小为2MB。

例如：-Xms6400K，-Xms256M

**9.-Xmx<size>**

设置虚拟机内存堆的最大可用大小，缺省单位为字节。该值必须为1024整数倍，并且要大于2MB。可用k(K)或m(M)为单位来设置较大的内存数。缺省堆最大值为64MB。

例如：-Xmx81920K，-Xmx80M

当应用程序申请了大内存运行时虚拟机抛出java.lang.OutOfMemoryError: Java heap space错误，就需要使用-Xmx设置堆的最大值

**10.-Xss<size>**

设置线程栈的大小，缺省单位为字节。与-Xmx类似，也可用K或M来设置较大的值。通常操作系统分配给线程栈的缺省大小为1MB。

另外也可在java中创建线程对象时设置栈的大小，构造函数原型为Thread(ThreadGroup group, Runnable target, String name, long stackSize)。

**11.-Xprof**

输出CPU运行时的诊断信息。

**12.-Xfuture**

对类文件进行严格格式检查，以保证类代码符合类代码规范。为保持向后兼容，虚拟机缺省不进行严格的格式检查。

**13.-Xrs**

减少虚拟机中操作系统的信号（singals）的使用。该参数通常用在虚拟机以后台服务方式运行时使用（如Servlet）。

**14.-Xcheck:jni**

调用JNI函数时进行附加的检查，特别地虚拟机将校验传递给JNI函数参数的合法性，在本地代码中遇到非法数据时，虚拟机将报一个致命错误而终止。使用该参数后将造成性能下降。

[https://www.cnblogs.com/princessd8251/articles/4025140.html](https://www.cnblogs.com/princessd8251/articles/4025140.html)