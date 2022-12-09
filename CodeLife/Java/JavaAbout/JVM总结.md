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

BootStrap ClassLoader

1. **加载java的核心库**（JAVA_HOME/jre/lib/rt.jar/resources.jar或sun.boot.class.path
2. 不继承自java.lang.ClassLoader,没有父加载器

ClassLoader

1. 派生于ClassLoader类