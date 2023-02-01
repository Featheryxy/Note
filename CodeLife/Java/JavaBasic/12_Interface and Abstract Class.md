# Interface and Abstract Class

Interface ：一种特殊的抽象类，只包含常量和方法的定义， 而没有变量和方法的实现，也可以有静态方法和默认方法

abstract class：由abstract修饰的类，不能实例化

抽象层次不同：抽象类是对类（属性，行为）的抽象，而接口是对行为的抽象。

跨域不同：抽象类是具有相似特点的类的，而接口可以跨不同的类

设计层次不同：抽象类是自下而上来设计的，而接口是自上而下设计



## Interface

1. **接口是常量和抽象方法的集合**，也可以有静态方法和默认方法。

   > 常量（public final static）
   >
   > 抽象方法（public abstract）

2. 接口还有**标识**作用

   > 里面没有任何方法和常量，如Remote接口

3. 允许多继承

- 访问修饰符一定为public，因为需要被实现
- 所有**成员变量**都默认是由**public static final**修饰
- 所有抽象方法都默认是由public abstract修饰的，无方法体
- 可以有static method 和 default method，必须要有方法体
  - static method 可以通过 接口.方法名() 调用
  - default method 需要子类来重写

```java
package test;

public interface IA {
    public final static int a=10;
    int b = 10; // 默认为 public final static

    public abstract void say(String name); //默认为 public abstract

    // static修饰的方法必须要有方法体
    public default boolean isTen(){ // 默认为 public，
        return b == 10;
    }

    static void hello() { // 默认为 public
        System.out.println("hello");
    }

    class B implements IA{
        @Override
        public void say(String name) {
            System.out.println(name);
        }

        @Override
        public boolean isTen() {
            return false;
        }
    }
    public static void main(String[] args) {
        IA.hello(); // hello
        System.out.println(IA.b); // 10
        IA ia = new B();
        ia.isTen();
        ia.say("milo");
    }
}

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

## abstract class

其主要作用用于继承

抽象方法：由abstract修饰的方法；只有方法的声明，没有方法的实现。以分号结束：

>  public abstract void talk();

抽象类：由abstract修饰的类。

> 抽象类除了不能实例化对象之外，类的其它功能依然存在，成员变量、成员方法和构造方法的访问方式和普通类一样。

抽象类规则

1. 抽象类不能被实例化
2. 抽象类中不一定包含抽象方法，但是有抽象方法的类必定是抽象类。
3. 抽象类中的抽象方法只是声明，不包含方法体
4. 构造方法，类方法（用 static 修饰的方法）不能声明为抽象方法
5. 抽象类的子类必须给出抽象类中的抽象方法的具体实现，除非该子类也是抽象类
6. 不能用abstract修饰变量、代码块、构造器；
7. 不能用abstract修饰私有方法、静态方法、 final的方法、 final的类

## differ

| No.  | 区别点       | 抽象类                                                       | 接口                                         |
| ---- | ------------ | ------------------------------------------------------------ | -------------------------------------------- |
| 1    | 定义         | 包含抽象方法的类                                             | 主要是抽象方法和全局常量的集合               |
| 2    | 组成         | 构造方法、抽象方法、普通方法、 常量、变量                    | 常量、抽象方法、 (jdk8.0:默认方法、静态方法) |
| 3    | 使用         | 子类继承抽象类(extends)                                      | 子类实现接口(implements)                     |
| 4    | 关系         | 抽象类可以实现多个接口                                       | 接口不能继承抽象类，但允许继承多个接口       |
| 5    | 常见设计模式 | 模板方法                                                     | 简单工厂、工厂方法、代理模式                 |
| 6    | 对象         | 都通过对象的多态性产生实例化对象                             |                                              |
| 7    | 局限         | 抽象类有单继承的局限                                         | 接口没有此局限                               |
| 8    | 实际         | 作为一个模板                                                 | 是作为一个标准或是表示一种能力               |
| 9    | 选择         | 如果抽象类和接口都可以使用的话，优先使用接口，因为避免单继承的局限 |                                              |

### 语法层次

1. 抽象类可以有构造方法，接口中不能有构造方法。
2. 抽象类中可以有普通成员变量，接口中没有普通成员变量
3. 抽象类中可以包含非抽象的普通方法，接口中的所有方法必须都是抽象的，不能有非抽象的普通方法。
4. 抽象类中的抽象方法的访问类型可以是public，protected和（默认类型,虽然eclipse下不报错，但应该也不行），但接口中的抽象方法只能是public类型的，并且默认即为public abstract类型。
5. 抽象类中可以包含静态方法，接口中不能包含静态方法
6. 抽象类和接口中都可以包含静态成员变量，抽象类中的静态成员变量的访问类型可以任意，但接口中定义的变量只能是public static final类型，并且默认即为publicstatic final类型。
7. 一个类可以实现多个接口，但只能继承一个抽象类。

### 设计层次

1. 抽象层次不同：接口是对行为的抽象，侧重于扩展类的行为，该类有什么功能；

   而抽象类则是对类（属性，行为）的抽象，是一种模板设计，侧重于类的定义，这个类是什么。

2. 跨域不同：抽象类是具有相似特点的类的，而接口可以跨不同的类

3. 设计层次不同：抽象类是自下而上来设计的，我们首先要知道子类才能抽象出父类，而接口不同，它不需要知道子类的存在，只需要第一一个规则即可