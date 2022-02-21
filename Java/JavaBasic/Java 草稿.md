# Java 草稿

# **Java**

## **1 简介**

### **1.1 Java语言的特点**

特点一： 面向对象
两个基本概念：类、对象
三大特性：封装、继承、多态
特点二： 健壮性
吸收了C/C++语言的优点，但去掉了其影响程序健壮性的部分（如指针、内存的申请与
释放等），提供了一个相对安全的内存管理和访问机制
特点三： 跨平台性
跨平台性：通过Java语言编写的应用程序在不同的系统平台上都可以运行。 “Write
once , Run Anywhere”
原理：只要在需要运行 java 应用程序的操作系统上，先安装一个Java虚拟机 (JVM Java
Virtual Machine) 即可。由JVM来负责Java程序在该系统中的运行

JDK = JRE + 开发工具集（例如Javac编译工具等）

JRE = JVM + Java SE标准类库

一个源文件中最多只能有一个public类。其它类的个数不限，如果源文件包含一个public类，则文件名必须按该类名命名

命名规范

包名：多单词组成时所有字母都小写： xxxyyyzzz

类名、接口名：多单词组成时，所有单词的首字母大写： XxxYyyZzz

变量名、方法名：多单词组成时，第一个单词首字母小写，第二个单词开始每个单词首字母大写： xxxYyyZzz

常量名：所有字母都大写。多单词时每个单词用下划线连接： XXX_YYY_ZZZ

