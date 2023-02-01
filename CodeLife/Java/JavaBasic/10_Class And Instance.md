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

当类中没有显式调用构造器时，会使用默认的无参构造器，否则使用显式的构造器

### extends

继承：基于已有的类创建新的类。i.e.：子类继承父类的所有属性和方法，并且可以重写父类的方法或增加自己的方法。

重写：同名同参（参数数量，参数类型，参数顺序）

- 若子类重写了父类方法，就意味着子类里定义的方法彻底覆盖了父类里的同名方法，系统将不可能把父类里的方法转移到子类中。
- 对于实例变量则不存在这样的现象，即使子类里定义了与父类完全相同的实例变量，这个实例变量依然不可能覆盖父类中定义的实例变量

子类重写的方法的返回值类型不能大于父类被重写的方法的返回值类型

子类重写的方法使用的访问权限不能小于父类被重写的方法的访问权限

子类不能重写父类中声明为private权限的方法

子类与父类中同名同参数的方法必须同时声明为非static的(即为重写)，或者同时声明为static的（不是重写） 。因为static方法是属于类的，子类无法覆盖父类的方法

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

### this 

this

1. 它在方法内部使用，即这个方法所属对象的引用
2. 它在构造器内部使用，调用该类的**其他构造器**

```java
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

### super

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

Java引用变量有两个类型： 编译时类型和运行时类型。

编译时， 看左边；运行时， 看右边

多态情况下，

“看左边” ： 看的是父类的引用（父类中不具备子类特有的方法）
“看右边” ： 看的是子类的对象（实际运行的是子类重写父类的方法）

对象的多态 —在Java中,子类的对象可以替代父类的对象使用

- 一个变量只能有一种确定的数据类型
- 一个引用类型变量可能指向(引用)多种不同类型的对象

子类可看做是特殊的父类， 所以父类类型的引用可以指向子类的对象：向上转型(upcasting)

一个引用类型变量如果声明为父类的类型，但实际引用的是子类对象，那么该变量就不能再访问子类中添加的属性和方法

### 类型转换

向上转型是自动的，如 int 自动向上转型为 float

向下转型需要强制类型转换

对Java对象的强制类型转换称为造型

- 从子类到父类的类型转换可以自动进行
- 从父类到子类的类型转换必须通过造型(强制类型转换)实现
- 无继承关系的引用类型间的转换是非法的
- 在造型前可以使用instanceof操作符测试一个对象的类型

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

static修饰的成员：static 修饰的字段属于类，由类名直接访问，不需要构造对象来访问，被所有对象所共享 (共享一块内存)

```java
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

