# Java

static

被修饰后的成员具备以下特点：
随着类的加载而加载  clinit
优先于对象存在  

修饰的成员，被所有对象所共享 (共享一块内存)
访问权限允许时，可不创建对象，直接被类调用



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