---
title: 内部类
date: 2020-10-11 18:58:01
tags:
categories: Java
---

对内部类的简单回顾

<!-- more -->



# Inner Class

在一个类中定义另一个类，前者称为**内部类**，后者称为**外部类**

分类：

- 成员内部类（static成员内部类和非static成员内部类）
- 局部内部类（不谈修饰符,  方法内，代码块内，构造器内）、匿名内部类

匿名内部类是局部内部类的一种特殊形式，没有类名。其在创建对象的时候定义类，其本质**是一个接口或者抽象类的实现类**。而lambda表达式就是内部类的简化写法，省去类的定义和方法定义。因为在加载匿名内部类之前已经加载了父类或父接口，而父类或父接口已经有了该匿名内部类的类定义和方法定义，故可以省去。

**内部类可以直接访问外部类的成员，包括私有。**

外部类要访问内部类的成员，必须创建内部类对象。

## 访问特点

- 内部类可以直接访问外部类的成员，包括私有。
- 外部类要访问内部类的成员，必须创建内部类对象。
- 外部类只能使用`default`和`protected`修饰
  - 外部类只有两个作用域：同包，任何位置。因此，只需要两种控制权限：包控制权限和公开访问权限。如果使用`protected`，则其作用和`public`相同

## 成员内部类

```java
class Outer {
    // 成员内部类
    public class Inner{

    }
}

public class Test{
    public static void main(String[] args) {
        // 创建外部类对象，都在外部类外部

        // 使用成员内部类造对象
		// Inner inner = new Outer.Inner(); wrong
        // 格式：外部类名.内部类名 i = new 外部类().new 内部类();
        Outer.Inner oi = new Outer().new Inner();
    }
}
```

## 局部内部类

- 局部内部类，不能使用访问修饰符，`static`, 但可以使用`final, abstract`

```java
class Outer {
    public void method(){
        int num=10;
        // 局部内部类
        class Inner{
            public void method(){
                System.out.println(num);
            }
        }
        Inner inner = new Inner();
        inner.method();
    }
}

public class Test{
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.method();
        // 10
    }
}
```

## 静态成员内部类

- 静态成员不能访问非静态成员， 非静态成员可以访问静态成员， 静态成员的创建在类加载过程中的初始化阶段完成， 创建的时间比非静态成员早

```java
class Outer {
    // 静态成员内部类
    public static class Inner{
        public void method(){
            System.out.println("静态内部类中的成员方法");

        }
    }
}

public class Test{
    public static void main(String[] args) {
         //静态内部类造对象
        // 类名.静态变量名
        Outer.Inner inner = new Outer.Inner();
        inner.method();
        // 静态内部类中的成员方法
    }
}
```

## 匿名内部类

- 匿名内部类是局部内部类的一种特殊形式，没有类名。其在创建对象的时候定义类，而lambda表达式就是内部类的简化写法。其本质**是一个接口或者抽象类的实现类**

### 接口

```java
interface A{
    void method();
}

class B implements A{
    @Override
    public void method() {
		System.out.println("接口A的实现类B");
    }
}


public class Test {
    public static void main(String[] args) {
        A a = new B(); // 多态，对象的创建
        a.method();// 调用接口A的实现类B的方法method



        // 由于不创建接口A的实现类，直接使用A接口的匿名内部类
        // 创建匿名内部类对象，并且重写了接口中的抽象方法
        A aa = new A() {
            @Override
            public void method() {
                System.out.println("接口A的匿名实现类");
            }
        };
        aa.method();
        // 接口A的匿名实现类
    }
}
```

### 抽象类

```java
abstract class C{
    public abstract  void method1();
    public abstract  void method2();
}

class D extends C{
    @Override
    public void method1() {
        System.out.println("抽象类的子类");
    }

    @Override
    public void method2() {
        System.out.println("抽象类的子类");
    }
}

public class Test {
    public static void main(String[] args) {
        D d = new D();
        d.method1();
        d.method2();
        System.out.println("+++++++++");
        // 匿名内部类的形式创建抽象类对象
        C c = new C() {
            @Override
            public void method1() {
                System.out.println("匿名抽象类");
            }

            @Override
            public void method2() {
                System.out.println("匿名抽象类");
            }
        };
        c.method1();
        c.method2();
       	/* 
        抽象类的子类
        抽象类的子类
        +++++++++
        匿名抽象类
        匿名抽象类
        */
    }
}

```

### 接口作为参数

函数式编程，传递行为

