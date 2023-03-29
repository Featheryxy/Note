<img src="C:\Users\zhang\AppData\Roaming\Typora\typora-user-images\image-20210309205854677.png" alt="image-20210309205854677" style="zoom: 80%;" />

### 字符型常量与字符串常量的区别？

1.形式上：字符型 ' '  字符串 " "

2.含义上：字符常量是一个整型值（ASCII值），可以参加表达式运算。字符串常量代表一个地址值（该字符串在内存中存放位置）

3.内存上：字符常量占2个字节；字符串常量占若干个字节



### String / StringBuffer / StringBuilder

- 可变性：
  - String：`private final char value[]`，不可变
  - StringBuilder 与 StringBuffer都继承自 AbstractStringBuilder 类，使用 `char [] value`，没有使用final, 可变的
- 线程安全：
  - String不可变，线程安全，StringBuffer对方法加了同步锁，线程安全
  - StringBuilder没有添加同步锁，非线程安全
- 性能：
  - 每次对String类型进行改变的时候，都会生成一个新的Sting对象，然后将指针指向新的String对象。性能低
  - StringBuffer，有同步锁，性能低
  - StringBuilder，性能高



**补充：**

操作字符串的类有：String、StringBuffer、StringBuilder。

String 和 StringBuffer、StringBuilder 的区别在于 String 声明的是不可变的对象，每次操作都会生成新的 String 对象，然后将指针指向新的 String 对象，而 StringBuffer、StringBuilder 可以在原有对象的基础上进行操作，所以在经常改变字符串内容的情况下最好不要使用 String。

StringBuffer 和 StringBuilder 最大的区别在于，StringBuffer 是线程安全的，而 StringBuilder 是非线程安全的，但 StringBuilder 的性能却高于 StringBuffer，所以在单线程环境下推荐使用 StringBuilder，多线程环境下推荐使用 StringBuffer。



**扩展：**

**String str="i"与 String str=new String(“i”)一样吗？**

不一样，因为内存的分配方式不一样。String str="i"的方式，Java 虚拟机会将其分配到常量池中；而 String str=new String(“i”) 则会被分到堆内存中。



**如何将字符串反转？**
使用 StringBuilder 或者 stringBuffer 的 reverse() 方法。

示例代码：

```java
// StringBuffer reverse
StringBuffer stringBuffer = new StringBuffer();
stringBuffer.append(“abcdefg”);
System.out.println(stringBuffer.reverse()); // gfedcba

// StringBuilder reverse
StringBuilder stringBuilder = new StringBuilder();
stringBuilder.append(“abcdefg”);
System.out.println(stringBuilder.reverse()); // gfedcba
```



**String 类的常用方法都有哪些？**

 indexOf()：返回指定字符的索引。
 charAt()：返回指定索引处的字符。
 replace()：字符串替换。
 trim()：去除字符串两端空白。
 split()：分割字符串，返回一个分割后的字符串数组。
 getBytes()：返回字符串的 byte 类型数组。
 length()：返回字符串长度。
 toLowerCase()：将字符串转成小写字母。
 toUpperCase()：将字符串转成大写字符。
 substring()：截取字符串。
 equals()：字符串比较。



### Overload / Override 重载和重写

- Overload表示同一个类中可以有多个名称相同的方法，但这些方法的**参数列表各不相同**（即**参数个数或类型不同**）。

  - 参数列表相同，返回值不同。Error, 二义性，即JVM不知道调用哪个函数。
  - 对于继承来说，如果某一方法在父类中是访问权限是priavte，那么就不能在子类对其进行重载，如果定义的话，也只是定义了一个新方法，而不会达到重载的效果。

  ```java
  // Error:(21, 19) java: 已在类 test.ShortTest中定义了方法 say(java.lang.String)
  //    static void say(String name){
  //        System.out.println("hello"+name);
  //    }
  
      static String say(String name){
          return name;
      }
  ```

- 重写Override表示子类中的方法可以与父类中的某个方法的**名称和参数完全相同**，**覆盖**

  - 覆盖的方法的**返回值**必须和被覆盖的方法的返回**一致**；
  - 覆盖的方法所**抛出的异常**必须和被覆盖方法的所抛出的异常**一致**，**或者是其子类**；
  - **被覆盖的方法不能为private**，否则在其子类中只是新定义了一个方法，并没有对其进行覆盖。

  

### ==hashcode和equals==

1. 如果两个对象相等，则 hashcode ⼀定也是相同的
2. 两个对象相等,对两个对象分别调⽤ equals ⽅法都返回 true
3. 两个对象有相同的 hashcode 值，它们也不⼀定是相等的（因为不同的地址可能会计算出相同的hash值）
4. 因此， equals ⽅法被覆盖过，则 hashCode ⽅法也必须被覆盖
5. hashCode() 的默认行为是对堆上的对象产⽣独特值。如果没有重写 hashCode()，则该 class的两个对象⽆论如何都不会相等（即使这两个对象指向相同的数据）  



判断两个对象同否相等就是看内容是不是一样，但hashCode()默认是根据对象在堆里的地址来产生哈希值的，相同内容的两个对象何来“他们hashcode本来相等”呢？





### 为什么要有hashcode?

hashcode() 为了提高查询的效率，但是hashcode不一定可靠，有时不同的对象生成的hashcode会一样。



### equals

- Object中，equals()方法使用==来比较两个对象是否相等，即比较两个对象的内存地址是否相同。

- equals() 相等的两个对象他们的hashCode() 一定相等，但hashCode()相等的两个对象他们的equals()不一定相等。

所以只要重写equals,就必须重写hashCode; 因为Set存储的是不重复对象，所以Set一定要重写这两个方法，如果使用自定义对象作为Map的key，则必须重写hashCode和equals。String 重写了hashCode和equals 方法。

当使用hash时重写hashCode, e.g.: HashTable, HashMap, HashSet

引用数据类型：数组，类，接口，在Java虚拟机栈中存储对象的引用，在堆中存储对象的实例

基本数据类型：8个，byte,short,int,long, float,double,char,boolean。直接存储在Java虚拟机栈中



### 7.==与equals的区别？

==：判断两个对象的地址是否相等，即是否是同一个对象

- 基本类型只能使用==，不能使用equals(), 包装类使用equals(), 不能使用= =

equals()：在object类中，等价于==

- 类没有覆盖equals()方法，等价于==
- 类覆盖equals()方法后，判断两个对象内容是否相等，String类中的equals()方法被重写过。



**补充**：对于基本数据类型和引用数据类型，==的作用效果是不一样的。

基本类型：比较的是值是否相同；
引用类型：比较的是引用是否相同；

代码示例：

```java
String x = “string”;
String y = “string”;
String z = new String(“string”);
System.out.println(x == y); // true
System.out.println(x == z); // false
System.out.println(x.equals(y)); // true
System.out.println(x.equals(z)); // true
```

**代码解读：**因为 x 和 y 指向的是同一个引用，所以 == 也是 true，而 new String()方法则重写开辟了内存空间，所以 == 结果为 false，而 equals 比较的一直是值，所以结果都为 true。



**equals 解读**

equals 本质上就是 ==，只不过 String 和 Integer 等重写了 equals 方法，把它变成了值比较。看下面的代码就明白了。

首先来看默认情况下 equals 比较一个有相同值的对象，代码如下：

```java
class Cat {
	public Cat(String name) {
 		this.name = name;
	}

	private String name;

	public String getName() {

  		return name;
	}

	public void setName(String name) {

  		this.name = name;
	}
}

Cat c1 = new Cat(“王磊”);
Cat c2 = new Cat(“王磊”);

System.out.println(c1.equals(c2)); // false
```


 输出结果出乎我们的意料，竟然是 false？这是怎么回事，看了 equals 源码就知道了，源码如下：

```java
public boolean equals(Object obj) {
 return (this == obj);
}
```


原来 equals 本质上就是 ==。

那问题来了，两个相同值的 String 对象，为什么返回的是 true？代码如下：

```java
String s1 = new String(“老王”);
String s2 = new String(“老王”);
System.out.println(s1.equals(s2)); // true
```

 同样的，当我们进入 String 的 equals 方法，找到了答案，代码如下：

```java
public boolean equals(Object anObject) {
 	if (this == anObject) {
 		return true;
 	}
    
 	if (anObject instanceof String) {
 		String anotherString = (String)anObject;
 		int n = value.length;
 		if (n == anotherString.value.length) {
 			char v1[] = value;
 			char v2[] = anotherString.value;
 			int i = 0;
 			while (n-- != 0) {
 			if (v1[i] != v2[i])
 				return false;
 				i++;
			 }
		 return true;
	 	}
 	}
    
 	return false;
}
```

原来是 String 重写了 Object 的 equals 方法，把引用比较改成了值比较。

**总结 ：**== 对于基本类型来说是值比较，对于引用类型来说是比较的是引用；而 equals 默认情况下是引用比较，只是很多类重写了 equals 方法，比如 String、Integer 等把它变成了值比较，所以一般情况下 equals 比较的是值是否相等。



### **8.动态语言  /  静态语言？**

动态类型语言是指在运行期间才去做数据类型检查的语言，也就是说，在用动态类型的语言编程时，永远也不用给任何变量指定数据类型，该语言会在你第一次赋值给变量时，在内部将数据类型记录下来。静态类型语言与动态类型语言刚好相反，它的数据类型是在编译其间检查的，也就是说在写程序时要声明所有变量的数据类型，C/C++是静态类型语言的典型代表，其他的静态类型语言还有C#、JAVA等。



### 9.intern()

- str.intern(): 判断字符串常量池中是否存在str值，

  - 如果常量池中有，则不会放入常量池，返回已有的常量池中的对象的地址
  - 如果没有，把对象的**引用地址复制**一份，放入常量池中，返回常量池中的引用地址  

  - ("a"+"b"+"c").intern() == "abc" // true


- str.toString() ---> 约等于 new String();  

  - 存储在堆中

s1 + s2 的执行细节：
\1. StringBuilder s = new StringBuilder();
\2. s.append(a);
\3. s.append(b);  



- new String("ab")会创造几个对象
  - 两个对象
  - new 关键字在堆空间创建的
  - 字符串常量池中的对象  

```java
 @org.junit.Test
    public void test(){
         // s: 堆， s2:堆, "ab":堆
        String s = new String("a") + new String("b");
        String s2 = s.intern(); // s2保存s的地址
        System.out.println(s == s2); // true
        System.out.println(s2 == "ab"); // true
        System.out.println(s == "ab"); // true

    }
    
        // x: 常量池，s：堆，s2：常量池， "ab": 常量池
        String x = "ab";
        String s = new String("a") + new String("b");
        String s2 = s.intern(); // s2保存x的地址
        System.out.println(s == x); // false
        System.out.println(s2 == x); // true
        System.out.println(s == "ab"); // false
        System.out.println(x == "ab"); // true


        // s1：堆，s2: 常量池
        String s1 = new String("ab"); 
        s1.intern(); // 常量池中已经存在"ab"
        String s2 = "ab"; // s2 直接指向常量池中的“ab”
        System.out.println(s1 == s2); // false;

        // s1：堆， s2:堆
        String s1 = new String("a") + new String("b");
        s1.intern(); // 常量池中不存在"ab",将"ab" 的引用放入常量池中，堆中的地址
        String s2 = "ab"; // s2 保存常量池中的"ab"的引用地址，即s1
        System.out.println(s1 == s2); // true;
```



