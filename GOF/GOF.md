# 设计模式

UML：https://www.omg.org/uml/



## Iterator--一个一个遍历

![image-20220320211607972](E:\GitHubNote\Note\GOF\GOF.assets\image-20220320211607972.png)

### 角色

- Iterator(迭代器)：负责定义按顺序逐个遍历元素的接口（API）
- Concretelterator(迭代器的实现类)
- Aggregate(集合)
- ConcreateAggregate

![image-20211114010753060](GOF.assets/image-20211114010753060.png)

## Adapter--代码复用

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

public class PrintBanner extends Banner implements Print {}
    
	public PrintBanner(String string){
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

## Template Method--将具体处理交给子类

Template Method: 在**父类**中定义**处理流程**的框架（算法），在**子类中实现具体处理**

通过final修饰父类的流程方法，防止子类修改父类的处理流程

### 角色

AbstractClass(抽象类)

ConcreateClass(具体类)

### 类的层次与抽象类

站在子类的角度

- 在子类中可以使用父类中定义的方法
- 可以通过在子类中增加方法以实现新的功能
- 在子类中重写父类的方法可以改变程序的行为

站在父类的角度，在父类中声明抽象方法

- 期待子类去实现抽象方法
- 要求子类去实现抽象方法

## Factory Method--将实例的生成交给子类

用Template Method来构建生成实例的工厂，父类决定实例的生成方式，子类负责生成实例

![image-20211114194600240](GOF.assets/image-20211114194600240.png)

### 角色

- ConcreteProduct: 具体的产品
- ConcreteCreator: 具体的创建者
- Product: 产品
- Creator: 创建者，不用new 关键字来生成实例，而是调用生成实例的专用方法来生成实例，防止父类与其他具体类耦合

### Creator生成实例的方法

- 指定抽象方法

  ```java
  abstract class Factory{
  	public abstract Product createProduct(String name);
      ...
  }
  ```

- 为其实现默认处理，不推荐

  ```java
  class Factory{
  	public  Product createProduct(String name){
          return new Product(name);
      }
  
  }
  ```

- 在其中抛出异常

  如果未在子类总实现该方法，报错
  
  ```java
  class Factory{
  	public  Product createProduct(String name){
          throw new FactoryMethodRuntimeException();
      }
  }
  // 如果未在子类中实现该方法，程序报错
  ```

## Singleton--只有一个实例

Singleton类只会生成一个实例。

![image-20211114203435250](GOF.assets/image-20211114203435250.png)

```java
public class Singleton {
    private static Singleton singleton = new Singleton();
    private Singleton(){
        System.out.println("生成了一个实例");
    }

    public static Singleton getSingleton() {
        return singleton;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Begin");
        Singleton obj1 = Singleton.getSingleton();
        Singleton obj2 = Singleton.getSingleton();
        if(obj1 == obj2){
            System.out.println("obj1 == obj2");
        }else {
            System.out.println("obj1 <> obj2");
        }
        System.out.println("End.");
    }
}
```

1. 定义**static**修饰的成员变量singleton，并将其初始化为Singleton类的实例。初始化行为仅在**类被加载**的时候进行一次
2. Singleton类的构造函数为private，禁止从Singleton类外部调用构造函数


## Prototype--通过复制生成实例

通常我们使用new关键字指定类名来生成实列，但是也有**不指定类名来生成实列**。如下述情况

1. 对象种类繁多，无法将它们整合到一个类中

2. 难以根据类生成实列，生成实列的过程太过复杂

3. 解耦框架与生成的实例

   > 想要让生成实例的框架不依赖于具体的类，先“注册”一个“原型”实例，然后通过复制该实例来生成新的实例。



```
clone方法定义在java.lang.Object中, q
Cloneable接口中没有声明任何方法，只是用来标记。称为标记接口

```

## Builder--组装复杂的实例

### 角色

- Builder(建造者)：负责定义用于生成实例的接口。Builder中准备了用于生成实例的方法
- ConcreteBuilder: Builder的实现类
- Director(监工): 负责使用Builder来生成实例。它并不依赖于ConcreteBuilder, 只调用Builder角色中被定义的方法
- Client(使用者): 使用Builder

可替换性：一个类不知道知道调用的是哪个子类。

### 代码

```java
public abstract class Builder {
    public abstract void makeTitle(String title);
    public abstract void makeString(String str);
    public abstract void makeItems(String[] items);
    public abstract void close();
}

public class Director {
    private Builder builder;
    public Director(Builder builder){
        this.builder = builder;
    }

    public void construct(){
        builder.makeTitle("Greeting");
        builder.makeString("从早上至下午");
        builder.makeItems(new String[]{
                "早上好。",
                "下午好。"
        });
        builder.makeString("晚上");
        builder.makeItems(new String[]{
                "晚上好。",
                "晚安。",
                "再见"
        });
        builder.close();
    }
}

public class TextBuilder extends Builder {
    private StringBuffer buffer = new StringBuffer();           // 文档内容保存在该字段中
    public void makeTitle(String title) {                       // 纯文本的标题
        buffer.append("==============================\n");      // 装饰线
        buffer.append("『" + title + "』\n");                   // 为标题添加『』
        buffer.append("\n");                                    // 换行
    }
    public void makeString(String str) {                        // 纯文本的字符串
        buffer.append('■' + str + "\n");                       // 为字符串添加■
        buffer.append("\n");                                    // 换行
    }
    public void makeItems(String[] items) {                     // 纯文本的条目
        for (int i = 0; i < items.length; i++) {
            buffer.append("　・" + items[i] + "\n");            // 为条目添加・
        }
        buffer.append("\n");                                    // 换行
    }
    public void close() {                                       // 完成文档
        buffer.append("==============================\n");      // 装饰线
    }
    public String getResult() {                                 // 完成的文档
        return buffer.toString();                               // 将StringBuffer变换为String
    }
}

public class HTMLBuilder extends Builder{
    private String filename;                                                        // 文件名
    private PrintWriter writer;                                                     // 用于编写文件的PrintWriter
    public void makeTitle(String title) {                                           // HTML文件的标题
        filename = title + ".html";                                                 // 将标题作为文件名
        try {
            writer = new PrintWriter(new FileWriter(filename));                     // 生成 PrintWriter
        } catch (IOException e) {
            e.printStackTrace();
        }
        writer.println("<html><head><title>" + title + "</title></head><body>");    // 输出标题
        writer.println("<h1>" + title + "</h1>");
    }
    public void makeString(String str) {                                            // HTML文件中的字符串
        writer.println("<p>" + str + "</p>");                                       // 用<p>标签输出
    }
    public void makeItems(String[] items) {                                         // HTML文件中的条目
        writer.println("<ul>");                                                     // 用<ul>和<li>输出
        for (int i = 0; i < items.length; i++) {
            writer.println("<li>" + items[i] + "</li>");
        }
        writer.println("</ul>");
    }
    public void close() {                                                           // 完成文档
        writer.println("</body></html>");                                           // 关闭标签
        writer.close();                                                             // 关闭文件
    }
    public String getResult() {                                                     // 编写完成的文档
        return filename;                                                            // 返回文件名
    }
}

public class Main {
    public static void main(String[] argsArr) {
        String args = "plain";

//        if (args.length != 1) {
//            usage();
//            System.exit(0);
//        }
        if (args.equals("plain")) {
            TextBuilder textbuilder = new TextBuilder();
            Director director = new Director(textbuilder);
            director.construct();
            String result = textbuilder.getResult();
            System.out.println(result);
        } else if (args.equals("html")) {
            HTMLBuilder htmlbuilder = new HTMLBuilder();
            Director director = new Director(htmlbuilder);
            director.construct();
            String filename = htmlbuilder.getResult();
            System.out.println(filename + "文件编写完成。");
        } else {
            usage();
            System.exit(0);
        }
    }
    public static void usage() {
        System.out.println("Usage: java Main plain      编写纯文本文档");
        System.out.println("Usage: java Main html       编写HTML文档");
    }
}
```

## Abstract Factory--将关联零件组成产品

**抽象工厂**的工作就是将**抽象零件**组装成**抽象产品**，我们不关心零件的具体实现，而是只关心接口（API）

- AbstractProduct(抽象产品)

  AbstractProduct负责定义AbstractFactory角色生成的抽象零件和产品的接口

- AbstractFactory

  负责定义用于生成抽象产品的接口

- ConcreteProduct

- ConcreteFactory

## Bridge--将类的功能层次结构与实现层次结构分离

**类的层次结构的两个作用**

1. 希望**增加新功能**，功能层次结构，子类扩展父类
   - 父类具有基本功能
   - 在子类中增加新的功能
   
2. 希望**增加新的实现**时，实现层次结构，子类实现父类
   
   如Template method
   
   - 父类通过声明**抽象方法**来定义接口（定义流程顺序）
   - 子类通过实现具体方法来实现接口
   
3. 类的层次接口的混杂与分离

   将类的**功能层次结构**与实现层次结构分离, 使用Bridge进行连结

## Strategy--整体地替换算法

## Composite

容器与内容的一致性

目录条目=文件+文件夹

## Decorator--装饰边框与被装饰物的一致性



