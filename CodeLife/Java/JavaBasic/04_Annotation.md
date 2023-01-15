# Annontation

注解可以类比于标签，

注解是一系列元数据，用来解释程序代码，但是并非是代码本身的一部分，对于代码的运行效果没有直接影响。

使用@interface来定义，有属性值，可以使用default来指定默认值。

有5种元注解@Retention，@Target, @Documented, @Inherited, @Repeatable  

```java
public @interface TestAnnotation {
}
```

有5种元注解，分别是

@Retention：Retention 的英文意为保留期的意思。它解释说明了这个注解的的存活时间。 

- RetentionPolicy.SOURCE 注解只在源码阶段保留，在编译器进行编译时它将被丢弃忽视。
- RetentionPolicy.CLASS 注解只被保留到编译进行的时候，它并不会被加载到 JVM 中。
- RetentionPolicy.RUNTIME 注解可以保留到程序运行的时候，它会被加载进入到 JVM 中，所以在程序运行时可以获取到它们。

@Documented：将注解中的元素包含到 Javadoc 中 

@Target：指定了注解运用的地方 

- ElementType.ANNOTATION_TYPE 可以给一个注解进行注解
- ElementType.CONSTRUCTOR 可以给构造方法进行注解
- ElementType.FIELD 可以给属性进行注解
- ElementType.LOCAL_VARIABLE 可以给局部变量进行注解
- ElementType.METHOD 可以给方法进行注解
- ElementType.PACKAGE 可以给一个包进行注解
- ElementType.PARAMETER 可以给一个方法内的参数进行注解
- ElementType.TYPE 可以给一个类型进行注解，比如类、接口、枚举

@Inherited：注解 Test 被 @Inherited 修饰，之后类 A 被 Test 注解，类 B 继承 A,类 B 也拥有 Test 这个注解。 

```
@Inherited
@Retention(RetentionPolicy.RUNTIME)
@interface Test {}
@Test
public class A {}
public class B extends A {}
```

@Repeatable  :注解的值可以同时取多个 

一个人他既是程序员又是产品经理,同时他还是个画家。 

```
@interface Persons {
    Person[]  value();
}
@Repeatable(Persons.class)
@interface Person{
    String role default "";
}
@Person(role="artist")
@Person(role="coder")
@Person(role="PM")
public class SuperMan{
}
```

注解的属性：注解的属性也叫做成员变量。注解只有成员变量，没有方法 。注解的成员变量在注解的定义中以“无形参的方法”形式来声明 ,可以用 default 关键值指定默认值

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface TestAnnotation {
    public int id() default -1;
    String msg();
}

@TestAnnotation(id=3,msg="hello annotation")
public class Test {
}
```



注解通过反射获取并使用，首先可以通过 Class 对象的 isAnnotationPresent() 方法判断它是否应用了某个注解 ，然后通过 getAnnotation() 方法来获取 Annotation 对象 

```java
// 判断是否应用了某个注解
public boolean isAnnotationPresent(Class<? extends Annotation> annotationClass) {}

public <A extends Annotation> A getAnnotation(Class<A> annotationClass) {}