### 10.对象实例化的过程

```java
Person person = new Person()
```

1. 加载类元信息 `Person person `
  2. 为对象分配内存  `new `
  3. 属性的默认初始化（零值初始化） `Person()`
  4. 设置对象头的信息
  5. 属性的显式初始化，代码块中初始化，构造器中初始化  



### 11.反射

反射指的是在运行时能够分析类的能力的程序。
反射机制可以用来：
1.在运行时分析类的能力--检查类的结构--所用到的就是java.lang.reflect包中的Field、Method、Constructor，分别用于描述类的与、方法和构造器。A中的Class类在java.lang中。
2.在运行时查看对象。
3.实现通用的数组操作代码。
反射机制的功能：
在运行时判断任意一个对象所属的类；在运行时构造任意一个类的对象；在运行时判断任意一个类所具有的成员变量和方法；在运行时调用任意一个对象的方法；生成动态代理。
反射机制常见作用：
动态加载类、动态获取类的信息（属性、方法、构造器）；动态构造对象；动态调用类和对象的任意方法、构造器；动态调用和处理属性；获取泛型信息（新增类型：ParameterizedType,GenericArrayType等）；处理注解（反射API:getAnnotationsdeng等）。
反射机制性能问题：
反射会降低效率。
void setAccessible(boolean flag):是否启用访问安全检查的开关，true屏蔽Java语言的访问检查，使得对象的私有属性也可以被查询和设置。禁止安全检查，可以提高反射的运行速度。
可以考虑使用：cglib/javaassist操作。



### 在javabean中要求提供一个public的空参构造器。

1. 



### 12.基本数据类型

**字节型（byte）** 1个字节 byte b = 10

**short** 2个字节 short s = 10

**int**  4个字节 int i = 10

**long**  8个字节 long o = 10L



**float** 4个字节 单精度，尾数精确到七位。float f = 10.0F

**double** 8个字节 双精度，经度是float的两倍，通常采用此。double d = 10.0



**字符型（char）** 2个字节 采用Unicode编码，可以直接使用Unicode值来表示字符型变量，‘\uXXXX’，XXXX代表十六进制，'\u00a' 表示 '\n'。



**boolean** false true



### short

```java
        short s1 = 1;
//      s1 = s1+1;  // Error:(6, 16) java: 不兼容的类型: 从int转换到short可能会有损失
        s1 += 1; // 编译器（javac）优化，short var2 = (short)(var1 + 1);
```



### 13.final

（1）修饰类

该类无法被继承

==该类中的方法无法被覆盖==

（2）修饰方法

该方法==可以被继承==，无法被重写（Override）

**优点：**

​	可以防止子类修改该方法的意义和实现，更为高效，编译器在遇到调用final方法转入内嵌机制，提高执行效率。

​	ps:父类中的private方法不能被子类覆盖，因此private方法默认是final型的。



（3）修饰变量

该变量变为常量

特点：可以先声明，不给初值，称作final空白，使用前必须被初始化，一旦被赋值，无法改变。



==（4）修饰参数==

1. 用final修饰参数时，可以读取该参数，但是不能对其作出下修改

```java
//      final关键字修饰一个变量时，是指其引用不能变
        final  StringBuffer a = new StringBuffer("immutable");

//      a = new StringBuffer(""); // Error:(11, 9) java: 无法为最终变量a分配值
        a.append(" broken");
        System.out.println(a); // immutable broken
```



**补充：**

final 修饰的类叫最终类，该类不能被继承。
final 修饰的方法不能被重写。
final 修饰的变量叫常量，常量必须初始化，初始化之后值就不能被修改。

### 14.sout

```java
System.out.println()
//system是java.lang中的一个类，out是System内的一个成员变量，这个变量是一个java.io.PrintStream类的对象，println就是一个方法了。
```



### ==15.泛型==

​	泛型仅仅是java的一颗语法糖，它不会影响java虚拟机生成的汇编代码，在编译阶段，虚拟机就会把泛型的类型擦除，还原成没有泛型的代码，顶多编译速度稍微慢一些，执行速度是完全没有什么区别的



### 16.String是否可变

```java
// String 对象不可变 只是 s 指向了 "hello world"
String s = "hello";
s += " world";
System.out.println(s); // hello world
```



### 17.for的遍历顺序

```java
static boolean foo(char c){
    System.out.print(c);
    return true;
}

public static void main(String[] args){
    int i = 0;
    for(foo('A'); foo('B') && (i<2); foo('C')){
        i++;
        foo('D');
    }
}

// ABDCBDCB
```



### 18.super和this

super： 只调用直接父类的构造器，必须写在子类构造方法的第一行，否则编译不通过

this：只能在类中的非静态方法中使用，静态方法和静态代码块（static 修饰）中绝对不能出现this

- static 修饰的方法或代码块在类加载过程中的Initialization被执行 
- 在类中调用构造器 A(x)    `this(x)`



### super this

由于this函数指向的构造函数默认有super()方法

### ++

```java
public void test() {
    int a = 10;
    System.out.println(a++ + a--); //
}
```



### 19.包

1.把功能相似或相关的类或接口组织在同一个包中，方便类的查找和使用。

2.如同文件夹一样，包也采用了树形目录的存储方式。同一个包中的类名字是不同的，不同的包中的类的名字是可以相同的，当同时调用两个不同包中相同类名的类时，应该加上包名加以区别。因此，包可以避免名字冲突。

3.包也限定了访问权限，拥有包访问权限的类才能访问某个包中的类。
Java使用包（package）这种机制是为了防止命名冲突，访问控制，提供搜索和定位类（class）、接口、枚举（enumerations）和注释（annotation）等。



### 20.Java创建对象的几种方式

1. ```java
   new person
   ```

2. 通过反射手段，调用`java.lang.Class`或`java.reflect.Constructor`的`newInstance()`方法

3. 调用对象的`clone()`方法

4. 运用反序列化手段，调用`java.io.ObjectInputStream`对象的`readObject()`方法

5. 静态工厂



### 21.构造函数

- 构造函数可以被过载，但不可以被重写
- 子类不继承父类的构造方法，而是必须调用其父类的构造方法
- 构造方法没有返回值，普通的类方法有返回值，可以和类名同名。
- 构造方法不能被对象调用，只会创建对象，使用new关键字



### 22.abstract的method是否可同时是static,是否可同时是native，是否可同时是synchronized?

 abstract的method不可以是static的，因为抽象的方法是要被子类实现的，而static与子类扯不上关系！

​    native方法表示该方法要用另外一种依赖平台的编程语言实现的，不存在着被子类实现的问题，所以，它也不能是抽象的，不能与abstract混用。例如，FileOutputSteam类要硬件打交道，底层的实现用的是操作系统相关的api实现；例如，在windows用c语言实现的，所以，查看jdk的源代码，可以发现FileOutputStream的open方法的定义如下：

*private native void open(Stringname) throwsFileNotFoundException;*

​    如果我们要用java调用别人写的c语言函数，我们是无法直接调用的，我们需要按照java的要求写一个c语言的函数，又我们的这个c语言函数去调用别人的c语言函数。由于我们的c语言函数是按java的要求来写的，我们这个c语言函数就可以与java对接上，java那边的对接方式就是定义出与我们这个c函数相对应的方法，java中对应的方法不需要写具体的代码，但需要在前面声明native。

​    关于synchronized与abstract合用的问题，我觉得也不行，因为在我几年的学习和开发中，从来没见到过这种情况，并且我觉得synchronized应该是作用在一个具体的方法上才有意义。而且，方法上的synchronized同步所使用的同步锁对象是this，而抽象方法上无法确定this是什么。



### 23.几种返回方式

1. return
2. 异常抛出



### 24.访问修饰符

1.public：可以访问任何一个在classpath下的类，接口，异常等。往往用于对外的情况，也就是对象或类对外的一种接口的形式。

2.protected：用来保护子类，它的含义在于子类可以用它修饰的成员，其他的不可以，它相当于传递给子类的一种继承的东西。

==补充：==

1）父类的protected成员是包内可见的，并且对子类可见。

2）如果子类和父类在不同的包，那么子类可以访问从父类中继承的protected方法，而不能访问父类实例的protected方法。



3.default：有时也称为friendly, 它是针对本包访问而设计的，任何处于本包下的类，接口，异常等，都可以相互访问，即使是父类没有用protected修饰的成员也可以

4.private：访问权限仅限于类的内部，是一部封装的体现，例如：大多数成员变量都是修饰符为private，不希望被其他任何外部的类访问

(1)对于外部类而言，它也可以使用访问控制符修饰，但外部类只能有两种访问控制级别：public和默认。因为外部类没有处于任何类的内部，也就没有其所在类的内部、所在类的子类两个范围，因此 private 和 protected 访问控制符对外部类没有意义。

(2)内部类的上一级程序单元是外部类，它具有 4 个作用域：同一个类（ private ）、同一个包（ protected ）和任何位置（ public ）。

(3)因为局部成员的作用域是所在方法，其他程序单元永远不可能访问另一个方法中的局部变量，所以所有的局部成员都不能使用访问控制修饰符修饰。

|    修饰符     | 类内部 | 同一个包 | 不同包的子类 | 同一个工程 |
| :-----------: | :----: | :------: | :----------: | :--------: |
|    private    |  Yes   |          |              |            |
| default(缺省) |  Yes   |   Yes    |              |            |
|   protected   |  Yes   |   Yes    |     Yes      |            |
|    public     |  Yes   |   Yes    |     Yes      |    Yes     |



### 25.拷贝

浅拷⻉（引用拷贝）：对基本数据类型进⾏值传递，对引⽤数据类型进⾏引⽤传递般的拷⻉，此为浅拷⻉。
深拷⻉（对象拷贝）：对基本数据类型进⾏值传递，对引⽤数据类型，创建⼀个新的对象，并复制其内容，此为深拷⻉。



### 26.int 与 Integer的区别

int是一个基本数据类型，保存在Java虚拟机栈中，时间和性能优于Integer，并不是同一个对象，默认值为0，使用==来比较。

Integer是一个包装类型，是一个Java对象，默认值为None，使用equals()比较，拥有一个内部缓存，-128-127可以使用== 比较，在==POJO==中最好使用Integer，在序列化过程中可以告诉对方有没有这个值。



### 27.复制构造函数被调用的三种情况

1.定义一个对象时，以本类另一个对象作为初始值，发生复制构造；

2.如果函数的形参是类的对象，调用函数时，将使用实参对象初始化形参对象，发生复制构造；

3.如果函数的返回值是类的对象，函数执行完成返回主调函数时，将使用return语句中的对象初始化一个临时无名对象，传递给主调函数，此时发生复制构造



### 28.引用