浮点型常量有两种表示形式：
 十进制数形式：如： 5.12 512.0f .512 (必须有小数点）
 科学计数法形式:如： 5.12e2 512E2 100E-2

当把任何基本数据类型的值和字符串(String)进行连接运算时(+)， 基本数据类型的值将自动转化为字符串(String)类型

```
        System.out.println("str1" + false); // str1false
        System.out.println(3.14f+""); // 3.14
        System.out.println(3+4+"hello"); // 7hello
        System.out.println("hello"+3+4); // hello34
        System.out.println("a"+1+"hello"); //a1hello
        System.out.println("hello"+"a"+1); //helloa1
```

```
        short s = 5;
//        s = s - 2;// wrong，2 is int
        s = 5 - (short)(2);
        s-=2; //Convert int to short

        char c = 'a'; // a = 97
        int i = 5;
        float d = .314F;
        double result = c+i+d; // 向上转型
```

对于整数，有四种表示方式：
二进制(binary)： 0,1 ，满2进1.以0b或0B开头。
十进制(decimal)： 0-9 ，满10进1。
八进制(octal)： 0-7 ，满8进1. 以数字0开头表示。
十六进制(hex)： 0-9及A-F，满16进1. 以0x或0X开头表示。此处的A-F不区分大小写。
如： 0x21AF +1= 0X21B0

Java整数常量默认是int类型，当用二进制定义整数时，其第32位是符号位；
当是long类型时，二进制默认占64位，第64位是符号位

二进制的整数有如下三种形式：
原码：直接将一个数值换成二进制数。最高位是符号位
负数的反码：是对原码按位取反，只是最高位（符号位）确定为1。
负数的补码：其反码加1

计算机以二进制补码的形式保存所有的整数。
正数的原码、反码、补码都相同
负数的补码是其反码+1

为什么要使用原码、反码、补码表示形式呢？
计算机辨别“符号位”显然会让计算机的基础电路设计变得十分复杂! 于是
人们想出了将符号位也参与运算的方法. 我们知道, 根据运算法则减去一个正
数等于加上一个负数, 即: 1-1 = 1 + (-1) = 0 , 所以机器可以只有加法而没有
减法, 这样计算机运算的设计就更简单了

位运算是直接对整数的二进制进行的运算

```
        System.out.println(3 << 1); // 3*2 = 6
        System.out.println(3 >> 1);  //floor(3/2)=1

        System.out.println(3 << 2); // 3*2^2 = 12
        System.out.println(3 >> 2);  //floor(3/2^2)=0
```

数组(Array)， 是多个相同类型数据按一定顺序排列的集合， 并使用一个名字命名， 并通过编号的方式对这些数据进行统一管理

```
动态初始化
int[] arr = new int[3];
System.out.println(arr[0]); // 默认初始化为0
arr[0] = 3;
System.out.println(arr[0]);
arr[1] = 9;
arr[2] = 8;

String names[];
names = new String[3];
names[0] = “钱学森”;
names[1] = “邓稼先”;
names[2] = “袁隆平”;

静态初始化
    int arr[] = new int[]{ 3, 9, 8};
    int[] arr = {3,9,8};

    String names[] = {
    “李四光”,“茅以升” ,“华罗庚”
    }
```

布尔数组默认为false

数组没有length()这个方法，有length的属性。String有length()这个方法

 类是对一类事物的描述，是抽象的、概念上的定义
 对象是实际存在的该类事物的每个个体，因而也称为实例(instance)。

方法的重载 ：同名不同参（参数列表，参数个数或参数类型，与返回值类型无关【System.out.ptintln()的返回值都会void】）

[Untitled](Java%20%E8%8D%89%E7%A8%BF%20db4d272d11f0438f8021f7a643820e83/Untitled%20Database%2008c7521dda464ceb9e86fc94aa2fbeff.csv)

JavaBean是一种Java语言写成的可重用组件

所谓javaBean，是指符合如下标准的Java类

类是公共的
有一个无参的公共的构造器
有属性，且有对应的get、 set方法

JavaBean示例

```
public class JavaBean {
    private String name; // 属性一般定义为private
    private int age;
    public JavaBean() {
    }
    public int getAge() {
        return age;
    }
    public void setAge(int a) {
        age = a;
    }
    public String getName() {
        return name;
    }
    public void setName(String n) {
        name = n;
    }
}
```

this

 它在方法内部使用，即这个方法所属对象的引用；
 它在构造器内部使用，表示该构造器正在初始化的对象

```
class Person{ // 定义Person类
    private String name ;
    private int age ;
    public Person(){ // 无参构造器
        System.out.println("新对象实例化") ;
    }
    public Person(String name){
        this(); // 调用本类中的无参构造器
        this.name = name ;
    }
    public Person(String name,int age){
        this(name) ; // 调用有一个参数的构造器
        this.age = age;
    }
    public String getInfo(){
        return "姓名： " + name + "，年龄： " + age ;
    }
}
```

MVC设计模式

MVC是常用的设计模式之一，将整个程序分为三个层次： 视图模型层，控制器层，与数据模型层。 这种将程序输入输出、数据处理，以及数据的展示分离开来的设计模式使程序结构变的灵活而且清晰，同时也描述了程序各个对象间的通信方式，降低了程序的耦合性

模型层 model 主要处理数据
>数据对象封装 model.bean/domain
>数据库操作类 model.dao
>数据库 model.db

控制层 controller 处理业务逻辑
应用界面相关 controller.activity
存放fragment  controller.fragment
显示列表的适配器  controller.adapter
服务相关的  controller.service
抽取的基类  controller.base

视图层 view 显示数据
>相关工具类 view.utils
>自定义view view.ui

继承：子类继承父类的所有属性和方法，并且可以重写父类的方法或增加自己的方法

重写：同名同参

子类重写的方法的返回值类型不能大于父类被重写的方法的返回值类型

子类重写的方法使用的访问权限不能小于父类被重写的方法的访问权限
子类不能重写父类中声明为private权限的方法

子类与父类中同名同参数的方法必须同时声明为非static的(即为重写)，或者同时声明为
static的（不是重写） 。因为static方法是属于类的，子类无法覆盖父类的方法

this代表本类对象的引用， super代表父类的内存
空间的标识

```
package inherit;

import java.util.Date;

public class Person {
        private String name;
        private int age;
        private Date birthDate;

        public Person(String name, int age, Date d) {
                    this.name = name;
                    this.age = age;
                    this.birthDate = d;
                }
        public Person(String name, int age) {
                    this(name, age, null);
                }
        public Person(String name, Date d) {
                    this(name, 30, d);
                }
        public Person(String name) {
                    this(name, 30);
                }
}

```

```
package inherit;

public class Student extends Person{
    private String school;
    public Student(String name, int age, String s) {
        super(name, age);
        school = s;
    }
    public Student(String name, String s) {
        super(name);
        school = s;
    }

    public Student(String s) {
        school = s;
        // 编译出错: no super(),系统将调用父类无参数的构造器。
        // 当类中没有显式调用构造器时，会使用默认的无参构造器，否则使用显式的构造器
        // 由于父类创建了带参构造器，又没有声明无参构造器。子类调用父类无参构造器，error
    }
}

```

[Untitled](Java%20%E8%8D%89%E7%A8%BF%20db4d272d11f0438f8021f7a643820e83/Untitled%20Database%204f22a3910d1b407cb53bb1e01423108d.csv)

对象的多态性：父类的引用指向子类的对象

Java引用变量有两个类型： 编译时类型和运行时类型。

编译时， 看左边；运行时， 看右边

多态情况下，

“看左边” ： 看的是父类的引用（父类中不具备子类特有的方法）
“看右边” ： 看的是子类的对象（实际运行的是子类重写父类的方法）

对象的多态 —在Java中,子类的对象可以替代父类的对象使用
一个变量只能有一种确定的数据类型
一个引用类型变量可能指向(引用)多种不同类型的对象

子类可看做是特殊的父类， 所以父类类型的引用可以指向子类的对象：向上转型(upcasting)

一个引用类型变量如果声明为父类的类型，但实际引用的是子类
对象，那么该变量就不能再访问子类中添加的属性和方法

对Java对象的强制类型转换称为造型
从子类到父类的类型转换可以自动进行
从父类到子类的类型转换必须通过造型(强制类型转换)实现
无继承关系的引用类型间的转换是非法的
在造型前可以使用instanceof操作符测试一个对象的类型

子类继承父类
若子类重写了父类方法，就意味着子类里定义的方法彻底覆盖了父类里的
同名方法，系统将不可能把父类里的方法转移到子类中。
对于实例变量则不存在这样的现象，即使子类里定义了与父类完全相同的
实例变量，这个实例变量依然不可能覆盖父类中定义的实例变量

```
package dengyu;

public class DengYu {
    static class Person{

    }
    public static void main(String[] args) {
        System.out.println(3 == 4); //false
        Person person1 = new Person();
        Person person2 = new Person();
        System.out.println(person1 == person2); //false
        System.out.println(person1.equals(person2)); //false

    }
}

```

1 == 既可以比较基本类型也可以比较引用类型。对于基本类型就是比较值，对于引用类型
就是比较内存地址
2 equals的话，它是属于java.lang.Object类里面的方法，如果该方法没有被重写过默认也
是==;我们可以看到String等类的equals方法是被重写过的，而且String类在日常开发中
用的比较多，久而久之，形成了equals是比较值的错误观点。
3 具体要看自定义类里有没有重写Object的equals方法来判断。
4 通常情况下，重写equals方法，会比较类中的相应属性是否都相等。

```
int it = 65;
float fl = 65.0f;
System.out.println(“65和65.0f是否相等？ ” + (it == fl)); //true int 向上转型为float
char ch1 = 'A'; char ch2 = 12;
System.out.println("65和'A'是否相等？ " + (it == ch1));//true
System.out.println(“12和ch2是否相等？ " + (12 == ch2));//true
String str1 = new String("hello");
String str2 = new String("hello");
System.out.println("str1和str2是否相等？ "+ (str1 == str2));//false
System.out.println("str1是否equals str2？ "+(str1.equals(str2)));//true
```

char，String输出对象时，自动调用toString方法

```
        char[] arr = new char[] { 'a', 'b', 'c' };
        System.out.println(arr);//abc
        int[] arr1 = new int[] { 1, 2, 3 };
        System.out.println(arr1);//[I@4554617c
        double[] arr2 = new double[] { 1.1, 2.2, 3.3 };
        System.out.println(arr2);//[D@74a14482
```

static

被修饰后的成员具备以下特点：
随着类的加载而加载  clinit
优先于对象存在  
修饰的成员，被所有对象所共享 (共享一块内存)
访问权限允许时，可不创建对象，直接被类调用

```
package statictest;

public class Person {
        private int id;
        public static int total = 0;

        public Person() {
                total++;
                id = total;
        }

        public static void main(String[] args) {
                Person.total = 100; // 不用创建对象就可以访问静态成员
                //访问方式：类名.类属性， 类名.类方法
                System.out.println(Person.total); // 100

                Person Tom = new Person();
                System.out.println(total); // 101

                total=100;
                System.out.println(total);  // 100

        }
}
```

在static方法内部只能访问类的static修饰的属性或方法， 不能访问类的非static的结构。

因为不需要实例就可以访问static方法，因此static方法内部不能有this。 (也
不能有super ? YES!)
 static修饰的方法不能被重写

理解main方法的语法

 由于Java虚拟机需要调用类的main()方法，所以该方法的访问权限必须是
public， 又因为Java虚拟机在执行main()方法时不必创建对象，所以该方法必须
是static的，该方法接收一个String类型的数组参数，该数组中保存执行Java命令
时传递给所运行的类的参数。
 又因为main() 方法是静态的，我们不能直接访问该类中的非静态成员，必须创
建该类的一个实例对象后，才能通过这个对象去访问类中的非静态成员

 静态代码块：用static 修饰的代码块
\1. 可以有输出语句。
\2. 可以对类的属性、类的声明进行初始化操作。
\3. 不可以对非静态的属性初始化。即：不可以调用非静态的属性和方法。
\4. 若有多个静态的代码块，那么按照从上到下的顺序依次执行。
\5. 静态代码块的执行要先于非静态代码块。
\6. 静态代码块随着类的加载而加载，且只执行一次。

 非静态代码块：没有static修饰的代码块
\1. 可以有输出语句。
\2. 可以对类的属性、 类的声明进行初始化操作。
\3. 除了调用非静态的结构外， 还可以调用静态的变量或方法。
\4. 若有多个非静态的代码块， 那么按照从上到下的顺序依次执行。
\5. 每次创建对象的时候， 都会执行一次。 且先于构造器执行。

```
package statictest;

public class Person {
        public static int total = 0;
        static {
                total = 100;
                System.out.println("in static block");
        }

        public static void main(String[] args) {
                System.out.println("total = " + Person.total);
                System.out.println("total = " + Person.total);
                /*
                in static block
                total = 100
                total = 100
                 */
        }
}

```

```
package wrapper;

import org.junit.Test;

public class WrapperTest {
    @Test
    public void  test1(){
        //String类型 --->基本数据类型、包装类：调用包装类的parseXxx(String s)
        String str1 = "123";

        //错误的情况：
//        int num1 = (int)str1;
//        Integer in1 = (Integer)str1;

        int num2 = Integer.parseInt(str1);
        System.out.println(num2+1); // 124

        String str2 = "true";
        boolean b1 = Boolean.parseBoolean(str2);
        System.out.println(b1); // true

        String str3 = "true1";
        boolean b2 = Boolean.parseBoolean(str3);
        System.out.println(b2); // false
    }
    @Test
    public void test2(){
        //基本数据类型、包装类--->String类型：调用String重载的valueOf(Xxx xxx)
        int num1 = 10;
        //方式1：连接运算
        String str1 = num1 + "";
        System.out.println(str1);

        //方式2：调用String的valueOf(Xxx xxx)
        float f1 = 12.3f;
        String str2 = String.valueOf(f1);
        System.out.println(str2); //"12.3"

        Double d1 = new Double(12.4);
        String str3 = String.valueOf(d1);
        System.out.println(str3);//"12.4"
    }

//    JDK 5.0 新特性：自动装箱 与自动拆箱
    @Test
    public void test3(){
        //自动装箱：基本数据类型 --->包装类
        int num2 = 10;
        Integer in1 = num2;//自动装箱

        boolean b1 = true;
        Boolean b2 = b1;//自动装箱

        //自动拆箱：包装类--->基本数据类型
        System.out.println(in1.toString());

        int num3 = in1;//自动拆箱
    }

    //包装类--->基本数据类型:调用包装类Xxx的xxxValue()
    @Test
    public void test4(){
        Integer in1 = new Integer(12);

        int i1 = in1.intValue();
        System.out.println(i1 + 1);

        Float f1 = new Float(12.3);
        float f2 = f1.floatValue();
        System.out.println(f2 + 1);
    }

    //基本数据类型 --->包装类：调用包装类的构造器
    @Test
    public void test5(){
        int num1 = 10;
//    System.out.println(num1.toString());
        Integer in1 = new Integer(num1);
        System.out.println(in1.toString());

        Integer in2 = new Integer("123");
        System.out.println(in2.toString());

        //报异常
//    Integer in3 = new Integer("123abc");
//    System.out.println(in3.toString());

        Float f1 = new Float(12.3f);
        Float f2 = new Float("12.3");
        System.out.println(f1);
        System.out.println(f2);

        Boolean b1 = new Boolean(true);
        Boolean b2 = new Boolean("TrUe");
        System.out.println(b2);
        Boolean b3 = new Boolean("true123");
        System.out.println(b3);//false

    }

}
```

final

在Java中声明类、 变量和方法时， 可使用关键字final来修饰,表示“最终的” 。
final标记的类不能被继承。 提高安全性， 提高程序的可读性。
String类、 System类、 StringBuffer类
final标记的方法不能被子类重写。
比如： Object类中的getClass()。
final标记的变量(成员变量或局部变量)即称为常量。 名称大写， 且只
能被赋值一次。
final标记的成员变量必须在声明时或在每个构造器中或代码块中显式赋
值， 然后才能使用。
final double MY_PI = 3.14;

抽象类。  父类的抽象,没有具体的实例

 用abstract关键字来修饰一个类， 这个类叫做抽象类。
 用abstract来修饰一个方法， 该方法叫做抽象方法。
抽象方法：只有方法的声明，没有方法的实现。以分号结束：
比如： public abstract void talk();
 含有抽象方法的类必须被声明为抽象类。
 抽象类不能被实例化。抽象类是用来被继承的，抽象类的子类必须重
写父类的抽象方法，并提供方法体。若没有重写全部的抽象方法，仍为抽象类。
 不能用abstract修饰变量、代码块、构造器；
 不能用abstract修饰私有方法、静态方法、 final的方法、 final的类。

 定义Java类的语法格式： 先写extends，后写implements
 class SubClass extends SuperClass implements InterfaceA{ }
 一个类可以实现多个接口， 接口也可以继承其它接口。
 实现接口的类中必须提供接口中所有方法的具体实现内容，方可实
例化。否则，仍为抽象类。
 接口的主要用途就是被实现类实现。 （面向接口编程）
 与继承关系类似，接口与实现类之间存在多态性
 接口和类是并列关系， 或者可以理解为一种特殊的类。 从本质上讲，
接口是一种特殊的抽象类，这种抽象类中只包含常量和方法的定义
(JDK7.0及之前)， 而没有变量和方法的实现。

[Untitled](Java%20%E8%8D%89%E7%A8%BF%20db4d272d11f0438f8021f7a643820e83/Untitled%20Database%20e7d758edd5414deb95bee2faf27118f8.csv)

```
package interfacetest;

interface A {
    int x = 0;
}
class B {
    int x = 1;
}
public class C extends B implements A {
    public void pX() {
//        System.out.println(x);  // Error:(12, 28) java: 对x的引用不明确
        System.out.println(A.x); // 0
        System.out.println(super.x);  // 1
    }
    public static void main(String[] args) {
        new C().pX();
    }
}
```

在Java中，允许一个类的定义位于另一个类的内部，前者称为**内部类**，后者称为**外部类**

成员内部类（static成员内部类和非static成员内部类）
局部内部类（不谈修饰符, 方法内，代码块内，构造器内）、匿名内部类

```
package com.atguigu.java2;
/*
 * 类的内部成员之五：内部类
 * 1. Java中允许将一个类A声明在另一个类B中，则类A就是内部类，类B称为外部类
 *
 * 2.内部类的分类：成员内部类（静态、非静态）  vs 局部内部类(方法内、代码块内、构造器内)
 *
 * 3.成员内部类：
 *      一方面，作为外部类的成员：
 *          >调用外部类的结构
 *          >可以被static修饰
 *          >可以被4种不同的权限修饰
 *
 *      另一方面，作为一个类：
 *          > 类内可以定义属性、方法、构造器等
 *          > 可以被final修饰，表示此类不能被继承。言外之意，不使用final，就可以被继承
 *          > 可以被abstract修饰
 *
 *
 * 4.关注如下的3个问题
 *   4.1 如何实例化成员内部类的对象
 *   4.2 如何在成员内部类中区分调用外部类的结构
 *   4.3 开发中局部内部类的使用  见《InnerClassTest1.java》
 *
 */
public class InnerClassTest {
    public static void main(String[] args) {

        //创建Dog实例(静态的成员内部类):
        Person.Dog dog = new Person.Dog();
        dog.show();
        //创建Bird实例(非静态的成员内部类):
//      Person.Bird bird = new Person.Bird();//错误的
        Person p = new Person();
        Person.Bird bird = p.new Bird();
        bird.sing();

        System.out.println();

        bird.display("黄鹂");

    }
}

class Person{

    String name = "小明";
    int age;

    public void eat(){
        System.out.println("人：吃饭");
    }

    //静态成员内部类
    static class Dog{
        String name;
        int age;

        public void show(){
            System.out.println("卡拉是条狗");
//          eat();
        }

    }
    //非静态成员内部类
    class Bird{
        String name = "杜鹃";

        public Bird(){

        }

        public void sing(){
            System.out.println("我是一只小小鸟");
            Person.this.eat();//调用外部类的非静态属性
            eat();
            System.out.println(age);
        }

        public void display(String name){
            System.out.println(name);//方法的形参
            System.out.println(this.name);//内部类的属性
            System.out.println(Person.this.name);//外部类的属性
        }
    }

    public void method(){
        //局部内部类
        class AA{

        }
    }

    {
        //局部内部类
        class BB{

        }
    }

    public Person(){
        //局部内部类
        class CC{

        }
    }

}
```

异常：在Java语言中， 将程序执行中发生的不正常情况称为“异常” 。
(开发过程中的语法错误和逻辑错误不是异常)

Error： Java虚拟机无法解决的严重问题。 如： JVM系统内部错误、 资源耗尽等严重情况。 比如： StackOverflowError和OOM。 一般不编写针对性的代码进行处理。
Exception: 其它因编程错误或偶然的外在因素导致的一般性问题， 可以使用针对性的代码进行处理。 例如：
空指针访问
试图读取不存在的文件
网络连接中断
数组角标越界

异常处理

方式一： try-catch-finally
方式二： throws + 异常类型

Java提供的是异常处理的抓抛模型。
Java程序的执行过程中如出现异常， 会生成一个异常类对象，
该异常对象将被提交给Java运行时系统， 这个过程称为抛出
(throw)异常。
异常对象的生成
由虚拟机自动生成：程序运行过程中，虚拟机检测到程序发生了问题，如果在当
前代码中没有找到相应的处理程序，就会在后台自动创建一个对应异常类的实例
对象并抛出——自动抛出
由开发人员手动创建： Exception exception = new ClassCastException();——创
建好的异常对象不抛出对程序没有任何影响，和创建一个普通对象一样

 如果一个方法内抛出异常， 该异常对象会被抛给调用者方法中处
理。 如果异常没有在调用者方法中处理， 它继续被抛给这个调用
方法的上层方法。 这个过程将一直继续下去， 直到异常被处理。
这一过程称为捕获(catch)异常。
 如果一个异常回到main()方法， 并且main()也不处理， 则程序运
行终止。
 程序员通常只能处理Exception， 而对Error无能为力

try
捕获异常的第一步是用try{…}语句块选定捕获异常的范围， 将可能出现
异常的代码放在try语句块中。
catch (Exceptiontype e)
在catch语句块中是对异常对象进行处理的代码。 每个try语句块可以伴随
一个或多个catch语句， 用于处理可能产生的不同类型的异常对象

finally
捕获异常的最后一步是通过finally语句为异常处理提供一个
统一的出口，使得在控制流转到程序的其它部分以前，能够
对程序的状态作统一的管理。
不论在try代码块中是否发生了异常事件， catch语句是否执
行， catch语句是否有异常， catch语句中是否有return，
finally块中的语句都会被执行。
finally语句和catch语句是任选的

前面使用的异常都是RuntimeException类或是它的子类，这些类的异常的特
点是：即使没有使用try和catch捕获， Java自己也能捕获，并且编译通过
( 但运行时会发生异常使得程序运行终止 )。
如果抛出的异常是IOException等类型的非运行时异常，则必须捕获，否则
编译错误。也就是说，我们必须处理编译时异常，将异常进行捕捉，转化为
运行时异常

声明抛出异常是Java中处理异常的第二种方式
如果一个方法(中的语句执行时)可能生成某种异常， 但是并不能确定如何处理这
种异常， 则此方法应显示地声明抛出异常， 表明该方法将不对这些异常进行处理，
而由该方法的调用者负责处理。
在方法声明中用throws语句可以声明抛出异常的列表， throws后面的异常类型可
以是方法中产生的异常类型， 也可以是它的父类

重写方法不能抛出比被重写方法范围更大的异常类型。 在多态的情况下