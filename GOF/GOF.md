# 设计模式

UML：https://www.omg.org/uml/

箭头方向：知道对方的信息时才能指向对方，

子类继承，扩展了父类，子类指向父类



```java
// composition 组合 实心菱形 part of, 关系更强
// Engine的生命周期是与Car一致的
public class Engine{
    
}

public class Car{
    Engine e = new Engine();
}

// aggregation 聚合 空心菱形 has a 关系一般
// Address，它是在Person之外创建的，所以即使Person被回收了，Address也不一定马上也会回收
public class Address{
    
}
public class Person{
    private Address address;
    public Person(Address address){
		this.address = address;
    }
}
```







## Iterator

一个一个遍历

## Adapter

Adapter模式会对现有的类进行适配，生成新的类，也成为Wrapper模式

> 不修改已有的代码，扩展功能

Adapter模式有以下两种

- 类适配器模式（使用继承的适配器）
- 对象适配器模式（使用委托的适配器）

### 类适配器模式

![image-20211107140623776](GOF.assets/image-20211107140623776.png)

PrintBanner 为适配器，使Banner能够适用于Print

```java
public class Banner {
    private String string;

    public Banner(String string){
        this.string = string;
    }

    public void showWithParen(){
        System.out.println("("+string+")");
    }

    public void showWithAster(){
        System.out.println("*"+string+"*");
    }
}

public interface Print {
    public abstract void printWeak();

    public abstract void printStrong();
}

    super(string);
    }

    @Override
    public void printWeak() {
        showWithParen();
    }

    @Override
    public void printStrong() {
        showWithAster();
    }
}


public class Main {
    public static void main(String[] args) {
        Print p = new PrintBanner("Hello");
        p.printWeak();
        p.printStrong();
        // (Hello)
		// *Hello*
    }
}
```

### 对象适配器模式

```java
```

### 角色

Target: 目标，所要实现的功能 Print

Clinet: 请求者 Main

Adaptee：被适配者 Banner

Adapter: 适配者

![image-20211107144617050](GOF.assets/image-20211107144617050.png)