1、强引用：一个对象赋给一个引用就是强引用，比如new一个对象，一个对象被赋值一个对象。
2、软引用：用SoftReference类实现，一般不会轻易回收，只有内存不够才会回收。
3、弱引用：用WeekReference类实现，一旦垃圾回收已启动，就会回收。
4、虚引用：不能单独存在，必须和引用队列联合使用。主要作用是跟踪对象被回收的状态。



### 29.try

try-catch
try-finally
try-catch-finally
但catch和finally语句不能同时省略！



### 30.Comparable和Comparator

- 定制排序：Java.util.Comparator, 将Comparator传递给sort方法，重写camparae方法
- 自然排序：Java.lang.Comparable，重写campareTo方法



## Java集合

### Java 容器都有哪些？
Java 容器分为 Collection 和 Map 两大类，其下又有很多子类，如下所示：

**Collection**
**List**
ArrayList
LinkedList
Vector
Stack

**Set**
HashSet
LinkedHashSet
TreeSet

**Map**
HashMap
LinkedHashMap
TreeMap
ConcurrentHashMap
Hashtable



### List / Set / Map

- List：可重复，有序，继承了List接口
- Set：不可重复，无序，继承了List接口
- Map：key-value，key是Set，value是collection



### Collection 和 Collections 有什么区别？
Collection 是一个集合接口，它提供了对集合对象进行基本操作的通用接口方法，所有集合都是它的子类，比如 List、Set 等。
Collections 是一个包装类，包含了很多静态方法，不能被实例化，就像一个工具类，比如提供的排序方法： Collections. sort(list)。



### List、Set、Map 之间的区别是什么？
List、Set、Map 的区别主要体现在两个方面：元素是否有序、是否允许元素重复。

三者之间的区别，如下表：

区别图





### ArrayList 和 LinkedList

同：都是线程不安全的

异：

- ArrayList，底层使用object[] ，实现了RandomAccess接口，可以支持高效的随机访问
- LinkedList，底层使用双向链表，适用于频繁的插入，删除操作



**补充：**

数据结构实现：ArrayList 是动态数组的数据结构实现，而 LinkedList 是双向链表的数据结构实现。
随机访问效率：ArrayList 比 LinkedList 在随机访问的时候效率要高，因为 LinkedList 是线性的数据存储方式，所以需要移动指针从前往后依次查找。
增加和删除效率：在非首尾的增加和删除操作，LinkedList 要比 ArrayList 效率要高，因为 ArrayList 增删操作要影响数组内的其他数据的下标。
综合来说，在需要频繁读取集合中的元素时，更推荐使用 ArrayList，而在插入和删除操作较多时，更推荐使用 LinkedList。



### Vector 和 ArrayList

- 同：

  - 都实现了List接口，有序，可重复的集合
  - 底层都使用`Object[], Capacity=10`, 

- 异：

  - Vector 线程安全，效率低。ArrayList 线程不安全，效率高
  - 即Vector增长原来的一倍，ArrayList增加原来的0.5倍。

  

**补充：**

线程安全：Vector 使用了 Synchronized 来实现线程同步，是线程安全的，而 ArrayList 是非线程安全的。

性能：ArrayList 在性能方面要优于 Vector。

扩容：ArrayList 和 Vector 都会根据实际的需要动态的调整容量，只不过在 Vector 扩容每次会增加 1 倍，而 ArrayList 只会增加 50%。



### Array 和 ArrayList 有何区别？

 Array 可以存储基本数据类型和对象，ArrayList 只能存储对象。

 Array 是指定固定大小的，而 ArrayList 大小是自动扩展的。

 Array 内置方法没有 ArrayList 多，比如 addAll、removeAll、iteration 等方法只有 ArrayList 有。

补充：对于基本类型的数据，集合可以通过自动装箱来减少编码量，但是如果是处理固定大小的基本数据类型，速度会相对较慢。



==自动装箱：==自动装箱是Java编译器在基本数据类型和对应的对象包装类型之间做的一个转化。比如：把int转化成Integer，double转化成Double，等等。反之就是自动拆箱。



### 在 Queue 中 poll()和 remove()有什么区别？
相同点：都是返回第一个元素，并在队列中删除返回的对象。

不同点：如果没有元素 poll()会返回 null，而 remove()会直接抛出 NoSuchElementException 异常。

代码示例：

```java
Queue queue = new LinkedList();
queue.offer(“string”); // add
System.out.println(queue.poll());
System.out.println(queue.remove());
System.out.println(queue.size());
```

 

### 如何实现数组和 List 之间的转换？

数组转 List：使用 Arrays. asList(array) 进行转换。

List 转数组：使用 List 自带的 toArray() 方法。

代码示例：

```java
// list to array
List list = new ArrayList();
list. add(“王磊”);
list. add(“的博客”);
list. toArray();
// array to list
String[] array = new String[]{“王磊”,“的博客”};
Arrays.asList(array);
```

 

### HashMap 和 HashTable

- 同：

  - 都实现了Map接口，无序，key:value，

- 异：

  - HashMap 线程不安全，Hashtable 线程安全

  - Hashtable是基于陈旧的Dictionary类的

  - HashMap允许将null作为一个entry的key或者value，而Hashtable不允许。

  - HashMap底层使用数组+链表+红黑树（当链表长度>8时，链表O(n)转化为红黑树O(log(N))，介绍搜索时间），七上八下。HashTable没有这样的机制

    

**补充：**

都实现了Map接口

存储：HashMap 运行 key 和 value 为 null，而 Hashtable 不允许。
线程安全：Hashtable 是线程安全的，而 HashMap 是非线程安全的。
推荐使用：可以看到，Hashtable 是保留类不建议使用，推荐在单线程环境下使用 HashMap 替代，如果需要多线程使用则用 ConcurrentHashMap 替代。



### HashMap 和 HashSet

HashSet 底层就是基于 HashMap 实现的 ，底层采用HashMap保存元素



### HashSet如何检查重复

当你把对象加⼊ HashSet 时， HashSet会先计算对象的 hashcode 值来判断对象加⼊的位置，同时也会与其他加⼊的对象的hashcode值作⽐较，如果没有相符的hashcode， HashSet会假设对象没有重复出现。但是如果发现有相同hashcode值的对象，这时会调⽤ equals（） ⽅法来检查hashcode相等的对象是否真的相同。如果两者相同， HashSet就不会让加⼊操作成功。  



### TreeSet

有序，不重复，使用红黑树



### TreeMap

红黑树



### ConcurrentHashMap 和 HashTable

底层数据结构：  

- JDK1.7的 ConcurrentHashMap 底层采⽤ 分段的数组+链表 实现， 
- JDK1.8  的ConcurrentHashMap 和1.8的HashTable相同，数组+链表+红黑树（当链表长度>8时，链表转化为红黑树）
- HashTable则采用数组+链表

实现线程安全的⽅式（重要）  ：

- 在JDK1.7的时候， ConcurrentHashMap（分段锁） 对整个桶
  数组进⾏了分割分段(Segment)，每⼀把锁只锁容器其中⼀部分数据，  
- JDK1.8 的时候已经摒弃了Segment的概念，⽽是直接⽤ Node 数组+链表+红⿊树的数据结构来实现，并发控制使⽤ synchronized 和
  CAS 来操作。  
- Hashtable(同⼀把锁) :使⽤ synchronized 来保证线程安全，效率⾮常低下。当⼀个线程访问同步⽅法时，其他线程也访问同步⽅法，可能会进⼊阻塞或轮询状态，如使⽤ put 添加元素，另⼀个线程不能使⽤ put 添加元素，也不能使⽤ get，竞争会越来越激烈效率越低。  



### 如何决定使用 HashMap 还是 TreeMap？
对于在 Map 中插入、删除、定位一个元素这类操作，HashMap 是最好的选择，因为相对而言 HashMap 的插入会更快，但如果你要对一个 key 集合进行有序的遍历，那 TreeMap 是更好的选择。



### 说一下 HashMap 的实现原理？
HashMap 基于 Hash 算法实现的，我们通过 put(key,value)存储，get(key)来获取。当传入 key 时，HashMap 会根据 key. hashCode() 计算出 hash 值，根据 hash 值将 value 保存在 bucket 里。当计算出的 hash 值相同时，我们称之为 hash 冲突，HashMap 的做法是用链表和红黑树存储相同 hash 值的 value。当 hash 冲突的个数比较少时，使用链表否则使用红黑树。



### 说一下 HashSet 的实现原理？
HashSet 是基于 HashMap 实现的，HashSet 底层使用 HashMap 来保存所有元素，因此 HashSet 的实现比较简单，相关 HashSet 的操作，基本上都是直接调用底层 HashMap 的相关方法来完成，HashSet 不允许重复的值。



**补充：**

![img](D:\消息保存\有道云笔记消息保存\zhangwj_524@163.com\af853e1d1ec94797bfd15d320097a6af\clipboard.png)

<img src="D:\消息保存\有道云笔记消息保存\zhangwj_524@163.com\8ed7d408ad0e4c0eaa37fcd8da6401d6\clipboard.png" alt="img" style="zoom:80%;" />



### 哪些集合类是线程安全的？

Vector、Hashtable、Stack 都是线程安全的，而像 HashMap 则是非线程安全的，不过在 JDK 1.5 之后随着 Java. util. concurrent 并发包的出现，它们也有了自己对应的线程安全类，比如HashMap 对应的线程安全类就是 ConcurrentHashMap。



### 迭代器 Iterator 是什么？

Iterator 接口提供遍历任何 Collection 的接口。我们可以从一个 Collection 中使用迭代器方法来获取迭代器实例。迭代器取代了 Java 集合框架中的 Enumeration，迭代器允许调用者在迭代过程中移除元素。



### Iterator 怎么使用？有什么特点？

Iterator 使用代码如下：

```java
List list = new ArrayList<>();
Iterator it = list. iterator();
while(it. hasNext()){
	String obj = it. next();
	System. out. println(obj);
}
```

Iterator 的特点是更加安全，因为它可以确保，在当前遍历的集合元素被更改的时候，就会抛出 ConcurrentModificationException 异常。



### Iterator 和 ListIterator 有什么区别？

Iterator 可以遍历 Set 和 List 集合，而 ListIterator 只能遍历 List。

Iterator 只能单向遍历，而 ListIterator 可以双向遍历（向前/后遍历）。

ListIterator 从 Iterator 接口继承，然后添加了一些额外的功能，比如添加一个元素、替换一个元素、获取前面或后面元素的索引位置。



### 怎么确保一个集合不能被修改？
可以使用 Collections. unmodifiableCollection(Collection c) 方法来创建一个只读集合，这样改变集合的任何操作都会抛出 Java. lang. UnsupportedOperationException 异常。

示例代码如下：

```java
List list = new ArrayList<>();
list.add(“x”);
Collection clist = Collections.unmodifiableCollection(list);
clist.add(“y”); // 运行时此行报错
System.out.println(list.size());
```



## 多线程

### 内存结构

```
线程1 CPU -- Cache -- |总线 | 
		  			 |	   |
线程2 CPU -- Cache -- |总线 |  ---- 主存（内存）
					 |	   |
线程3 CPU -- Cache -- |总线 | 
```