1. **实现多态性：** 接口允许您实现多态性。如果方法接受接口类型的参数，那么您可以传递任何实现该接口的类的实例作为参数，从而实现不同类的对象之间的通用操作。
2. **实现回调：** 接口可用于实现回调机制。通过传递实现某个接口的对象作为参数，您可以将回调函数传递给其他方法，从而在特定事件发生时执行相应的操作。这在事件处理和异步编程中非常有用。
3. **策略模式：** 接口可用于实现策略模式。通过传递不同的实现了相同接口的类作为参数，您可以在运行时选择不同的策略或算法来实现不同的行为。
4. **解耦合：** 使用接口作为参数可以降低代码的耦合度。当方法接受接口类型而不是具体的类类型时，它可以与多个不同的类协同工作，而不需要直接依赖于特定的类。

```java
interface A{
    void method();
}
public class Test {
    public static void main(String[] args) {
        method(new A() {
            @Override
            public void method() {
                System.out.println("接口传参");
            }
        });

    }

    public static void method(A a){

    }
}

```

## 面试题1

```java
class Outer {

    // jdk 1.8 之前会报错，必须给局部变量加final之后，局部内部类才能使用
    public void method(){
        // 在编译的时候自动为i添加final关键字
        int i = 1000; // 局部变量，保存在Java虚拟机栈中，方法执行结束后，释放内存
        class Inner2{
            public void method(){
                System.out.println(i);
            }
        }
        // 局部内部类只能在局部范围中使用
        Inner2 i2 = new Inner2(); // 实例对象保存在堆内存空间
        i2.method();
    }
}

public class Test{
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.method();
        // 1000
    }
}
```

下面会出错

```java
class Outer {

    // jdk 1.8 之前会报错，必须给局部变量加final之后，局部内部类才能使用
    public void method(){
        int i = 1000; // 局部变量，保存在Java虚拟机栈中，方法执行结束后，释放内存
        class Inner2{
            public void method(){
                System.out.println(i);
            }
        }
        // 局部内部类只能在局部范围中使用
        Inner2 i2 = new Inner2(); // 实例对象保存在堆内存空间
        i2.method();
    }
}

public class Test{
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.method();
        // 1000
    }
}
```

## 面试题2

```java
package main.inner.demo5;

interface Inter{
    void show();
}

class Outer{
    // 补齐代码，输出HelloWorld
    public static Inter method(){
        Inter i = new Inter() {
            @Override
            public void show() {
                System.out.println("HelloWorld");
            }
        };
        return i;
    }
}

class OuterDemo{
    public static void main(String[] args) {
        Outer.method().show();
    }
}

```

## lambda表达式

匿名内部类的简写，**省去类的定义和方法定义**。因为在加载匿名内部类之前已经加载了父类或父接口，而父类或父接口已经有了该匿名内部类的类定义和方法定义，故可以省去

```java
package classdemo;

import java.util.function.Consumer;
import java.util.function.Function;

public class InnerClassDemo {
    public static void main(String[] args) {
        A a = new B(); // 多态
        a.method("a");
        // 接口A的实现类B

        // 使用A接口的匿名内部类
        // 创建匿名内部类对象
        A aa = new A() {
            @Override
            public void method(String a) {
                System.out.println("接口A的匿名实现类");
            }
        };

        // 既然只有一个方法，那么方法名可以省略
        A aaa = (String nn)-> {
                System.out.println("接口A的匿名实现类");
            };

        // 省去方法中的参数定义
        A aaaa = (nn)-> {
            System.out.println("接口A的匿名实现类");
        };

        A aaaaa = (nn)-> System.out.println("接口A的匿名实现类"+nn);
        aaaaa.method("究极体");

        // Consumer 可以使用任何一个类的方法，该方法的参数列表和函数式接口中声明的方法一样
        //
        Consumer<String> tConsumer = (nn) -> System.out.println("接口A的匿名实现类" + nn);
        tConsumer.accept("执行了concumer");

        // :: 方法引用， 将System.out的println方法地址赋给接口A中的方法
        A a6 = System.out::println;
        a6.method("::");

        // 函数接口可以使用任何一个类的方法，该方法的参数列表和函数式接口中声明的方法一样
        C c=new C();
//        Consumer<String> dec = c::dec;
        A dd = c::dec;
        dd.method("成功");

        // 1. 去
//        A aa = () ->{
//
//                System.out.println("接口A的匿名实现类");
//
//        };
//        aa.method();
        // 接口A的匿名实现类
    }
}

// 函数式接口是只包含一个方法的接口
interface A{
    void method(String a);
}

class B implements A{
    @Override
    public void method(String a) {
        System.out.println("接口A的实现类B: "+a);
    }
}


class C{
    public void dec(String a) {
        System.out.println("C执行了"+a);
    }

    public void decB(String a) {
        System.out.println("C执行了"+a);
    }
}

```

