# Reflection

反射就是把java类中的各种成分映射成一个个的Java对象，如Fields，Constructor对象，我们可以通过Class对象来获取类的结构信息。

Class是一个普通的类，这个类描述的是所有类的公共特性。

其构造方法为private，所以Class对象的由JVM来创建，将class文件读入内存，并为之创建一个Class对象



Java运行时系统始终为所有对象维护一个运行时类型标识。保存这些信息的类名为Class.

在启动时，包含main方法的类被加载，它会加载所有需要的类。这些被加载的类又要加载它们需要的类，以此类推。这将花费很长时间，可以使用Class.forName手工强制加载其他类。

- 可以使用==运算符来实现两个类对象的比较

```java
if(student.getClass() == Student.class);
```

## 1 概述

### 1.1 概念

- Reflection（反射）是被视为**动态语言**的关键，反射机制允许程序在**执行期**借助于Reflection API**取得任何类的内部信息**，并能直接操作任意对象的内部属性及方法  

- **加载完类**之后， 在**堆内存**的方法区中就产生了一个**Class类型的对象**（ 一个类只有一个Class对象） ， 这个对象就包含了完整的类的结构信息。 我们可以通过这个对象看到类的结构。 这个对象就像一面镜子， 透过这个镜子看到类的结构， 所以， 我们形象的称之为： 反射  

### 1.2 动态语言 vs 静态语言  

1. 动态语言
   是一类在运行时可以改变其结构的语言：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。**通俗点说就是在运行时代码可以根据某些条件改变自身结构**。
   主要动态语言： Object-C、 C#、 JavaScript、 PHP、 Python、 Erlang。  

2. 静态语言  

   与动态语言相对应的， 运行时结构不可变的语言就是静态语言。如Java、 C、C++  

3. Java不是动态语言， 但Java可以称之为“准动态语言” 。 即Java有一定的动态性， 我们可以利用反射机制、 字节码操作获得类似动态语言的特性。Java的动态性让编程的时候更加灵活！  

## 2 反射

### 2.1 常规操作

```java
package com.atguigu.java;

public class Person {

    private String name;
    public int age;

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Person(String name, int age) {

        this.name = name;
        this.age = age;
    }

    private Person(String name) {
        this.name = name;
    }

    public Person() {
        System.out.println("Person()");
    }

    public void show(){
        System.out.println("你好，我是一个人");
    }

    private String showNation(String nation){
        System.out.println("我的国籍是：" + nation);
        return nation;
    }
}
```

```java
//反射之前，对于Person的操作
@Test
public void test1() {

    //1.创建Person类的对象
    Person p1 = new Person("Tom", 12);

    //2.通过对象，调用其内部的属性、方法
    p1.age = 10;
    System.out.println(p1.toString());

    p1.show();

    //在Person类外部，不可以通过Person类的对象调用其内部私有结构。
    //比如：name、showNation()以及私有的构造器
}
```

### 2.2 反射的使用

```java
@Test
public void test2() throws Exception{
    Class clazz = Person.class;
    //1.通过反射，创建Person类的对象
    Constructor cons = clazz.getConstructor(String.class,int.class);
    Object obj = cons.newInstance("Tom", 12);
    Person p = (Person) obj;
    System.out.println(p.toString());
    //2.通过反射，调用对象指定的属性、方法
    //调用属性
    Field age = clazz.getDeclaredField("age");
    age.set(p,10);
    System.out.println(p.toString());

    //调用方法
    Method show = clazz.getDeclaredMethod("show");
    show.invoke(p);

    System.out.println("*******************************");

    //通过反射，可以调用Person类的私有结构的。比如：私有的构造器、方法、属性
    //调用私有的构造器
    Constructor cons1 = clazz.getDeclaredConstructor(String.class);
    cons1.setAccessible(true);
    Person p1 = (Person) cons1.newInstance("Jerry");
    System.out.println(p1);

    //调用私有的属性
    Field name = clazz.getDeclaredField("name");
    name.setAccessible(true);
    name.set(p1,"HanMeimei");
    System.out.println(p1);

    //调用私有的方法
    Method showNation = clazz.getDeclaredMethod("showNation", String.class);
    showNation.setAccessible(true);
    String nation = (String) showNation.invoke(p1,"中国");//相当于String nation = p1.showNation("中国")
    System.out.println(nation);

}
```

## 3 java.lang.Class

### 3.1 概述

对象照镜子后可以得到的信息：某个类的属性、方法和构造器、某个类到底实现了哪些接口。对于每个类而言， JRE 都为其保留一个不变的 Class 类型的对象。一个 Class 对象包含了特定某个结构(class/interface/enum/annotation/primitive type/void/[])的有关信息。

