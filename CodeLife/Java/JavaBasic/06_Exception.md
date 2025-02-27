# 异常

异常主要用于处理程序中的不被期望的事件，其顶层父类为 Throwable，由此派生出 Error 和 Exception。

Error ：JVM本身的错误 ，不能通过代码处理。如： JVM系统内部错误、 资源耗尽等严重情况，StackOverflowError和OOM。

Exception ：可以被Java异常处理机制使用 

异常总体上可分为两类，非检查异常（unckecked exception）和检查异常（checked exception）。

- unckecked exception：Error 和 RuntimeException 以及他们的子类 
- checked exception：others

异常处理方式：

1. try…catch{1, m}…[finally ]， 
2. throws+ 异常类型：在方法签名上声明，将checked exception交给函数调用者caller处理，自己不处理

异常对象的生成

- 由虚拟机自动生成：程序运行过程中，虚拟机检测到程序发生了问题，如果在当前代码中没有找到相应的处理程序，就会在后台自动创建一个对应异常类的实例对象并抛出——自动抛出
- 由开发人员手动创建： Exception exception = new ClassCastException();——创建好的异常对象不抛出对程序没有任何影响，和创建一个普通对象一样

注意事项：

try块中一旦出现异常，不会执行异常抛出点后的代码，会生成一个对应异常类的对象，根据此对象的类型，去catch中进行匹配。如果一个方法内抛出异常， 该异常对象会被抛给调用者方法中处
理。 如果异常没有在调用者方法中处理， 它继续被抛给这个调用方法的上层方法。 这个过程将一直继续下去， 直到异常被处理。这一过程称为捕获(catch)异常。

如果一个异常回到main()方法， 并且main()也不处理， 则程序运行终止。

每一个catch块用于捕获并处理一个特定的异常，或者这异常类型的子类，Java7中可以将多个异常声明在一个catch中。

catch中的异常类型如果满足子父类关系，则要求子类一定声明在父类的上面。先抛具体的错误，再抛通用的错误。否则编译不通过错

不论在try代码块中是否发生了异常事件， catch语句是否执行， catch语句是否有异常， catch语句中是否有return，finally块中的语句都会被执行。

异常的链式调用：

将异常对象作为参数构造新的异常对象

```java
public class Throwable implements Serializable {
    private Throwable cause = this;
    public Throwable(String message, Throwable cause) {
        fillInStackTrace();
        detailMessage = message;
        this.cause = cause;
    }
     public Throwable(Throwable cause) {
        fillInStackTrace();
        detailMessage = (cause==null ? null : cause.toString());
        this.cause = cause;
    }
    //........
}
```

finally块和return：

一个函数的返回值总是指向同一个内存地址，如果一个函数中有多个返回值，则后执行的会覆盖之前执行的数据。

- finally中的return 会覆盖 try 或者catch中的返回值。
- finally中的return会抑制（消灭）前面try或者catch块中的异常
- finally中的异常会覆盖（消灭）前面try或者catch中的异常



异常处理策略：

1. resumption model of exception handling（恢复式异常处理模式 ） ：当异常被处理后，控制流会恢复到**异常抛出点**接着执行 
2. termination model of exception handling（终结式异常处理模式）：执行流恢复到处理了异常的**catch块后接着执行** 

建议：

1. 不要在fianlly中使用return和抛出异常
2. fianlly中仅用作与资源的释放
3. return写在函数的最后面，而不是try … catch … finally中 





方法不仅告诉编译器返回什么值，还要告诉编译器有可能发生什么错误。

```java
public FileInputStream(String name) throws FileNotFoundException {
        this(name != null ? new File(name) : null);
}

// 该声明表示这个构造器将根据给定的String参数产生一个FileInputStream对象，但也可能出错
// 而抛出一个FileNotFoundException 异常。如果出错，该构造器不会创建一个对象，而会抛出
// 异常，运行时系统就会搜索知道如何处理FileNotFoundException 对象的异常处理器
```

## Reference

https://zhuanlan.zhihu.com/p/37925008

## **概述**

异常：在Java语言中， 将**程序执行中**发生的不正常情况称为“异常” 。(开发过程中的语法错误和逻辑错误不是异常)

- 一个方法必须声明所有可能抛出的检查型异常。
- 子类覆盖超类的一个方法时，子类方法中声明的检查型异常不能比超类方法中声明的异常更通用。

异常事件分类：

顶层父类为 Throwable，派生出 Error 和 Exception