public Annotation[] getAnnotations() {}
```

使用场景：

1. 检查
2. 



> 注解：注解是一系列元数据，它提供数据用来解释程序代码，但是注解并非是所解释的代码本身的一部分。注解对于代码的运行效果没有直接影响 
>
> 元注解：注解的注解，用注解修饰注解





## Reference

https://zhuanlan.zhihu.com/p/37701743

## 概述

- 从 JDK 5.0 开始, Java 增加了对元数据(MetaData) 的支持, 也就是Annotation(注解)  
- Annotation 其实就是代码里的特殊标记, 这些标记可以在**编译, 类加载, 运行时被读取**, **并执行相应的处理**。通过使用 Annotation, 程序员可以在不改变原有逻辑的情况下, 在源文件中嵌入一些补充信息。 代码分析工具、开发工具和部署工具可以通过这些补充信息进行验证或者进行部署。  
- Annotation 可以像修饰符一样被使用, 可用于**修饰包,类, 构造器, 方法, 成员变量, 参数, 局部变量的声明**, 这些信息被**保存在 Annotation的 “name=value” 对中**。  
- 框架 = 注解 + 反射 + 设计模式。  



## 注解分类

第一类是由编译器使用的注解，例如：

- `@Override`：让编译器检查该方法是否正确地实现了覆写；
- `@SuppressWarnings`：告诉编译器忽略此处代码产生的警告。

这类注解不会被编译进入`.class`文件，它们在编译后就被编译器扔掉了。

第二类是由工具处理`.class`文件使用的注解，比如有些工具会在加载class的时候，对class做动态修改，实现一些特殊的功能。这类注解会被编译进入`.class`文件，但加载结束后并不会存在于内存中。这类注解只被一些底层库使用，一般我们不必自己处理。

第三类是在程序运行期能够读取的注解，它们在加载后一直存在于JVM中，这也是最常用的注解。例如，一个配置了`@PostConstruct`的方法会在调用构造方法后自动被调用（这是Java代码读取该注解实现的功能，JVM并不会识别该注解）。



## 常见的Annotation示例

### 文档相关

@author 标明开发该类模块的作者， 多个作者之间使用,分割
@version 标明该类模块的版本
@see 参考转向， 也就是相关主题
@since 从哪个版本开始增加的
@param 对方法中某参数的说明， 如果没有参数就不能写
@return 对方法返回值的说明， 如果方法的返回值类型是void就不能写
@exception 对方法可能抛出的异常进行说明 ， 如果方法没有用throws显式抛出的异常就不能写
其中
	@param @return 和 @exception 这三个标记都是只用于方法的。
	@param的格式要求： @param 形参名 形参类型 形参说明
	@return 的格式要求： @return 返回值类型 返回值说明
	@exception的格式要求： @exception 异常类型 异常说明
	@param和@exception可以并列多个  

### 三个基本注解

@Override: 限定**重写父类方法**, 该注解只能用于方法
@Deprecated: 用于表示**所修饰的元素(类, 方法等)已过时**。通常是因为所修饰的结构危险或存在更好的选择
@SuppressWarnings: **抑制编译器**警告  

## 元注解

**元注解：修饰注解的注解**
**@Retention**：指定所修饰的 Annotation 的生命周期：SOURCE\CLASS（默认行为）\RUNTIME  只有声明为RUNTIME生命周期的注解，才能通过反射获取。

- 仅编译期使用, 编译后丢弃：`RetentionPolicy.SOURCE`；
- 保存在class文件, 不会加载到JVM：`RetentionPolicy.CLASS`；
- 运行期：`RetentionPolicy.RUNTIME`, 加载进JVM 。程序可以**通过反射获取该注释**。

**@Target**: 用于指定被修饰的 Annotation 用于哪些地方

- 类或接口：`ElementType.TYPE`；
- 字段：`ElementType.FIELD`；
- 方法：`ElementType.METHOD`；
- 构造方法：`ElementType.CONSTRUCTOR`；
- 方法参数：`ElementType.PARAMETER`。

*******出现的频率较低*******
**@Documented**: 表示所修饰的注解在被javadoc解析时，保留下来。

- 定义为Documented的注解必须设置Retention值为RUNTIME  

**@Inherited**: 被它修饰的 Annotation 将具有继承性。

- 如果把标有@Inherited注解的自定义的注解标注在类级别上，子类则可以继承父类类级别的注解  

## 自定义 Annotation

1. 注解声明为：@interface, 自动继承了java.lang.annotation.Annotation接口  
2. 内部定义成员，通常使用value表示
3. 可以指定成员的默认值，使用default定义
4. 如果自定义注解**没有成员**，表明是一个**标识作用**。

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface Report {
    int type() default 0;
    String level() default "info";
    String value() default "";
}
```

ps: 
   如果注解有成员，在使用注解时，需要指明成员的值。
   自定义注解必须配上注解的信息处理流程(使用反射)才有意义。
   自定义注解通过都会指明两个元注解：Retention、Target

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface Range {

	int min() default 0;

	int max() default 255;

}