多线程当中，每个线程都拥有自己的Cache, 对变量进行读写操作时，都会先将该变量从内存中加载到Cache中，经过CPU处理后再将该变量放回Cache中，最后放入内存中。所以可能会导致缓存不一致问题。

为了解决缓存不一致性问题，通常来说有以下2种解决方法：

1. 通过在总线加LOCK锁的方式

   阻塞了其他CPU对其他部件访问（如内存），从而使得只能有一个CPU能使用这个变量的内存。

2. 通过缓存一致性协议（Intel 的MESI协议）

   当CPU写数据时，如果发现操作的变量是共享变量，即在其他CPU中也存在该变量的副本，会发出信号通知其他CPU将该变量的**缓存行置为无效状态**，因此当其他CPU需要读取这个变量时，发现自己缓存中缓存该变量的缓存行是无效的，那么它就会从内存重新读取。

   

### 守护进程

Daemon，在Linux中，守护进程程序的名称通常以字母“d”结尾，将后台程序变成一种服务，比如说，用命令行输入启动程序，如果不是守护进程的话，一旦命令行窗口关闭，程序就终止了；而如果启动守护进程，则退出命令行窗口之后，服务一直处于运行状态。

后台线程：指为其他线程提供服务的线程，也称为守护线程。JVM的垃圾回收线程就是一个后台线程。
前台线程：是指接受后台线程服务的线程，其实前台后台线程是联系在一起，就像傀儡和幕后操纵者一样的关系。傀儡是前台线程、幕后操纵者是后台线程。由前台线程创建的线程默认也是前台线程。可以通过isDaemon()和setDaemon()方法来判断和设置一个线程是否为后台线程。



### 程序、进程、线程

程序：静态的代码块

进程：运行的一个程序，作为资源分配的单位

线程：进程的细化，程序的一条执行路径。



**补充：**

**线程和进程的区别？**

 一个程序下至少有一个进程，一个进程下至少有一个线程，一个进程下也可以有多个线程来增加程序的执行速度。



**守护线程是什么？**

 守护线程是运行在后台的一种特殊进程。它独立于控制终端并且周期性地执行某种任务或等待处理某些发生的事件。在 Java 中垃圾回收线程就是特殊的守护线程。



### 线程的生命周期

- **新建**： 当一个Thread类或其子类的对象被声明并创建时，新生的线程对象处于新建状态
- **就绪**： 处于新建状态的线程被**start()**后，**将进入线程队列等待CPU时间片**，此时它已具备了运行的条件，只是**没分配到CPU资源**
- **运行**： 当就绪的线程被调度并获得CPU资源时,便进入运行状态， run()方法定义了线程的操作和功能
- **阻塞**： 在某种特殊情况下，被人为挂起或执行输入输出操作时，让出 CPU 并临时中止自己的执行，进入阻塞状态
- **死亡**： 线程完成了它的全部工作或线程被提前强制性地中止或出现异常导致结束  



**补充：**

线程的状态：

NEW 尚未启动
RUNNABLE 正在执行中
BLOCKED 阻塞的（被同步锁或者IO锁阻塞）
WAITING 永久等待状态
TIMED_WAITING 等待指定的时间重新被唤醒的状态
TERMINATED 执行完成



### 并发与并行

并发：单处理器，同时执行多个任务；两个或多个时间在同一时间间隔内发生

并行：多处理器，同时执行多个任务；两个或多个时间在同一时刻发生



**补充：**

并行：多个任务在同一个 CPU 核上，按细分的时间片轮流(交替)执行，从逻辑上来看那些任务是同时执行。

并发：多个处理器或多核处理器同时处理多个任务。

如下图：

并发和并行

并发 = 两个队列和一台咖啡机。

并行 = 两个队列和两台咖啡机。



### 上下文切换

概括来说就是：当前任务在执⾏完 CPU 时间⽚切换到另⼀个任务之前会先保存⾃⼰的状态，以便下次再切换回这个任务时，可以再加载这个任务的状态。 **任务从保存到再加载的过程就是⼀次上下⽂切换**。  



### 死锁

不同的线程分别占用对方需要的同步资源不放弃，都在等待对方放弃自己需要的同步资源，就形成了线程的死锁, 

**出现死锁后，不会出现异常，不会出现提示，只是所有的线程都处于阻塞状态，无法继续**。要满足下面4个条件

1. 互斥条件：一个资源每次只能被一个进程使用
2. 请求与保持条件：一个进程因请求资源而阻塞时，对已获得的资源保持不放
3. 不剥夺条件：进程已获得的资源，在未使用完之前，不能强行剥夺
4. 循环等待：A 等 B, B 等 C, C等A



**补充：**

**什么是死锁？**

当线程 A 持有独占锁a，并尝试去获取独占锁 b 的同时，线程 B 持有独占锁 b，并尝试获取独占锁 a 的情况下，就会发生 AB 两个线程由于互相持有对方需要的锁，而发生的阻塞现象，我们称为死锁。



**怎么防止死锁？**

尽量使用 tryLock(long timeout, TimeUnit unit)的方法(ReentrantLock、ReentrantReadWriteLock)，设置超时时间，超时可以退出防止死锁。

尽量使用 Java. util. concurrent 并发类代替自己手写锁。

尽量降低锁的使用粒度，尽量不要几个功能用同一把锁。

尽量减少同步的代码块。



### sleep()和wait()

 * 相同点：一旦执行方法，都可以使得当前的**线程进入阻塞**状态。

 * 不同点：

   * Wait 通常被⽤于线程间交互/通信， sleep 通常被⽤于暂停执⾏。  
   * 两个方法**声明的位置**不同：**Thread类中声明sleep()** , **Object类中声明wait()**
   * **调用的要求**不同：sleep()可以在**任何场景**下调用。 wait()必须使用在**同步代码块**或**同步方法**中
   * 关于是否释放同步监视器：如果两个方法都使用在同步代码块或同步方法中，**sleep()不会释放锁**，**wait()会释放锁**。

   

**补充：**

类的不同：sleep() 来自 Thread，wait() 来自 Object。

释放锁：sleep() 不释放锁；wait() 释放锁。

用法不同：sleep() 时间到会自动恢复；wait() 可以使用 notify()/notifyAll()直接唤醒。



### 创建多线程的方式

1. 创建一个继承于Thread类的子类，重写run方法，调用start()

2. 创建一个实现了Runnable接口的类，重写run方法。将此对象作为参数传入Thread类中，调用Thread类对象的start()方法

3. 创建一个实现了Callable接口的类，重写call()方法

   ```java
   		NumThread numThread = new NumThread(); //  NumThread implements Callable
           FutureTask futureTask = new FutureTask(numThread);  //`FutureTask` 同时实现了`Runnable, Future`接口
           new Thread(futureTask).start();
   		// futureTask对象可以获取返回值，Object sum = futureTask.get();
   ```

   - 可以有返回值, 方法可以抛出异常, 支持泛型的返回值 `V call() throws Exception;`

4. 线程池

<img src="D:\消息保存\有道云笔记消息保存\zhangwj_524@163.com\e285d273881a476ba415629a29c52351\clipboard.png" alt="img" style="zoom:80%;" />

![img](D:\消息保存\有道云笔记消息保存\zhangwj_524@163.com\5a718d95900147748ca4fd958de92478\clipboard.png)

![img](D:\消息保存\有道云笔记消息保存\zhangwj_524@163.com\8cb1bfccfbe04f2b90354b4500f8c711\clipboard.png)

![img](D:\消息保存\有道云笔记消息保存\zhangwj_524@163.com\a47e12eede9f4b9f8120049f2bdb9daa\clipboard.png)

![img](D:\消息保存\有道云笔记消息保存\zhangwj_524@163.com\6e213f91af334081a63618f95de5406b\clipboard.png)





**补充：**

继承 Thread 重新 run 方法；
实现 Runnable 接口；
实现 Callable 接口。



### 说一下 runnable 和 callable 有什么区别？

Runnable 没有返回值，callable 可以拿到有返回值，callable 可以看作是 runnable 的补充。



### Thread 和 Runnable的区别于联系

联系：`public class Thread implements Runnable`

相同点：两种方式都需要重写run(),将线程要执行的逻辑声明在run()中。

优先选择实现Runnable接口的方式

- 避免java单继承带来的局限性(Runnable接口,  class Thread)
- 更适合来处理多个线程有共享数据的情况
- 线程池只能放入实现Runable或Callable类线程，不能直接放入继承Thread的类



### Thread类中的常用方法

```java
/**
* 1. start():启动当前线程；调用当前线程的run()
 * 2. run(): 通常需要重写Thread类中的此方法，将创建的线程要执行的操作声明在此方法中
 * 3. currentThread():静态方法，返回当前执行代码的线程
 * 4. getName(): 获取当前线程的名字
 * 5. setName(): 设置当前线程的名字
 * 6. yield(): 释放当前cpu的执行权
 * 7. join(): 在线程a中调用线程b的join(),此时线程a就进入阻塞状态，直到线程b完全执行完以后，线程a才
 *           结束阻塞状态。
 * 8. stop():已过时。当执行此方法时，强制结束当前线程。
 * 9. sleep(long millitime):让当前线程“睡眠”指定的millitime毫秒。在指定的millitime毫秒时间内，当前
 *                          线程是阻塞状态。
 * 10. isAlive():判断当前线程是否存活
 
 * 线程的优先级：
 * 1.
 * MAX_PRIORITY：10
 * MIN _PRIORITY：1
 * NORM_PRIORITY：5  -->默认优先级
 * 2.如何获取和设置当前线程的优先级：
 *   getPriority():获取线程的优先级
 *   setPriority(int p):设置线程的优先级
 *
 * 说明：高优先级的线程要抢占低优先级线程cpu的执行权。但是只是从概率上讲，高优先级的线程高概率的情况下
 * 被执行。并不意味着只有当高优先级的线程执行完以后，低优先级的线程才执行。
 */
```



### 在 Java 程序中怎么保证多线程的运行安全？
方法一：使用安全类，比如 Java. util. concurrent 下的类。
方法二：使用自动锁 synchronized。
方法三：使用手动锁 Lock。
手动锁 Java 示例代码如下：

```java
Lock lock = new ReentrantLock();
lock. lock();

try {
	System. out. println(“获得锁”);
} catch (Exception e) {
 // TODO: handle exception
 } finally {
 	System. out. println(“释放锁”);
 	lock. unlock();
 }
```



### 代码级的锁有哪些

1. synchronized
2. ReentrantLock  `ReentrantLock implements Lock`
   - `this.sync = (ReentrantLock.Sync)(fair ? new ReentrantLock.FairSync() : new ReentrantLock.NonfairSync());` 
   - 线程 先到先服务。默认为false
   - 公平锁：新入线程不能直接获取锁，必须去排队（除非没有任何竞争发生）
   - 非公平锁：。新入的线程则可以先尝试获取锁，如果失败了再排队。
3. volatile

使用顺序：

- Lock ---> 同步代码块（已经进入了方法体，分配了相应资源） ----> 同步方法（在方法体之外）

