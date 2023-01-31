# Class and Instance

类是对一类事物的描述，是抽象的、概念上的定义
对象是实际存在的该类事物的每个个体，因而也称为实例(instance)。



JVM以类为模板，在堆中构造出实例。

类元信息存储在栈中，一个.class文件，有且只有一个全限定名称，只有一个Class对象实例与之对应。

对象实例保存在堆中，可以有多个。

所以先有类，再有实例，实例方法可以访问类属性，而类方法不能访问实例变量。

类属性和方法通过static 修饰

### class

class —> instance

- instance field
- method
    - constructor
    - mutator method：更改器方法
    - accessor method：访问器方法

对象的三个主要特性

- behavior：对对象的操作
- state：调用方法后，对象会如何响应
- identity：区分相同状态与行为的不同对象

类之间的关系

- 依赖（uses-a）
- 聚合（has-a）
- 组合（contains-a）
- 继承（is-a）

```java
/**
new Date(); 产生一个对象，返回一个引用。
将引用赋值给对象变量deadline
*/
Date deadline = new Date();
```

```java
class ClassName{
	field1; 
	field2;
	...
	constructor1;
	constructor2;
	...
	method1;
	method2;
	...
}
```

### extends

继承：基于已有的类创建新的类。i.e.：复用这些类的方法，而且可以增加一些新的方法和字段。

使用依据：if student is a people, then we use class student extends people.

```java
public classPeople {
	private Stringname;
	private intage;
	
	public People(){
	
	}
	
	public People(String name,intage){
		this.name= name;
		this.age= age;
	}
	
	public void introduce(){
	      System.out.println("My name is "+name+", I'm "+age+" year old.");
	}
}

public class Student extends People {
	private String degree;

	public Student(){

	}

	public Student(String name, int age, String degree){
		super(name, age);
		this.degree = degree;
	}

	// 方法覆盖
	@Override
	public void introduce() {
		// 利用super关键字调用超类的方法
		super.introduce();
		System.out.println("I have "+degree+" degree!");
	}

	public static void main(String[] args) {
		Student student = new Student("Milo", 25, "master");
		student.introduce();
	}
}
```

### this and super

this

1. 指示**隐式参数的引用**
2. 调用该类的**其他构造器**

super

1. 调用超类的方法
2. 调用超类的**构造器**

### 多态

多态：一个对象变量可以指示多种实际类型的现象。对象变量是多态的（polymorphic）

动态绑定：运行时能够自动选择适当的方法.

原理：每个类会维护一个方法表（method table），其中列出了所有的签名和要调用的实际方法。首先虚拟机获取多态变量people的People和Student的方法表，然后查找相同签名的方法，最后再调用

方法签名：方法的名字和参数列表

```java
People people;
people = new People();
people = new Student();
```

### 强制类型转换

原因：暂时忽视对象的实际类型之后使用对象的全部功能。每个对象变量都有一个类型，类型描述了这个变量所引用的以及能够引用的对象类型。

```java
if (arr[1] instanceof People){
	people = (People)arr[1];
}
```

### parameter

隐式（implicit）参数：field1, this关键字指示隐式参数

显式（explicit）参数：method中的参数

不要返回可变对象引用的访问器方法，应该对它进行克隆

```java
class Employee{
	private Date hireDay;
	public Date getHireDay(){
		return hireDay; // BAD
	}
}

class Employee{
	private Date hireDay;
	public Date getHireDay(){
		return (Date)hireDay.clone(); // OK
	}
}

```

### final

final修饰实例字段，必须在构造对象时初始化，i.e.: 在构造器执行后，该值不能被修改

final修饰变量时，变量中的**对象引用不可变**，但是这个对象的内容可以更改。

final修饰类时，该类不能被继承，类中的方法不会被覆盖，默认都是final

final修饰方法时，该**方法可以被继承**，**但是不能被覆盖override**

```java
final StringBuilder evaluations;
evaluations =newStringBuilder();
evaluations.append(LocalDate.now()+": Gold star!\n");
System.out.println(evaluations);

final intage = 25;
age = 13;// error
```

### static

static修饰的变量或方法在类加载的时候就进行了initialization

静态字段：static 修饰的字段属于类，由类名直接访问，不需要构造对象来访问

静态常量：

静态方法：

```java
public final class Math {
	...
	public static final double PI = 3.14159265358979323846;
	...
}
```

### method parameter

按值调用：call by value, 参数为基本数据类型

按引用调用该：call by reference，参数为对象引用

### object constructor

重载，默认字段初始化，无参数的构造器

```java
package basictype;

public class People {
	// 1. 默认初始化 null, 0, false
	private String name;

	// 2.显式字段初始化
	private int age = 0;

	private boolean isMale;

	// 3.利用初始化块初始化
	{
		isMale = true;
	}

	public People(){

	}

	// 4.利用构造器初始化
	public People(String name){
		this.name = name;
	}

	public People(String name, int age){
		// this调用另一个构造器
		this(name);
		this.age = age;
	}

	@Override
	public String toString() {
		return "People{" +
				"name='" + name + '\'' +
				", age=" + age +
				", isMale=" + isMale +
				'}';
	}

	public static void main(String[] args) {
		People people = new People();
		System.out.println(people);
		// People{name='null', age=0, isMale=true}

		People people2 = new People("Milo", 25);
		System.out.println(people2);
		// People{name='Milo', age=25, isMale=true}
	}
}
```

