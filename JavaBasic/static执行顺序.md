```java
public class A {
    public A(){
        System.out.println("A的构造函数");
    }
    
    {
        System.out.println("A的代码块");
    }
    
    static {
        System.out.println("A的静态代码块");
    }
}

class B extends A{
    public B(){
        System.out.println("B的构造函数");
    }

    {
        System.out.println("B的代码块");
    }

    static {
        System.out.println("B的静态代码块");
    }

    public static void main(String[] args) {
        new B();
        /*
        A的静态代码块
        B的静态代码块
        A的代码块
        A的构造函数
        B的代码块
        B的构造函数
         */
    }
}
```