```java
// 同步代码块
synchronized(同步监视器){
      //需要被同步的代码
}

//同步方法1
private static synchronized void show(){//同步监视器：类名.class
   
}
//同步方法2
private static synchronized void show(){//同步监视器：this
   
}

private ReentrantLock lock = new ReentrantLock();
lock.lock();
// 逻辑
lock.unlock();
```

- **同步监视器**，俗称：**锁**。任何一个类的对象，都可以充当锁

  - **多个线程必须要共用同一把锁**。

- 在实现**Runnable接口创建多线程**的方式中，我们可以考虑使用**this充当同步监视器**。

- 在**继承Thread类创建多线程**的方式中，慎用this充当同步监视器，考虑使用**当前类类名.class充当同步监视器**。

- 同步方法仍然涉及到同步监视器，只是**不需要我们显式的声明**。

  -  **非静态的同步方法**，同步监视器是：**this**
  -  **静态的同步方法**，同步监视器是：当前类本身,**类名.class**

  

### synchronized

synchronized 关键字加到 **static 静态⽅法**和 **synchronized(class)代码块**上都是是**给 Class类上锁**。 

synchronized 关键字加到**实例⽅法**上是给**对象实例上锁**。尽量不要使⽤
synchronized(String a) 因为JVM中，字符串常量池具有缓存功能！  



### volatile

- volatile关键字用在多线程同步中，可保证读取的可见性, JVM保证从主内存加载到线程工作内存的值是最新的.
- volatile能禁止进行指令重排序,但不能保证线程安全



**补充：**

**多线程中 synchronized 锁升级的原理是什么？**

synchronized 锁升级原理：在锁对象的对象头里面有一个 threadid 字段，在第一次访问的时候 threadid 为空，jvm 让其持有偏向锁，并将 threadid 设置为其线程 id，再次进入的时候会先判断 threadid 是否与其线程 id 一致，如果一致则可以直接使用此对象，如果不一致，则升级偏向锁为轻量级锁，通过自旋循环一定次数来获取锁，执行一定次数之后，如果还没有正常获取到要使用的对象，此时就会把锁从轻量级升级为重量级锁，此过程就构成了 synchronized 锁的升级。

锁的升级的目的：锁升级是为了减低了锁带来的性能消耗。在 Java 6 之后优化 synchronized 的实现方式，使用了偏向锁升级为轻量级锁再升级到重量级锁的方式，从而减低了锁带来的性能消耗。



### synchronized 和 volatile

- 关键字volatile是线程同步的轻量级实现，所以volatile性能肯定比synchronized要好，并且只能修改变量，而synchronized可以修饰方法，以及代码块。
  多线程访问volatile不会发生阻塞，而synchronized会出现阻塞
- volatile能保证数据的可见性，但不能保证原子性；而synchronized可以保证原子性，也可以间接保证可见性，因为它会将私有内存和公共内存中的数据做同步
- 关键字volatile解决变量在多线程之间的可见性；而synchronized解决的是多线程之间资源同步问题



**补充：**

**说一下 synchronized 底层实现原理？**  

synchronized 是由一对 monitorenter/monitorexit 指令实现的，monitor 对象是同步的基本实现单元。在 Java 6 之前，monitor 的实现完全是依靠操作系统内部的互斥锁，因为需要进行用户态到内核态的切换，所以同步操作是一个无差别的重量级操作，性能也很低。但在 Java 6 的时候，Java 虚拟机 对此进行了大刀阔斧地改进，提供了三种不同的 monitor 实现，也就是常说的三种不同的锁：偏向锁（Biased Locking）、轻量级锁和重量级锁，大大改进了其性能。



**synchronized 和 volatile 的区别是什么？**

volatile 是变量修饰符；synchronized 是修饰类、方法、代码段。
volatile 仅能实现变量的修改可见性，不能保证原子性；而 synchronized 则可以保证变量的修改可见性和原子性。
volatile 不会造成线程的阻塞；synchronized 可能会造成线程的阻塞。



### lock 与 synchronized

 * 相同：二者都可以解决线程安全问题

 * 不同：

    *   synchronized机制在执行完相应的同步代码以后，**自动释放同步监视器**
    *   Lock需要**手动启动同步**（lock()），同时结束同步也需要手动实现（unlock()）

   

**补充：**

**synchronized 和 Lock 有什么区别？**
synchronized 可以给类、方法、代码块加锁；而 lock 只能给代码块加锁。

synchronized 不需要手动获取锁和释放锁，使用简单，发生异常会自动释放锁，不会造成死锁；而 lock 需要自己加锁和释放锁，如果使用不当没有 unLock()去释放锁就会造成死锁。

通过 Lock 可以知道有没有成功获取锁，而 synchronized 却无法办到。



### synchronized 和 ReentrantLock 区别是什么？
synchronized 早期的实现比较低效，对比 ReentrantLock，大多数场景性能都相差较大，但是在 Java 6 中对 synchronized 进行了非常多的改进。

主要区别如下：

ReentrantLock 使用起来比较灵活，但是必须有释放锁的配合动作；
ReentrantLock 必须手动获取与释放锁，而 synchronized 不需要手动释放和开启锁；
ReentrantLock 只适用于代码块锁，而 synchronized 可用于修饰方法、代码块等。
volatile 标记的变量不会被编译器优化；synchronized 标记的变量可以被编译器优化。



### wait() / notify() / nitifyAll()

 * `wait()`:一旦执行此方法，当前线程就进入**阻塞**状态，并**释放同步监视器**。

 * `notify()`:一旦执行此方法，就会**唤醒被wait的一个线程**。如果有多个线程被wait，就唤醒优先级高的那个。

 * `notifyAll()`:一旦执行此方法，就会**唤醒所有被wait的线程**。

 * 说明：

   * `wait()，notify()，notifyAll()`三个方法必须在**同步代码块**或**同步方法**中使用， 定义在`java.lang.Object`类中。
   * `wait()，notify()，notifyAll()`三个方法的**调用者**必须是同步代码块或同步方法中的**同步监视器**。否则，会出现`IllegalMonitorStateException`异常

   

**补充：**

**notify()和 notifyAll()有什么区别？**
notifyAll()会唤醒所有的线程，notify()之后唤醒一个线程。notifyAll() 调用后，会将全部线程由等待池移到锁池，然后参与锁的竞争，竞争成功则继续执行，如果不成功则留在锁池等待锁被释放后再次参与竞争。而 notify()只会唤醒一个线程，具体唤醒哪一个线程由虚拟机控制。



### 并发编程的三个重要特性

1. 原⼦性 : ⼀个的操作或者多次操作，要么所有的操作全部都得到执⾏并且不会收到任何因素的⼲扰⽽中断，要么所有的操作都执⾏，要么都不执⾏。 synchronized 可以保证代码⽚段的原⼦性。
2. 可⻅性 ：当⼀个变量**对共享变量进⾏了修改**，那么**另外的线程都是⽴即可以看到修改后的最新值**。 volatile 关键字可以保证共享变量的可⻅性。
3. 有序性 ：代码在执⾏的过程中的先后顺序， Java 在编译器以及运⾏期间的优化，**代码的执⾏顺序未必就是编写代码时候的顺序**。 volatile 关键字可以禁⽌指令进⾏重排序优化。  



### 线程的 run() 和 start() 有什么区别？
start() 方法用于启动线程，run() 方法用于执行线程的运行时代码。run() 可以重复调用，而 start() 只能调用一次。



### 创建线程池有哪几种方式？
线程池创建有七种方式，最核心的是最后一种：

newSingleThreadExecutor()：它的特点在于工作线程数目被限制为 1，操作一个无界的工作队列，所以它保证了所有任务的都是被顺序执行，最多会有一个任务处于活动状态，并且不允许使用者改动线程池实例，因此可以避免其改变线程数目；

newCachedThreadPool()：它是一种用来处理大量短时间工作任务的线程池，具有几个鲜明特点：它会试图缓存线程并重用，当无缓存线程可用时，就会创建新的工作线程；如果线程闲置的时间超过 60 秒，则被终止并移出缓存；长时间闲置时，这种线程池，不会消耗什么资源。其内部使用 SynchronousQueue 作为工作队列；

newFixedThreadPool(int nThreads)：重用指定数目（nThreads）的线程，其背后使用的是无界的工作队列，任何时候最多有 nThreads 个工作线程是活动的。这意味着，如果任务数量超过了活动队列数目，将在工作队列中等待空闲线程出现；如果有工作线程退出，将会有新的工作线程被创建，以补足指定的数目 nThreads；

newSingleThreadScheduledExecutor()：创建单线程池，返回 ScheduledExecutorService，可以进行定时或周期性的工作调度；

newScheduledThreadPool(int corePoolSize)：和newSingleThreadScheduledExecutor()类似，创建的是个 ScheduledExecutorService，可以进行定时或周期性的工作调度，区别在于单一工作线程还是多个工作线程；

newWorkStealingPool(int parallelism)：这是一个经常被人忽略的线程池，Java 8 才加入这个创建方法，其内部会构建ForkJoinPool，利用Work-Stealing算法，并行地处理任务，不保证处理顺序；

ThreadPoolExecutor()：是最原始的线程池创建，上面1-3创建方式都是对ThreadPoolExecutor的封装。



### 线程池都有哪些状态？

RUNNING：这是最正常的状态，接受新的任务，处理等待队列中的任务。
SHUTDOWN：不接受新的任务提交，但是会继续处理等待队列中的任务。
STOP：不接受新的任务提交，不再处理等待队列中的任务，中断正在执行任务的线程。
TIDYING：所有的任务都销毁了，workCount 为 0，线程池的状态在转换为 TIDYING 状态时，会执行钩子方法 terminated()。
TERMINATED：terminated()方法结束后，线程池的状态就会变成这个。



### 线程池中 submit() 和 execute() 方法有什么区别？

execute()：只能执行 Runnable 类型的任务。
submit()：可以执行 Runnable 和 Callable 类型的任务。
Callable 类型的任务可以获取执行的返回值，而 Runnable 执行无返回值。



### ThreadLocal 是什么？有哪些使用场景？

ThreadLocal 为每个使用该变量的线程提供独立的变量副本，所以每一个线程都可以独立地改变自己的副本，而不会影响其它线程所对应的副本。

ThreadLocal 的经典使用场景是数据库连接和 session 管理等。



### 说一下 atomic 的原理？

atomic 主要利用 CAS (Compare And Wwap) 和 volatile 和 native 方法来保证原子操作，从而避免 synchronized 的高开销，执行效率大为提升。



## 异常

### throw 和 throws 的区别？

throw：是真实抛出一个异常。
throws：是声明可能会抛出一个异常。



### final、finally、finalize 有什么区别？

final：是修饰符，如果修饰类，此类不能被继承；如果修饰方法和变量，则表示此方法和此变量不能在被改变，只能使用。
finally：是 try{} catch{} finally{} 最后一部分，表示不论发生任何情况都会执行，finally 部分可以省略，但如果 finally 部分存在，则一定会执行 finally 里面的代码。
finalize： 是 Object 类的一个方法，在垃圾收集器执行的时候会调用被回收对象的此方法。