- Error： **Java虚拟机无法解决**的严重问题，无法通过代码解决。
- Exception: 其它因编程错误或偶然的外在因素导致的一般性问题， 可以**使用针对性的代码进行处理**。 例如：
    - 编译时异常：.java---javac--->.class
    - 运行时异常：.class -----java-------> 在内存中加载、运行类



```
    java.lang.Throwable
        |-----java.lang.Error(unchecked, 非检查型):一般不编写针对性的代码进行处理。
        |-----java.lang.Exception:可以进行异常的处理
            |------编译时异常(checked)
                    |-----IOException
                        |-----FileNotFoundException
                    |-----ClassNotFoundException
            |------运行时异常(unchecked,RuntimeException)
                    |-----NullPointerException
                    |-----ArrayIndexOutOfBoundsException
                    |-----ClassCastException
                    |-----NumberFormatException
                    |-----InputMismatchException
                    |-----ArithmeticException
```

异常的处理：抓抛模型

1. "抛"：程序在正常执行的过程中，一旦出现异常，就会在异常代码处生成一个对应异常类的对象。并将此对象抛出。一旦抛出对象以后，其后的代码就不再执行。
    - 关于异常对象的产生：① 系统自动生成的异常对象; ② 手动的生成一个异常对象，并抛出（throw）
2. "抓"：可以理解为异常的处理方式：① try-catch-finally 自己处理异常 ② throws 将异常传递给调用
3. 捕获那些你知道如何处理的异常，继续传播那些不知道如何处理的异常

## **try-catch**

```
/*
 * try{
 *      //可能出现异常的代码
 * }catch(异常类型1 变量名1){
 *      //处理异常的方式1
 * }catch(异常类型2 变量名2){
 *      //处理异常的方式2
 * }catch(异常类型3 变量名3){
 *      //处理异常的方式3
 * }
 * ....
 * finally{
 *      //一定会执行的代码
 * }
 *
 * 说明：
 * 1. finally是可选的。
 * 2. 使用try将可能出现异常代码包装起来，在执行过程中，一旦出现异常，就会生成一个对应异常类的对象，根据此对象的类型，去catch中进行匹配
 * 3. 一旦try中的异常对象匹配到某一个catch时，就进入catch中进行异常的处理。一旦处理完成，就跳出当前的try-catch结构（在没有写finally的情况）。
 * 4. catch中的异常类型如果没有子父类关系，则谁声明在上，谁声明在下无所谓。
 *    catch中的异常类型如果满足子父类关系，则要求子类一定声明在父类的上面。先抛具体的错误，  *    再抛通用的错误。否则，报错。否则，报错
 * 5. 常用的异常对象处理的方式： ① String  getMessage()    ② printStackTrace()
 * 6. 在try结构中声明的变量，再出了try结构以后，就不能再被调用
 * 7. try-catch-finally结构可以嵌套
 *
 * 体会1：使用try-catch-finally处理编译时异常，是得程序在编译时就不再报错，但是运行时仍可能报错。
 *     相当于我们使用try-catch-finally将一个编译时可能出现的异常，延迟到运行时出现。
 *
 * 体会2：开发中，由于运行时异常比较常见，所以我们通常就不针对运行时异常编写try-catch-finally了。
 *      针对于编译时异常，我们说一定要考虑异常的处理。
 */

@Test
    public void test1(){
        String str = "123";
        str = "abc";
        int num = 0;
        try{
            num = Integer.parseInt(str);
            System.out.println("hello-----1");
        }catch(NumberFormatException e){
//          System.out.println("出现数值转换异常了，不要着急....");
            //String getMessage():
//          System.out.println(e.getMessage());
            //printStackTrace():
            e.printStackTrace();
        }catch(NullPointerException e){
            System.out.println("出现空指针异常了，不要着急....");
        }catch(Exception e){
            System.out.println("出现异常了，不要着急....");
        }
        System.out.println(num);
        System.out.println("hello-----2");
    }
```

## **try-catch-finally**

- finally是可选的, 在抛出异常之前执行
- 多个catch块中只能执行一个
- **catch中的异常类型如果满足子父类关系, 父类一定在子类后面, 否则编译不通过**
- 如果没有子父类关系, 声明顺序无所谓
- 不管是否又异常捕获，finally子句中的代码都会执行。  try中有return语句，catch中有return语句等情况。
    - **在执行catch中的return语句前执行finally**
