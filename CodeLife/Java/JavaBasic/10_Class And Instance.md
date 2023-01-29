# Class And Instance

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

## Package

### package name

包名：将一个**因特网域名的逆序**形式作为包名。考虑域名horstmann.com, 工程名为corejava，Employee为包下的类。则**完全限定名(fully qualified name)**为com.horstmann.com.Employee

### 类的导入

```java
import java.time.LocalDate;

public class packtest {
	public static void main(String[] args) {
		java.time.LocalDate today = java.time.LocalDate.now();
		// 等价于
		LocalDate.now();
	}
}
```

### 静态导入

```java
import static java.lang.Math.*;

public classpacktest {
	public static voidmain(String[] args) {
	      Math.pow(2,2);
				// 等价于
				pow(2,2);
	   }
}
```