### try-catch-finally 中哪个部分可以省略？

try-catch-finally 其中 catch 和 finally 都可以被省略，但是不能同时省略，也就是说有 try 的时候，必须后面跟一个 catch 或者 finally。



### try-catch-finally 中，如果 catch 中 return 了，finally 还会执行吗？

finally 一定会执行，即使是 catch 中 return 了，catch 中的 return 会等 finally 中的代码执行完之后，才会执行。



### 常见的异常类有哪些？

NullPointerException 空指针异常
ClassNotFoundException 指定类不存在
NumberFormatException 字符串转换为数字异常
IndexOutOfBoundsException 数组下标越界异常
ClassCastException 数据类型转换异常
FileNotFoundException 文件未找到异常
NoSuchMethodException 方法不存在异常
IOException IO 异常
SocketException Socket 异常



## JVM

堆内存由存活和死亡的对象，空闲碎片组成，死亡的对象是应用不可访问尚且还没有被垃圾收集器回收掉的对象。

释放掉占据的内存空间是由gc完成，但是程序员无法明确强制其运行，该空间在不被引用的时候不一定会立即被释放，这取决于GC本身，无法由程序员通过代码控制

**运行时数据区：**

- **本地方法栈**：C语言实现

- **Java虚拟机栈**：由一个个栈帧组成，运行时的单位，i.e.: 程序如何执行。存放基本数据类型的局部变量，以及引用数据类型的对象的引用。一个线程对应一个Java虚拟机栈，Java虚拟机栈包含一组栈帧，一个栈帧对应一个方法
- 局部变量表--存储方法参数和定义在方法体内的局部变量，容量大小在编译期确定，基本单位为Slot, 如果当前帧是由非Static方法创建，this存放在slot的index为0处；
  
- 操作栈，
  - 动态连接--指向运行时常量池的方法引用，在Java源文件被**编译**到字节码文件时，**所有的变量和方法引用都作为符号引用**（SymbolicReference # 数字）保存在class文件的常量池中。  将符号引用转换为调用方法的直接引用。  
  - 方法返回地址：存储调用该方法的PC寄存器（调用该方法指令的下一条指令的地址）的值
  
- **堆（Eden, S0, S1, 新生代，老年代）**：存储的单位，存储大多数的对象。
  - 新生区，每个对象都拥有一个年龄计数器，每次YGC(当Eden区满时，触发YGC，S区满后不会触发)后，如果该对象依然存活，这年龄计数器+1，并且晋升到下一个区，Eden晋升到S0区，S0区满后，将S0中幸存的对象复制到S1区，S1区满后将幸存的对象复制到S0区，复制之后有交换，谁空谁是to  当年龄计数器增加到15时，将对象晋升（Promotion）为老年代（Tenured/old）  
    - Eden：大多数对象在Eden区被创建
    - S0(from区)
    - S1(to 区)
  - 养老区
  - GC about: 频繁在新生区收集，很少在养老区收集，几乎不在永久区/元空间收集  

- **程序计数器**：存储下一条指令的地址

- **方法区/元空间/永久代（常量池，方法元信息，类元信息）**：存储已被虚拟机加载的类型信息，常量(final)，静态变量(static)，即时编译后的代码缓存等  
  - jdk 7: 永久代，使用Java虚拟机内存，容易OOM
  - jdk8: 元空间，直接使用本地内存
  - **字符串常量池和运行时常量池从逻辑上属于方法区，但存储在堆中，**

- JIT：将字节码指令解释/编译为对应平台上的本地机器指令  



每个线程：独立包括Java虚拟机栈，本地方法栈，程序计数器

线程间共享：堆，堆外内存（方法区，代码缓存）



栈：不存在GC问题，但是肯定存在OOM

堆和方法区：GC和Error



- 部分收集：不是完整收集整个Java堆的垃圾收集
  - 新生代收集（Minor GC / Young GC）：只是新生代（Eden\ S0，S1）的垃圾收集
  - 老年代收集（Major GC / Old GC）:只是老年代的垃圾收集。
  - ps：很多时候Major GC会和Full GC混淆使用，需要具体分辨是老年代回收还是整堆回收
    混合收集（Mixed GC）：收集整个新生代以及部分老年代的垃圾收集
- 整堆收集（Full GC）：收集整个java堆和方法区的垃圾收集  



### 编译与解释

- 第一种是将源代码编译成字节码文件，然后**在运行时通过解释器将字节码文件转为机器码**执行
- 第二种是编译执行（**直接编译成机器码**）。使用JIT将方法编译成机器码后再执行  

HotSpot VM采用解释器与即时编译器并存的架构  

### Java类加载器

A.引导类加载器（bootstrap class loader）：它用来加载 Java 的核心库，是用原生代码来实现的
B.扩展类加载器（extensions class loader）：它用来加载 Java 的扩展库。
C.系统类加载器（system class loader）：它根据 Java 应用的类路径（CLASSPATH）来加载 Java 类
D.tomcat为每个App创建一个Loader，里面保存着此WebApp的ClassLoader。需要加载WebApp下的类时，就取出ClassLoader来使用



## Servlet

### Java Web为什么需要Tomcat

tomcat是servlet容器，客户端访问服务端使用的是http协议，而底层使用的是socket。tomcat充当服务端的socket，我们写的程序无需再做socket的工作，因为tomcat已经帮我们做了，我们只需要把自己的业务处理放在servlet的service方法即可

1. - 

### HttpServlet容器响应Web客户请求流程

HttpServlet容器响应Web客户请求流程如下：
1）Web客户向Servlet容器发出Http请求；
2）Servlet容器解析Web客户的Http请求；
3）Servlet容器创建一个HttpRequest对象，在这个对象中封装Http请求信息；
4）Servlet容器创建一个HttpResponse对象；
5）Servlet容器调用HttpServlet的service方法，这个方法中会根据request的Method来判断具体是执行doGet还是doPost，把HttpRequest和HttpResponse对象作为service方法的参数传给HttpServlet对象；
6）HttpServlet调用HttpRequest的有关方法，获取HTTP请求信息；
7）HttpServlet调用HttpResponse的有关方法，生成响应数据；
8）Servlet容器把HttpServlet的响应结果传给Web客户。
doGet() 或 doPost() 是创建HttpServlet时需要覆盖的方法.



## 补充

### 1.解释一下面向对象？

面向对象四大特征：抽象、封装、继承、多态

**封装：**是指将一类事物的属性和行为抽象成一个类，一般是使其属性私有化，行为公开化，在提高数据的隐秘性的同时，使代码模块化。

- 封装的好处是：将变化隔离，便于使用，提高代码复用性，提高安全性。

- 封装原则：把不需要对外提供的内容都隐藏起来；把属性都隐藏，提供公共方法对其访问。

**继承：**基于已有的类的定义为基础，构建新的类，已有的类称为父类，新构建的类称为子类，子类能调用父类的非private修饰的成员，同时还可以自己添加一些新的成员，扩充父类，甚至重写父类的方法，让其表现符合子类的特征。

- 继承的好处是：
  - 实现了代码的复用
  -  Java中所有的类都是通过直接或间接地继承java.lang.Object
  - 子类不能继承父类中访问权限为private的成员变量和方法
  - 子类可以重写父类的方法

**多态：**实现多态的两种方式：覆盖（Override）和重载（Overload）

- 覆盖，是指子类重新定义父类的虚函数的做法。它是覆盖了一个方法并且对其重写，以求达到不同的作用。
- 重载，是指允许存在多个同名函数，而这些函数的参数表不同（或参数表不同，或参数类型不同，或两者都不同）。它是指我们可以定义一些名称相同的方法，通过定义不同的输入参数来区分这些方法。
- 多态的**弊端**：当父类引用指向子类对象时，虽然提高了扩展性，但是只能访问父类中具备的方法，不可以访问子类中特有的方法。（访问的局限性）

**补充：**所谓多态就是指在程序中定义的引用变量，这个引用变量具体指向哪个类型，具体可以调用哪些方法，在程序编译时是无法确定的，需要在程序运行时才能确定。

简单来说就是一个引用变量到底会指向哪个类的实例对象，该引用变量发出的方法调用到底是哪个类中实现的方法，必须在程序运行期间才能决定。

在Java中有两种实现多态的方法：继承（多个子类对同一方法的重写）和接口（实现接口并覆盖接口中同一方法）



**抽象：**抽象是将一类对象的共同特征总结出来构造类的过程，包括数据抽象和行为抽象两个方面，抽象只关注对象的哪些属性和行为，并不关注这些行为的细节是什么。



### 2.JDK和JRE的区别？

 **JDK：**Java Development Kit 的简称，Java 开发工具包，提供了 Java 的开发环境和运行环境。
 **JRE：**Java Runtime Environment 的简称，Java 运行环境，为 Java 的运行提供了所需环境。

具体来说 JDK 其实包含了 JRE，同时还包含了编译 Java 源码的编译器 Javac，还包含了很多 Java 程序调试和分析的工具。简单来说：如果你需要运行 Java 程序，只需安装 JRE 就可以了，如果你需要编写 Java 程序，需要安装 JDK。



### 3.两个对象的hashCode()相同，则equals()也一定为true，对吗？

代码示例：

```java
String str1 = "通话";
String str2 = "重地";
System. out. println(String.format("str1：%d | str2：%d", str1.hashCode(),str2.hashCode()));

System.out.println(str1.equals(str2));
//执行的结果：
//str1：1179395 | str2：1179395
//false
```


 **代码解读：**很显然“通话”和“重地”的 hashCode() 相同，然而 equals() 则为 false，因为在散列表中，hashCode() 相等即两个键值对的哈希值相等，然而哈希值相等，并不一定能得出键值对相等。



### 4.Java 中的 Math. round(-1. 5) 等于多少？

等于 -1，Math. round 四舍五入大于 0. 5 向上取整的。



### 5.String 属于基础的数据类型吗？

String 不属于基础类型，基础类型有 8 种：byte、boolean、char、short、int、float、long、double，而 String 属于对象。



### 6.抽象类必须要有抽象方法吗？
 不需要，抽象类不一定非要有抽象方法。有抽象方法的类一定是抽象类。抽象类只可被继承，不能被实例化，当子类重写了父类中的所有抽象方法后，子类可以实例化。

示例代码：

```java
abstract class Cat {
 	public static void sayHi() {
 		System.out.println(“hi~”);
 	}
}
```

上面代码，抽象类并没有抽象方法但完全可以正常运行。



### 7.接口和抽象类有什么区别？

**默认方法实现：**抽象类可以有默认的方法实现；接口不能有默认的方法实现。

**实现：**抽象类的子类使用 extends 来继承；接口必须使用 implements 来实现接口。

**构造函数：**抽象类可以有构造函数；接口不能有。

**main 方法：** 

**实现数量：**类可以实现很多个接口；但是只能继承一个抽象类。

**访问修饰符：**接口中的方法默认使用 public 修饰；抽象类中的方法可以是任意访问修饰符。



### 8.Java 中 IO 流分为几种？

**按功能来分：**输入流（input）、输出流（output）。

**按类型来分：**字节流和字符流。