public class Person {
	@Range(min = 1, max = 20)
	public String name;

	@Range(max = 10)
	public String city;

	@Range(min = 1, max = 100)
	public int age;

	public Person(String name, String city, int age) {
		this.name = name;
		this.city = city;
		this.age = age;
	}

	@Override
	public String toString() {
		return String.format("{Person: name=%s, city=%s, age=%d}", name, city, age);
	}
}

public class Main {

	public static void main(String[] args) throws Exception {

		Person p1 = new Person("Bob", "Beijing", 20);
		Person p2 = new Person("", "Shanghai", 20);
		Person p3 = new Person("Alice", "Shanghai", 199);
		for (Person p : new Person[] { p1, p2, p3 }) {
			try {
				check(p);
				System.out.println("Person " + p + " checked ok.");
			} catch (IllegalArgumentException e) {
				System.out.println("Person " + p + " checked failed: " + e);
			}
		}
		// Person {Person: name=Bob, city=Beijing, age=20} checked ok.
		// Person {Person: name=, city=Shanghai, age=20} checked failed: java.lang.IllegalArgumentException: Invalid field: name
		// Person {Person: name=Alice, city=Shanghai, age=199} checked failed: java.lang.IllegalArgumentException: Invalid field: age
	}

	static void check(Person person) throws IllegalArgumentException, ReflectiveOperationException {
		for (Field field : person.getClass().getFields()) {
			Range range = field.getAnnotation(Range.class);
			if (range != null) {
				Object value = field.get(person);
				if (value instanceof String) {
					String s = (String) value;
					// 判断值是否满足@Range的min/max:
					if (s.length() < range.min() || s.length() > range.max()) {
						throw new IllegalArgumentException("Invalid field: " + field.getName());
					}
				}
				if (value instanceof Integer) {
					Integer i = (Integer) value;
					// 判断值是否满足@Range的min/max:
					if (i < range.min() || i > range.max()) {
						throw new IllegalArgumentException("Invalid field: " + field.getName());
					}
				}
			}
		}
	}
}
```

##  JDK8中注解的新特性

### 5.1 可重复注解

1. 在MyAnnotation上声明@Repeatable，成员值为MyAnnotations.class
2. MyAnnotation的Target和Retention等元注解与MyAnnotations相同。



MyAnnotation

```java
@Inherited
@Repeatable(MyAnnotations.class)
@Retention(RetentionPolicy.RUNTIME)
@Target({TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE,TYPE_PARAMETER,TYPE_USE})
public @interface MyAnnotation {

    String value() default "hello";
}
```

MyAnnotations

```java
@Inherited
@Retention(RetentionPolicy.RUNTIME)
@Target({TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE})
public @interface MyAnnotations {

    MyAnnotation[] value();
}
```

```java
//jdk 8之前的写法：
//@MyAnnotations({@MyAnnotation(value="hi"),@MyAnnotation(value="hi")})
@MyAnnotation(value="hi")
@MyAnnotation(value="abc")
class Person{
    private String name;
    private int age;

    public Person() {
    }
    @MyAnnotation
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    @MyAnnotation
    public void walk(){
        System.out.println("人走路");
    }
    public void eat(){
        System.out.println("人吃饭");
    }
}
```

### 5.2 类型注解

- ElementType.TYPE_PARAMETER  表示该注解能写在**类型变量的声明语句**中（如：泛型声明）。
- ElementType.TYPE_USE  表示该注解**能写在使用类型的任何语句**中。

```java
@Inherited
@Repeatable(MyAnnotations.class)
@Retention(RetentionPolicy.RUNTIME)
@Target({TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE,TYPE_PARAMETER, TYPE_USE})
public @interface MyAnnotation {
    String value() default "hello";
}
```

```java
//           TYPE_PARAMETER,
class Generic<@MyAnnotation T>{
    public void show() throws @MyAnnotation RuntimeException{ // TYPE_USE

        ArrayList<@MyAnnotation String> list = new ArrayList<>(); // TYPE_USE

        int num = (@MyAnnotation int) 10L; // TYPE_USE
    }
}
```

