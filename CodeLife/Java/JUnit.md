---
title: 初探JUnit
date: 2020-10-18 11:13:32
tags: 
categories: Java
---

JUnit是一个开源的Java语言的单元测试框架

<!-- more -->

## 1 简介

### 什么是单元测试

- 测试是针对最小的功能单元编写测试代码
- Java程序最小的功能单元是方法
- 单元测试就是针对单个Java方法的测试

### maven gav

```xml
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.8.2</version>
        </dependency>
```



### JUnit是一个开源的Java语言的单元测试框架

- 门针对Java语言设计，使用最广泛·
- JUnit是事实上的标准单元测试框架
- 使用断言（Assertion）测试期望结果
- 可以方便地组织和运行测试
- 可以方便地查看测试结果
- 常用IDE（例如Eclipse）都集成了JUnit
- 可以方便地集成到Maven

### JUnit的设计

- TestCase：一个TestCase表示一个测试
- TestSuite：一个TestSuite包含一组TestCase，表示一组测试
- TestFixture：一个TestFixture表示一个测试环境
- TestResult：用于收集测试结果
- TestRunner：用于运行测试
- TestListener：用于监听测试过程，收集测试数据
- Assert：用于断言测试结果是否正确

## 2 Assert

### 使用Assert断言

- 相等：assertEquals（100，x）
- 断言数组相等：assertArrayEquals（{1，2，3}，x）
- 浮点数断言相等：assertEquals（3.1416，x，0.0001）
- 断言为nul:assertNull（x）
- 断言为true/false:assertTrue（x>0）assertFalse（x<0）
- 其他：assertNotEquals/assertNotNull

```java
package sample;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;

public class Calculator {
    public int calculate(String expression){
        // ?、+这些字符本身有逻辑含义，想表达这些字符的字面值就需要转义，即变成\?、\+
        // 为了保证送到正则编译器的表达式是上述字面值，代码中的字符串中必须存在\，对这个\转义需要另一个\
        String[] ss = expression.split("\\+");
        System.out.println(expression + " => " + Arrays.toString(ss));
        int sum = 0;
        for(String s : ss){
            sum = sum + Integer.parseInt(s);
        }
        return sum;
    }

    @Test
    public void test(){
        assertEquals(6, new Calculator().calculate("1+2"));
        assertEquals(3, new Calculator().calculate("1+2"));
    }

    @Test
    public void test1(){
        assertEquals(3, new Calculator().calculate(" 1+2"));
    }

//    public static void main(String[] args) {
//        Calculator calculator = new Calculator();
//        int r = calculator.calculate("1+2+3");
//        System.out.println(r);
//    }
}
```

### 同一个单元测试内的多个测试方法

- 测试前都需要初始化某些对象，在@Before 方法中初始化测试资源
- 测试后可能需要清理资源 filelnputStream.close()，在@After方法中释放测试资源

JUnit对于每个@Test方法：

1. 实例化Calculator Test
2. 执行@Before方法
3. 执行@Test方法
4. 执行@After方法

## 3 @Before和@After

### 使用@Before和@After

- 单个@Test方法执行前会创建新的XxxTest实例，实例变量的状态不会传递给下一个@Test方法
- 单个@Test方法执行前后会执行@Before和@Atfter方法

### @BeforeClass和@AfterClass

@BeforeClass和@AfterClass静态方法：

1. 在执行所有@Test方法前执行@BeforeClass静态方法
2. 执行所有测试
3. 在执行所有@Test方法后执行@AfterClass静态方法

@BeforeClass和@AfterClass静态方法：

- @BeforeClass静态方法初始化的对象只能存放在静态字段中
- 静态字段的状态会影响到所有@Test

### 资源

初始化测试资源称为Fixture

- @Before：初始化测试对象，例如：input=new FilelnputStream（）；
- @After：销毁@Before创建的测试对象，例如：input.close（）；
- @BeforeClass：初始化非常耗时的资源，例如：创建数据库
- @AfterClass：清理@BeforeClass创建的资源，例如：删除数据库

```java
package sample;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalculatorTest {

    Calculator calc;

    @Before
    public void setUp(){
        calc = new Calculator();
    }

    @Test
    public void test(){
        int r = calc.calculate("1+2");
        assertEquals(3, r);
    }
    @Test
    public void test1(){
        int r = calc.calculate("1+2+3");
        assertEquals(6, r);
    }
}
```

### JUnit执行逻辑

```java
invokeBeforeClass(CalculatorTest.class); // @BeforeClass
for(Method testMethod : finTestMethods(CalculatorTest.class)){
    CalculatorTest test = new CalculatorTest(); // new 
    test.setUp(); // @Before
    testMethod.invoke(test); // @Test
    test.tearDown(); // @After
}
invokeAfterClass(CalculatorTest.class); // @AfterClass
```

```java
package sample;

import org.junit.*;

public class SequenceTest {
    @BeforeClass
    public static void setUpBeforeClass() throws Exception{
        System.out.println("setUpBeforeClass()");
    }

    @AfterClass
    public static void tearDownAfterClass() throws Exception{
        System.out.println("tearDownAfterClass()");
    }

    @Before
    public void setUp() throws Exception{
        System.out.println("    setUp()");
    }

    @After
    public void tearDown() throws Exception{
        System.out.println("   tearDown()");
    }

    // 构造函数
    public SequenceTest(){
        System.out.println("new SequenceTest()");
    }

    @Test
    public void testA(){
        System.out.println("    testA()");
    }

    @Test
    public void testB(){
        System.out.println("    testB()");
    }

    @Test
    public void testC(){
        System.out.println("    testC()");
    }
    
    /*
    setUpBeforeClass()
    new SequenceTest()
        setUp()
        testA()
       tearDown()
    new SequenceTest()
        setUp()
        testB()
       tearDown()
    new SequenceTest()
        setUp()
        testC()
       tearDown()
    tearDownAfterClass()
     */
}

```

### 总结

- 理解JUnit执行测试的生命周期
- @Before用于初始化测试对象，测试对象以实例变量存放
- @After用于清理@Before创建的对象
- @BeforeClass用于初始化耗时资源，以静态变量存放
- @AfterClass用于清理@BeforeClass创建的资源

## 4 异常处理

```java
@Test(expected = NumberFormatException.class)
public void test3(){
    calc.calculate("");
}
//  => []

@Test(expected = NumberFormatException.class)
public void test3() {
    calc.calculate(null);
}
//    java.lang.Exception: Unexpected exception, expected<java.lang.NumberFormatException> but was<java.lang.NullPointerException>
```

### 总结

- 测试异常可以使用@Test（expected=Exception.class）
- 对可能发生的每种类型的异常进行测试

## 5 参数化测试

如果待测试的输入和输出是一组数据：

- 可以把测试数据组织起来
- 用不同的测试数据调用相同的测试方法



##  Reference

https://www.cnblogs.com/niunotniu/p/14671941.html