**字节流和字符流的区别是：**字节流按 8 位传输以字节为单位输入输出数据，字符流按 16 位传输以字符为单位输入输出数据。



### 9.BIO、NIO、AIO 有什么区别？
 **BIO：**Block IO 同步阻塞式 IO，就是我们平常使用的传统 IO，它的特点是模式简单使用方便，并发处理能力低。
 **NIO：**New IO 同步非阻塞 IO，是传统 IO 的升级，客户端和服务器端通过 Channel（通道）通讯，实现了多路复用。
 **AIO：**Asynchronous IO 是 NIO 的升级，也叫 NIO2，实现了异步非堵塞 IO ，异步 IO 的操作基于事件和回调机制。



### 10.Files的常用方法都有哪些？
 Files. exists()：检测文件路径是否存在。
 Files. createFile()：创建文件。
 Files. createDirectory()：创建文件夹。
 Files. delete()：删除一个文件或目录。
 Files. copy()：复制文件。
 Files. move()：移动文件。
 Files. size()：查看文件个数。
 Files. read()：读取文件。
 Files. write()：写入文件。



### 11.单例设计模式（Singleton）

软件开发最常用的设计模式之一

单：唯一

例：实例

即某个类在整个系统中只能有一个实例对象可被获取和使用的代码模式。

如：代表JVM运行环境的Runtime类

**要求：**

1.某个类只能有一个实例

私有化构造器 private  

​                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             2.类必须自行创建这个实例



3.必须自己主动提供给外部这个实例





**饿汉式：**开始就实例化

（1）直接实例化饿汉式（简洁直观）

（2）枚举式（最简洁）

（3）静态代码块饿汉式

```java
// 直接实例化饿汉式
class Singleton1 {
    //构造器私有化
    private Singleton1(){
      
    }
    
    //内部创建对象
    public static final Singleton1 INSTANCE = new Singleton1();

    //提供返回对象的方法
    public static Singleton getSingleton(){
        return INSTANCE;
    }
}

//枚举
public enum Singleton2{
    INSTANCE;
}

//静态代码块
class Singleton1 {
    
    //内部创建对象
    public static final Singleton1 INSTANCE;
    
    static{
        INSTANCE = new Singleton1();
    }
    
    //构造器私有化
    private Singleton1(){
      
    }
}

```

直接就创建，不存在线程安全问题。



**懒汉式：**需要的时候再实例化。

（1）线程不安全（单线程适用）

（2）线程安全（多线程适用）

（3）静态内部类形式（多线程适用）

```java
//线程不安全
class Singleton2 {
    private static Singleton2 instance;
    private Singleton2(){
        
    }
    
    public static Singleton getInstance(){
        //要加个判定语句
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }
}


//线程安全
class Singleton2 {
    private static Singleton2 instance;
    private Singleton2(){
        
    }
    
    synchronized(Singleton2.class){
        public static Singleton getInstance(){
        	if(instance == null){
            	instance = new Singleton();
        }
            
        return instance;
    }
}
    
//静态内部类
//在内部类被加载和初始化时，才创建INSTANCE实例对象
//静态内部类不会自动随着外部类的加载和初始化而初始化，它是要单独去加载和初始化的
//因为是在内部类加载和初始化时创建的，因此是线程安全的
class Singleton2 {
	
    
    private Singleton2(){
        
    }
	
    private static class Inner(){
        private static final INSTANCE = new Singleton2();
    }
    
    public static Singleton2 getInstance(){
        return Inner.INSTANCE;
    }

}    
```

总结：

如果是饿汉式，枚举类最简单

如果是懒汉式，静态内部类形式最简单



### 12.static关键字

《Java编程思想》 P86：

static方法就是没有this的方法。在static方法内部不能调用非静态方法，反过来是可以的。而且可以==在没有创建任何对象的前提下，仅仅通过类本身来调用static方法==。这实际上正是static方法的主要用途。

一句话来概括：方便在没有创建对象的情况下来进行调用。

被static关键字修饰的变量或者方法不需要依赖于对象来进行访问，只要类被成功加载，就可以通过类名去进行访问。

static可以用来修饰类的成员变量（属性）、类的成员方法，另外可以编写static代码块来优化程序性能。

- static修饰成员变量（属性）
- static修饰方法
- static修饰代码块

注：

- 独立于类
- 在类加载的时候执行，只执行一次
- 修饰的方法只在调用时执行



（1）static修饰方法

static修饰的方法一般称作静态方法，由于静态方法不依赖于任何对象就可以进行访问，因此对于静态方法来说，是没有this的。并且由于这个特性，在静态方法中不能访问非静态成员变量和非静态成员方法，因为非静态成员变量和非静态成员方法都必须依赖于具体的对象才能够被调用。

（注：非静态成员方法中可以访问静态成员方法和变量）

​	

```java
class MyObject{
    private static String str1 = "staticProperty";
    private String str2 = "property";
    
    public MyObject(){
        
    }
    
    public void print1(){
        System.out.println(str1);
        System.out.println(str2);
        print2();
    }
    
    public static void print2(){
        System.out.println(str1);
        //System.out.println(str2); 非法
        //print1(); 非法
    }
}
```

同理，为什么main方法必须是static的，因为程序在执行main方法的时候没有创建任何对象，因此只能通过类名来访问。



（2）static修饰成员变量

static修饰的变量也称作静态变量，静态变量和非静态变量的区别是：

静态变量被所有的对象所共享，在内存中只有一个副本，它当且仅当类在初次加载时会被初始化。

非静态变量是对象所拥有的，在创建对象的时候被初始化，存在多个副本，各个对象拥有的副本互不影响。



static成员变量的初始化顺序按照定义的顺序进行初始化。



（3）static修饰代码块

jdbc中通过静态代码快来加载资源。

static代码块可以置于类中的任何地方，类中可以由多个static代码块。在类初次被加载的时候，会按照static块的顺序来执行每个static块，每个都只会执行一次。



**static误区：**

1.static关键字会改变类中成员的访问权限吗？

不会，和C++中的static关键字不一样



2.能通过this访问静态成员变量吗？

虽然说静态方法没有this，但是可以通过this访问静态变量。

```java
public class Main{
    static int value = 33;
    
    public static void main(String[] args) throws Expection{
        new Main().printValue();
    }
    
    private void printValue(){
        int value = 3;
        System.out.println(this.value);
    }
}

//out 33
//this代表当前对象，通过new Main()来调用printValue，当前对象就是通过new Main()生成的对象，而static变量是被对象所享有的，故输出为33。
//在printValue()方法内部的value是局部变量，不可能与this关联
//记住：静态变量虽然独立于对象，但是不代表不可以通过对象去访问，所有的静态变量和静态方法都可以通过对象去访问（在访问权限足够的情况下）。
```



3.static能作用于局部变量吗？

在C/C++中static是可以作用域局部变量的，但是在Java中切记：static是不允许用来修饰局部变量，这是Java语法的规定。



```java
public  class  Test  extends  Base{
 
     static {
         System.out.println( "test static" );
     }
     
     public  Test(){
         System.out.println( "test constructor" );
     }
     
     public  static  void  main(String[] args) {
         new  Test();
     }
}
 
class  Base{
     
     static {
         System.out.println( "base static" );
     }
     
     public  Base(){
         System.out.println( "base constructor" );
     }
}

//输出
//base static
//test static
//base constructor
//test constructor
    
//执行过程
//在执行开始，先要寻找到main方法，因为main方法是程序的入口，但是在执行main方法之前，必须先加载Test类，而在加载Test类的时候发现Test类继承自Base类，因此会转去先加载Base类，在加载Base类的时候，发现有static块，便执行了static块。在Base类加载完成之后，便继续加载Test类，然后发现Test类中也有static块，便执行static块。在加载完所需的类之后，便开始执行main方法。在main方法中执行new Test()的时候会先调用父类的构造器，然后再调用自身的构造器。因此，便出现了上面的输出结果。
```



```java
public  class  Test {
     Person person =  new  Person( "Test" );
     static {
         System.out.println( "test static" );
     }
     
     public  Test() {
         System.out.println( "test constructor" );
     }
     
     public  static  void  main(String[] args) {
         new  MyClass();
     }
}
 
class  Person{
     static {
         System.out.println( "person static" );
     }
     public  Person(String str) {
         System.out.println( "person " +str);
     }
}
 
 
class  MyClass  extends  Test {
     Person person =  new  Person( "MyClass" );
     static {
         System.out.println( "myclass static" );
     }
     
     public  MyClass() {
         System.out.println( "myclass constructor" );
     }
}

//输出
//test static
//myclass static
//person static
//test constructor
//person MyClass
//myclass constructor

//执行过程
//首先加载Test类，因此会执行Test类中的static块。接着执行new MyClass()，而MyClass类还没有被加载，因此需要加载MyClass类。在加载MyClass类的时候，发现MyClass类继承自Test类，但是由于Test类已经被加载了，所以只需要加载MyClass类，那么就会执行MyClass类的中的static块。在加载完之后，就通过构造器来生成对象。而在生成对象的时候，必须先初始化父类的成员变量，因此会执行Test中的Person person = new Person()，而Person类还没有被加载过，因此会先加载Person类并执行Person类中的static块，接着执行父类的构造器，完成了父类的初始化，然后就来初始化自身了，因此会接着执行MyClass中的Person person = new Person()，最后执行MyClass的构造器。
```

 

```java
public  class  Test {
     
     static {
         System.out.println( "test static 1" );
     }
     public  static  void  main(String[] args) {
         
     }
     
     static {
         System.out.println( "test static 2" );
     }
}

//输出
//test static 1
//test static 2

//执行过程
// 1.加载类：通过jvm调用ClassLoader类中的loaderClass方法加载我们要执行的类
//2.执行static修饰的内容（从上往下执行）
//3.调用构造器
//4.成员变量初始化
//5.执行构造方法，对象创建完毕
```

注：

  1.static修饰的属性和方法，使用类名.xx的形式访问。

  2.使用的位置：那些不需要通过创建对象就可以访问方法的情况。



### 13.JDBC

​	Java数据库连接，（Java Database Connectivity，简称JDBC）是Java语言中用来规范客户端程序如何来访问数据库的应用程序接口，提供了诸如查询和更新数据库中数据的方法。JDBC也是Sun Microsystems的商标。我们通常说的JDBC是面向关系型数据库的。



常见面试题：







### 14.静态代码块 构造代码块 构造方法的执行顺序？

```java
public class ExA {  
    static {  
        System.out.println("父类--静态代码块");  
    }  
   
    public ExA() {  
        System.out.println("父类--构造函数");  
    }  
   
    {  
        System.out.println("父类--非静态代码块");  
    }  
   
    public static void main(String[] args) {  
        new ExB();  
    }  
}  
   
class ExB extends ExA {  
    static {  
        System.out.println("子类--静态代码块");  
    }  
    {  
        System.out.println("子类--非静态代码块");  
    }  
   
    public ExB() {  
        System.out.println("子类--构造函数");  
    }  
}  
 
//执行结果 

//1.父类--静态代码块 
//2.子类--静态代码块   
//3.父类--非静态代码块 
//4.父类--构造函数 
//5.子类--非静态代码块 
//6.子类--构造函数
```