- Class本身也是一个类
- Class 对象只能由系统建立对象
- **一个加载的类**在 JVM 中**只会有一个Class实例**
- **一个Class对象**对应的是一个加载到JVM中的一个**.class文件**
-  每个类的实例都会记得自己是由哪个 Class 实例所生成
- 通过Class可以完整地得到一个类中的所有被加载的结构
- Class类是Reflection的根源，针对任何你想动态加载、运行的类，唯有先获得相应的Class对象  

1. 类的加载过程：
   程序经过javac.exe命令以后，会生成一个或多个字节码文件(.class结尾)。
   接着我们使用java.exe命令对某个字节码文件进行解释运行。相当于将某个字节码文件加载到内存中。此过程就称为类的加载。加载到内存中的类，我们就称为运行时类，此运行时类，就作为Class的一个实例。

2. 换句话说，**Class的实例就对应着一个运行时类**。
3. 加载到内存中的运行时类，会缓存一定的时间。在此时间之内，我们可以通过不同的方式来获取此运行时类。

### 3.2 获取Class的实例

```java
@Test
    public void test3() throws ClassNotFoundException {
        //方式一：调用运行时类的属性：.class
        Class clazz1 = Person.class;
        System.out.println(clazz1);
        
        //方式二：通过运行时类的对象,调用getClass()
        Person p1 = new Person();
        Class clazz2 = p1.getClass();
        System.out.println(clazz2);

        //方式三：调用Class的静态方法：forName(String classPath)
        Class clazz3 = Class.forName("com.atguigu.java.Person");
//        clazz3 = Class.forName("java.lang.String");
        System.out.println(clazz3);

        System.out.println(clazz1 == clazz2);
        System.out.println(clazz1 == clazz3);

        //方式四：使用类的加载器：ClassLoader  (了解)
        ClassLoader classLoader = ReflectionTest.class.getClassLoader();
        Class clazz4 = classLoader.loadClass("com.atguigu.java.Person");
        System.out.println(clazz4);

        System.out.println(clazz1 == clazz4);
    }
```

### 3.3 Class对象类型

（1） class：
外部类， 成员(成员内部类， 静态内部类)， 局部内部类， 匿名内部类
（2） interface： 接口
（3） []：数组
（4） enum：枚举
（5） annotation：注解@interface
（6） primitive type：基本数据类型
（7） void  

```java
@Test
public void test4(){
    Class c1 = Object.class;
    Class c2 = Comparable.class;
    Class c3 = String[].class;
    Class c4 = int[][].class;
    Class c5 = ElementType.class;
    Class c6 = Override.class;
    Class c7 = int.class;
    Class c8 = void.class;
    Class c9 = Class.class;

    int[] a = new int[10];
    int[] b = new int[100];
    Class c10 = a.getClass();
    Class c11 = b.getClass();
    // 只要数组的元素类型与维度一样，就是同一个Class
    System.out.println(c10 == c11);

}
```

## 4 创建运行时类的对象

### 4.1 **newInstance**()

**newInstance**(): 调用此方法，创建对应的运行时类的对象。内部调用了运行时类的**空参的构造器**。

要想此方法正常的创建运行时类的对象，要求：

1. 运行时类必须提供空参的构造器
2. 空参的构造器的访问权限得够。通常，设置为public。

在javabean中要求提供一个public的空参构造器。原因：

1. 便于通过反射，创建运行时类的对象
2. 便于子类继承此运行时类时，默认调用super()时，保证父类有此构造器

```java
@Test
public void test1() throws IllegalAccessException, InstantiationException {

    Class<Person> clazz = Person.class;
    Person obj = clazz.newInstance();
    System.out.println(obj);
    // Person{name='null', age=0}
}
```

### 4.2 动态性

```java
@Test
public void test2(){

    for(int i = 0;i < 100;i++){
        int num = new Random().nextInt(3);//0,1,2
        String classPath = "";
        switch(num){
            case 0:
                classPath = "java.util.Date";
                break;
            case 1:
                classPath = "java.lang.Object";
                break;
            case 2:
                classPath = "com.atguigu.java.Person";
                break;
        }

        try {
            Object obj = getInstance(classPath);
            System.out.println(obj);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
```

## 5 获取运行时类的完整结构  