- 像数据库连接、输入输出流、网络编程Socket等资源，JVM是不能自动的回收的，我们需要自己手动的进行资源的释放。此时的资源释放，就需要声明在finally中。

```
    @Test
    public void testMethod(){
        int num = method();
        System.out.println(num);
        // 我一定会被执行
        // 3
    }

    public int method(){

        try{
            int[] arr = new int[10];
            System.out.println(arr[10]);
            return 1;
        }catch(ArrayIndexOutOfBoundsException e){
            e.printStackTrace();
            return 2;
        }finally{
            System.out.println("我一定会被执行");
            return 3;
        }
    }
```

## **throws + 异常类型**

- "throws + 异常类型"写在方法的声明处。指明此方法执行时，可能会抛出的异常类型。
    - 一旦当方法体执行时，出现异常，仍会在异常代码处生成一个异常类的对象，此对象满足throws后异常类型时，就会被抛出。**异常代码后续的代码，就不再执行！**
- 体会：try-catch-finally:真正的将异常给处理掉了。
    - throws的方式只是将异常抛给了方法的调用者。 并没有真正将异常处理掉。
- 开发中如何选择使用try-catch-finally 还是使用throws？
    - 如果父类中被重写的方法没有throws方式处理异常，则子类重写的方法也不能使用throws，意味着如果子类重写的方法中有异常，必须使用try-catch-finally方式处理。
    - 执行的方法a中，先后又调用了另外的几个方法，这几个方法是递进关系执行的。我们建议这几个方法使用throws的方式进行处理。而执行的方法a可以考虑使用try-catch-finally方式进行处理。

```
public static void main(String[] args){
        try{
            method2();
        }catch(IOException e){
            e.printStackTrace();
        }
//      method3();
    }

    public static void method3(){
        try {
            method2();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void method2() throws IOException{
        method1();
    }

    public static void method1() throws FileNotFoundException,IOException{
        File file = new File("hello1.txt");
        FileInputStream fis = new FileInputStream(file);

        int data = fis.read();
        while(data != -1){
            System.out.print((char)data);
            data = fis.read();
        }
        fis.close();
        System.out.println("hahaha!");
    }
```

## **手动抛出异常**

- `throw new RuntimeException(String message);`
- `throw new Exception(String message);`

```
public class StudentTest {

    public static void main(String[] args) {
        try {
            Student s = new Student();
            s.regist(-1001);
            System.out.println(s);
        } catch (Exception e) {
//          e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}

class Student{
    private int id;
    public void regist(int id) throws Exception {
        if(id > 0){
            this.id = id;
        }else{
//          System.out.println("您输入的数据非法！");
            //手动抛出异常对象
//          throw new RuntimeException("您输入的数据非法！");
//          throw new Exception("您输入的数据非法！");
            throw new MyException("不能输入负数");
            //错误的
//          throw new String("不能输入负数");
        }
    }

    @Override
    public String toString() {
        return "Student [id=" + id + "]";
    }
}
```

## **自定义异常**

按照国际惯例， 自定义的异常应该总是包含如下的构造函数： 

- 一个无参构造函数
- 一个带有String参数的构造函数，并传递给父类的构造函数。
- 一个带有String参数和Throwable参数，并都传递给父类构造函数
- 一个带有Throwable 参数的构造函数，并传递给父类的构造函数。

```java
package com.atguigu.java2;
/*
 * 如何自定义异常类？
 * 1. 继承于现有的异常结构：RuntimeException 、Exception
 * 2. 提供全局常量：serialVersionUID
 * 3. 提供重载的构造器
 *
 */
public class MyException extends Exception{

    static final long serialVersionUID = -7034897193246939L;

    public MyException(){

    }

    public MyException(String msg){
        super(msg);
    }
}
```

## **练习题**

```
public class ReturnExceptionDemo {
    static void methodA() {
        try {
            System.out.println("进入方法A");
            throw new RuntimeException("制造异常");
        } finally {
            System.out.println("用A方法的finally");
        }
    }

    static void methodB() {
        try {
            System.out.println("进入方法B");
            return;
        } finally {
            System.out.println("调用B方法的finally");
        }
    }

    public static void main(String[] args) {
        try {
            methodA();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        methodB();
    }
    /*
    进入方法A
    用A方法的finally
    制造异常
    进入方法B
    调用B方法的finally
     */
}
```

## **throw与throws**

- throw：生成异常对象
- throws：在方法签名中使用，向上一级抛出异常，用于处理异常