### Java8新特性

1.

2.



### 类的加载机制

在编码完成后，Javac编译器会将 .java 文件转换为 .class 文件，在需要用到某个类的时候，Java虚拟机会加载将 .class文件，并创建相应的class对象，然后 将class文件加载到虚拟机的内存中。



### JMM内存模型



### JVM分区



### 数据结构

**1.数据结构有哪些？**

线性数据结构：数组，栈，队列，线性表（单链表，双链表，循环链表，双向循环链表）

树形数据结构：树，堆

图形数据结构：图



## 数据库

### 范式

- 1NF: 所有属性都是**不可分的基本数据项**
- 2NF: 每一个**非主属性完全函数依赖于码**。
  - 在1NF的基础上， 消除**部分依赖**
- 3NF: 每一个非主属性既**不部分依赖于码**也**不传递依赖于码**。
  - 在2NF的基础上， 消除**传递依赖**
- 反范式：**多表连接查询比较费时**，为了提高效率，允许数据冗余。



**补充：**

第一范式：所有字段都是不可分的基本字段

第二范式：

第三范式：

### 隔离级别

1. Read Uncommitted(读取未提交的内容) 可能脏读，不可重复读，幻读
2. Read Committed(读取提交内容) 可能不可重复读，幻读
3. Repeatable Read(可重读) 可能幻读
   - MySQL的默认事务隔离级别
4. Serializable(可串行化)

### MySQL简介

开源的关系型数据库，默认引擎是InnoDB,在5.7中，所有的存储引擎中只有InnoDB是事务性存储引擎

### InnoDB和MyISAM的区别

MyISAM是MySQL5.5之前的默认数据库，适用于读密集的情况下，5.5之后为InnoDB

- MyISAM：表级锁，强调性能，不支持事务，不支持崩溃修复和外键
- InnoDB：默认为行级锁，支持事务，崩溃修复和外键

### 事务的特性

事务：逻辑上的一组操作，要么都执行，要么都不执行。

- 原子性（Atomicity）：事务是最小的执行单位，不可分割
- 一致性（consistency）：事务执行前后，数据保持一致
- 隔离性（Isolation）：并发访问数据库时，一个用户的事务不被其他事务干扰
- 持久性（durability）：事务提交后，对数据库中的数据的改变是永久的

### Jion

关系表R（A，...），S(B，...)

- 内连接（innner jion）：可以使用像 = 或 <, >子类的比较符，还包括等值连接和自然连接
  - 等值连接：从R和S的笛卡尔积中选取A=B的原组，有重复列

  - 自然连接（nature jion）：在等值连接的基础上去除重复的属性列


- 外连接（outer jion）：把悬浮元组保存在结果中，其他属性填NULL。包括左外连接，右外连接和完整外部连接

  > 悬浮元组：在连接运算中舍弃的元组

  - left join 或 left outer join：只保留左边关系R中的悬浮元组，其他属性填NULL（即保留左表R中的所有元组，）
  - right jion 或 right outer jion
  - full jion 或 full outer jion

### 视图

虚表，修改视图会修改原始表，因为数据库中只存放视图的定义，不存放视图对应的数据。



### 内连接、外连接、左连接、右连接

外连接（out join）

分为外左连接(left outer join)和外右连接(right outer join)

**左连接**，取左边的表的全部，右边的表按条件，符合的显示，不符合则显示null

举例：select <select list> from A left join B on A.id=B.id

![img](https://images2017.cnblogs.com/blog/1074709/201712/1074709-20171229170434726-2010021622.png)

**右连接**：取右边的表的全部，左边的表按条件，符合的显示，不符合则显示null

举例：select <select list> from A right join B on A.id=B.id

![img](https://images2017.cnblogs.com/blog/1074709/201712/1074709-20171229171503867-2027149651.png)

内连接（inner join）

内连接：也称为等值连接，返回两张表都满足条件的部分

> 注释：inner join 就等于 join 

![SQL INNER JOIN](http://www.runoob.com/wp-content/uploads/2013/09/img_innerjoin.gif)



### 主键、外键





## 网络

### OSI七层模型

- 应用层：HTTP，FTP，DNS, DHCP，TELNET
- 表示层：加密解密，翻译，压缩
- 会话层：不同机器上的用户建立及管理回话
- 传输层：负责报文交付，可靠传输，不可靠传输，流量控制，文件分段,，TCP，UDP，
  - 数据段 = 源端口+目标端口+数据
- 网络层：负责IP寻址，控制子网的运行，如逻辑编址，分组传输，路由选择，ARP，IP，ICMP，IGMP
  - 数据包/报 = 目标IP地址+源IP地址+数据段
  - 路由器 Router
  - ARP：IP地址与物理地址的映射
- 数据链路层：物理寻址，将比特流转为逻辑传输线路，封装成帧，透明传输，差错检测CRC ，CSMA/CD
  - 数据帧 = 目标MAC地址+源MAC地址+数据包
  - 交换机 Switch
- 物理层：定义接口标准
  - Bit流
  - 集线器 Hub

### 三次握手

A：我想和你建立链接（SYN=1, seq=1000）

B：我收到了(ACK=1, ack=1001)，我也想和你建立链接（SYN=1, seq= 2000）

A: 我收到了（ACK=1， seq=2001）

目的：建立可靠的通信信道，确认自己与对方的发送与接收是正常的

### 四次挥手

A: 我想断开链接（FIN=1， seq = 25368）

B：我收到了（ACK=1, ack=25369）

B：我也想和你断开链接（FIN=1，seq=10568）

A：我收到了（ACK=1， ack=10569）

### 交换机和路由器

1. 路由器可以为局域网**自动分配IP和虚拟拨号**。交换机只是用来**分配网络数据**的。
2. **路由器在网络层，根据IP地址寻址**。路由器可以处理“TCP/IP”协议，交换机不行。**交换机在数据链路层，根据“MAC”地址寻址**。
   - 待定：**路由器可以把一个IP分给多个主机使用，对外IP相同**。**交换机可以把很多主机连接起来，对外的IP不同**。
3. **路由器可以提供防火墙**，交换机不能提供这个功能。**交换机是做扩大局域网接入点**的，可以让局域网连进更多的电脑。路**由器是用来做网间连接**，也就是用来连接不同网络的。

### TCP和UDP

同：都在传输层

异：

- TCP：面向连接，可靠交付，一对一，面向字节流，总体开销大
- UDP：无连接，最大努力交付，可以一对多，面向报文，不会出现拥塞控制，首部开销小，只有8个字节，而TCP有20个字节
  - DNS，SNMP(简单网络管理协议), TFTP(Trival FIle Transfer Protocal)

### TCP如何保证可靠传输

1. 数据包校验
2. 对失序数据包重排序
3. 丢弃重复数据
4. 应答机制
5. 超时重发
6. 流量控制

### 停止等待协议

为了可靠传输，每发完一个分组就停止发送，等待对方确认。

### 上网过程

用户在浏览器中键入URL，数据包到DNS，DNS将URL解析成IP地址返回给用户，浏览器将再通过IP地址访问服务器。建立TCP连接，发送HTTP请求，服务器接收到请求后，将网页分割成一个个数据帧。数据帧存储到网卡缓存，按顺序发送给用户。数据帧不能删除，当用户收到数据包后确认后无误后向服务器确认后，才可以删除

### forward 和 redirect

1. 从地址栏显示来说
   - forward是服务器请求资源,服务器直接访问目标地址的URL,把那个URL的响应内容读取过来,然后把这些内容再发给浏览器.浏览器根本不知道服务器发送的内容从哪里来的,所以它的**地址栏还是原来的地址.**
   - redirect是服务端根据逻辑, 发送一个状态码, 告诉浏览器重新去请求那个地址. 所以**地址栏显示的是新的URL**.

2. 从数据共享来说
   - forward: 转发页面和转发到的页面可以共享request里面的数据.
   - redirect: 不能共享数据.

3. 从运用地方来说
   - forward:一般用于**用户登陆**的时候, 根据角色转发到相应的模块.
   - redirect: 一般用于**用户注销登陆**时返回主页面和跳转到其它的网站等.

4. 从效率来说
   - forward: 高.
   - redirect: 低.

### SSL

SSL 安全套接字，https中的s

- 位于传输层之上，应用层之下
- 在发送方，SSL接受应用层的数据，对数据进行加密，然后把加了密的数据送往TCP套接字
- 在接受方，SSL从TCP套接字读取数据，解密后把数据交给应用层

SSL的功能

1. SSL服务器鉴别：允许用户证实服务器的身份。具有SSL功能的浏览器维持一个表，上面有一些可信赖的认证中心CA（Certificate Authority）和它们的公钥
2. 加密的SSL会话：客户和服务器交互的所有数据都在发送方加密，在接收方解密。
3. SSL客户鉴别：允许服务器证实客户的身份

### HTTP状态码

- 1XX 信息
  - 100 Continue:
- 2XX Success
  - 200 OK
- 3XX 重定向
  - 301 Moved Permanently：永久重定向
  - 302 Foud：临时重定向
- 4XX 客户端错误
  - 400 Bad Request
  - 401 Unauthorized
- 5XX 服务器错误



### HTTP和HTTPS

- 端口不同：80，443
- HTTP运行在TCP之上，明文传输，HTTPS在运行在SSL/TLS之上，SSL/TLS位于传输层之上，应用层之下，加密传输，需要到CA申请证书，要钱

### Cookie和Session

因为HTTP是一种无状态协议，为了跟踪用户状态状态，服务器向浏览器分配一个唯一ID，以Cookie的形式发送到浏览器，浏览器访问服务器时，会带上Cookie用以识别身份

异：

- Cookie一般用来保存用户信息及喜好，保存在客户端
- Session 通过服务端记录用户的状态，如购物车，保存在服务器端，更加安全

### GET和POST

同：都属于HTTP请求
异：

- 本质：GET只是一次请求，而POST先发请求头再发请求体，实际上是两次请求
- REST服务：GET是幂等的，即读取同一个资源总得到相同的数据。而POST会对服务器进行改变
- 请求参数：GET数据会附在URL上，即HTTP报文的请求头中，用？分割URL和传输数据，参数之间使用&相连。英文/数字原样发送，其他字符用BASE64加密；而POST会把提交的数据放在HTTP报文的请求体中。
- 安全性：POST更安全
- 请求大小：GET请求的长度受限于浏览器或服务器，而POST没有限制

### 数字签名

对文件使用单向散列函数获得摘要，摘要确保文件的完整性，再使用发送方的私钥对摘要形成数字签名

防止发送方不承认这是自己的私钥或被他人盗用私钥，从而需要第三方（证书颁发机构 CA）来发放证书（私钥和公钥（CA签名）

> 散列函数 单向函数
>
> 摘要保证了明文的完整性
>
> 私钥相当于自己签名，体现了抗抵赖性

### RESTful

看URL就知道要干什么，

method就知道干什么

看状态码就知道结果怎么样



### JDBC是什么？连接过程