```java
@MyAnnotation(value="hi")
public class Person extends Creature<String> implements Comparable<String>,MyInterface{

    private String name;
    int age;
    public int id;

    public Person(){}

    @MyAnnotation(value="abc")
    private Person(String name){
        this.name = name;
    }

     Person(String name,int age){
        this.name = name;
        this.age = age;
    }
    @MyAnnotation
    private String show(String nation){
        System.out.println("我的国籍是：" + nation);
        return nation;
    }

    public String display(String interests,int age) throws NullPointerException,ClassCastException{
        return interests + age;
    }


    @Override
    public void info() {
        System.out.println("我是一个人");
    }

    @Override
    public int compareTo(String o) {
        return 0;
    }

    private static void showDesc(){
        System.out.println("我是一个可爱的人");
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", id=" + id +
                '}';
    }
}
```

- `getFields()` : 获取当前**运行时类**及其**父类**中声明为**public访问权限的属性**
- `getDeclaredFields()`: 获取当前**运行时类**中声明的**所有属性**（包括private）。（不包含父类中声明的属性）

```java
@Test
public void test1(){

    Class clazz = Person.class;

    //获取属性结构
    //getFields():获取当前运行时类及其父类中声明为public访问权限的属性
    Field[] fields = clazz.getFields();
    for(Field f : fields){
        System.out.println(f);
    }
    System.out.println();

    //getDeclaredFields():获取当前运行时类中声明的所有属性。（不包含父类中声明的属性）
    Field[] declaredFields = clazz.getDeclaredFields();
    for(Field f : declaredFields){
        System.out.println(f);
    }
}
```

## 6 调用运行时类的指定结构

### 6.1 指定的属性

```java
@Test
public void testField1() throws Exception {
    Class clazz = Person.class;

    //创建运行时类的对象
    Person p = (Person) clazz.newInstance();

    //1. getDeclaredField(String fieldName):获取运行时类中指定变量名的属性
    Field name = clazz.getDeclaredField("name");

    //2.保证当前属性是可访问的
    name.setAccessible(true);
    //3.获取、设置指定对象的此属性值
    name.set(p,"Tom");

    System.out.println(name.get(p));
}
```

### 6.2 指定的方法

```java
@Test
    public void testMethod() throws Exception {

        Class clazz = Person.class;

        //创建运行时类的对象
        Person p = (Person) clazz.newInstance();

        /*
        1.获取指定的某个方法
        getDeclaredMethod():参数1 ：指明获取的方法的名称  参数2：指明获取的方法的形参列表
         */
        Method show = clazz.getDeclaredMethod("show", String.class);
        //2.保证当前方法是可访问的
        show.setAccessible(true);

        /*
        3. 调用方法的invoke():参数1：方法的调用者  参数2：给方法形参赋值的实参
        invoke()的返回值即为对应类中调用的方法的返回值。
         */
        Object returnValue = show.invoke(p,"CHN"); //String nation = p.show("CHN");
        System.out.println(returnValue);

        System.out.println("*************如何调用静态方法*****************");

        // private static void showDesc()

        Method showDesc = clazz.getDeclaredMethod("showDesc");
        showDesc.setAccessible(true);
        //如果调用的运行时类中的方法没有返回值，则此invoke()返回null
//        Object returnVal = showDesc.invoke(null);
        Object returnVal = showDesc.invoke(Person.class);
        System.out.println(returnVal);//null

    }
```

### 6.3 指定的构造器

```java
@Test
    public void testConstructor() throws Exception {
        Class clazz = Person.class;

        //private Person(String name)
        /*
        1.获取指定的构造器
        getDeclaredConstructor():参数：指明构造器的参数列表
         */

        Constructor constructor = clazz.getDeclaredConstructor(String.class);

        //2.保证此构造器是可访问的
        constructor.setAccessible(true);

        //3.调用此构造器创建运行时类的对象
        Person per = (Person) constructor.newInstance("Tom");
        System.out.println(per);

    }

```

## 7 反射的应用：动态代理  

## Others

Class:Class就是一个普通的类，这个类描述的是所有的类的公共特性。如所有的类，都有一个类名，都有0个或者多个字段
使用，由于其构造函数为私有的，不能使用关键字new

```java
public static void main(String[] args){
       //第一种
       Class c1 = String.class;
	   // 一般我们把Class的对象叫字节码
       //第二种
       String s = "hello,world";
       Class c2 = s.getClass();
		//第三种,以上面的Book类为例,其实就是动态加载类，注意捕获异常，因为类有可能不存在
   		try {
       		Class c3 = Class.forName("com.test.Book");
   		} catch (ClassNotFoundException e) {
       		e.printStackTrace();
        }
}
```

## Reference

   https://www.cnblogs.com/lingyejun/p/17034074.html
