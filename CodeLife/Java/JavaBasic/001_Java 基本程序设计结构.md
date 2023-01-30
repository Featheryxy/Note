# Java 基本程序设计结构

### 简介

JRE = JVM + Java SE标准类库

JDK = JRE + 开发工具集（例如Javac编译工具等）

大小写敏感

变量的声明尽可能靠近第一次使用的地方

### 命名规范

包名：多单词组成时所有字母都小写： xxxyyyzzz

类名、接口名：多单词组成时，所有单词的首字母大写： XxxYyyZzz

变量名、方法名：多单词组成时，第一个单词首字母小写，第二个单词开始每个单词首字母大写： xxxYyyZzz

常量名：所有字母都大写。多单词时每个单词用下划线连接： XXX_YYY_ZZZ

### 注释

```java
// 单行

/*
多行
*/

/**
文档注释
*/
```

### 基本数据类型

基本类型（数值，字符，布尔）不是对象，

byte   1字节   8位  [-128~127]   127+128+1=256 = 2^8

short  2字节

int      4字节

long   8字节

float    4字节

double 8字节

char      2字节  Unicode编码  \u0000-\uFFFF

boolean 1字节 true, false

```java
		byte a = 1;
		short b = 2;
		int c = 3;
		long d1 = 4l;
		long d2 = 4L;
		float e1 = 5f;
		float e2 = 5F;
		double f1 = 5;
		double f2 =5d;
		char g = 'g';
		String s = "G";
```

### 字符串

1. Java字符串就是Unicode字符序列
2. 使用+拼接字符串，任何基本数据类型的值和字符串(String)进行连接运算时(+)， 基本数据类型的值将自动转化为字符串(String)类型
3. 字符串不可变，但是可以使字符串变量引用一个新的字符串
4. 空串与Null串

```java
		String blankStr = "";
		if (blankStr.length()==0){
			System.out.println("空串");
		}
		if (blankStr.equals("")){
			System.out.println("空串");
		}

		String nullStr = null;
		if (nullStr==null){
			System.out.println("Null串");
		}

		String str = "not null and blank";
		if (str!=null && str.length()!=0){
			System.out.println("既不是Null串也不是空串");
		}
```

### StringBuilder

```java
		StringBuilder stringBuilder = new StringBuilder();
		stringBuilder.append("Hello ");
		stringBuilder.append("World");
		stringBuilder.append('!');
		System.out.println(stringBuilder);
		// Hello World!
```

### 变量与常量

变量大小写敏感

变量的声明尽可能靠近第一次使用的地方

```java
int AgeOfMine = 1;

final int YEAR = 2021; 
static final int YEAR = 2021;  // 可以在一个类的多个方法中使用

```

### 运算符

```
1. 算术运算符： +,-,*,/,%
3/2 = 1
3/2.0 = 1.5
3%2 = 1

2. 关系运算符：<, >, <=, >=, ==, !=

3. 逻辑运算符：&&, ||, 

expression1 && expression2
if expression1 equal to false, expression2 will be not execute.

expression1 || expression2
if expression1 equal to true, expression2 will be not execute.

condition? expression1 : expression2

4. 位运算符
&(and), |(or), ^(xor), ~(not)
>> 右移，高位用0填充
<< 左移，低位用0填充
```

### 数值类型转换

无信息丢失转换

byte —> short —>int —>long

                              —>double

char—> int

### 流程控制

```java
if (condition) statement;

if (condition) statement1 else statement2;

if ... else if ...

switch(choice){
	case 1:
		...
	  break;
	case 2:
		...
	  break;
	default:
		...
		break;
}
// 如果case分支没有break语句，继续执行下个case语句
// case 标签可以为 char, byte, short, int的常量表达式，字符串字面量，枚举常量

while(condition) statement

do statement while(condition)

for(condition) statement

for(variable: collection) statement
```

### label

```java
label:
{
	...
	if (condition) break|continue label;
	...
}
```

### 数组

```java
// 动态初始化
int[] a = new int[3]; // 已完成默认初始化，a = {0,0,0}
a[1] = 1;

int a [] = new int[3];

// 静态初始化
int[] arr1 = {1, 2, 3};
int[] arr2= new int[]{ 3, 9, 8};

int a [] = {1, 2, 3};
```
