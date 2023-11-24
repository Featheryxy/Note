JVM 只关心字节码文件（.class文件）

#### 代码执行流程

java程序.java--（编译javac）-->字节码文件.class-->类装载子系统化身为反射类Class--->运行时数据区

#### JVM架构

类加载子系统（Class loader SubSystem）

运行时数据区（Runtime Data Area）

- 线程共享：方法区（Method Area， jdk8中叫做永久代，元空间 Metaspace ），堆区（heap）

- 线程私有：Java栈（Java stack），本地方法栈（Native Method Stack），程序计数器（Program Counter Register）

执行引擎（Execution Engine）

#### Class loader SubSystem

类加载子系统

将class文件加载到方法区的内存空间中

类加载过程：

加载（Loading）

----> 链接 （Linking）= 验证（Verification）+ 准备（Preparation）+ 解析（Resolution）

----> 初始化（Initialization）

#### Loading

1. 通过一个类的**全限定名**获取定义此类的**二进制字节流**；
2. 将这个字节流所代表的的**静态存储结构**保存在**方法区**中；
3. 在内存中生成一个代表这个类的**java.lang.Class对象**

#### Linking

1. 为类变量（静态变量）在**方法区**中分配内存并附**默认值**，如int类型默认赋0值
2. final static 变量在编译时进行宏替换
3. 实例变量在new后进行初始化并分在在堆中

#### Initiallization

1. 执行类构造器方法clinit（class or interface initialization method），为**类变量进行赋值**
2. 有静态代码块---> 有类构造器方法clinit（）
3. 先初始化父类中的类变量，再初始化子类

#### ClassLoader

BootStrap ClassLoader 引导类加载器

1. **加载java的核心库**（JAVA_HOME/jre/lib/rt.jar/resources.jar或sun.boot.class.path
2. 不继承自java.lang.ClassLoader,没有父加载器

Extension ClassLoader 扩展类加载器，加载/jdk/jre/lib/ext下的类

Application Class Loader：应用程序类加载器：也称为用户自定义类加载器，它是用来加载应用程序自己编写的类，也就是classpath路径下的类。应用程序类加载器是由Java编写的，它继承自java.lang.ClassLoader类。

System ClassLoader 系统类加载器：搜索CLASSPATH中指明的路径和JVR文件

#### 双亲委派机制

指在类加载时，如果一个类加载器收到了加载一个类的请求，它首先不会自己去加载这个类，而是把这个请求委派给父类加载器去处理，如果父类加载器还存在父类加载器，则会继续向上委托，一直到最顶层的启动类加载器。只有当父类加载器无法完成类的加载时，子加载器才会尝试自己去加载。

优点：

1. 避免类的重复加载
2. 保护程序安全，防止核心API被随意修改，沙箱安全机制

#### 同一个类

在jvm中，即使这两个类对象（class对象）来源同一个Class文件，被同一个虚拟机所加载，但只要加载它们的ClassLoader实例对象不同，那么这两个类对象也是不相等的.



类变量  方法区

成员变量  堆内存

局部变量   栈内存
