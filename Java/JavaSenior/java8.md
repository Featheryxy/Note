Java是面向对象语音，所以必须要创建一个类，由类的实例对象中的某个方法来封装代码

Java 是强类型语言，必须声明参数类型

lambda表达式: (参数类型 变量，……) -> 表达式。

 如果参数类型可被推导，则参数类型可被省略，如果没有参数或只有一个参数，小括号也可省略



函数式接口 只包含一个抽象方法的接口

Lambda表达式 函数式接口的实例



方法引用：传递给其他代码的操作已经有实现的方法

```java
button.setOnAction(event -> System.out.println(event));

// 方法引用, 使用 :: 来分隔方法名和 （对象或类）的名字
button.setOnAction(System.out::println);

对象 :: 实例方法
类 :: 静态方法
类 :: 实例方法    
this :: 方法
super :: 方法    
```

构造器引用

```java
Button[] buttons = stream.toArray(Button[] :: new)
```





一个内部类可以访问任何有效的final局部变量



