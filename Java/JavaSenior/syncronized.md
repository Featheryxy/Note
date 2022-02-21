## 并发编程中的三个问题

### 可见性

可见性 Visibility：指一个线程对共享变量进行修改，另外的线程并没有立即看到修改后的最新值。

下列代码中，第一个线程并不会停止

```java
boolean flag = true;

new Thread(()->{
    while (flag) {
        
    }
}.start();
           
sleep(1000);
           
new Thread(()->{
	flag = false
}.start(); 
```

### 原子性

原子性 Atomicity：当一个线程对共享变量操作到一半时，另外的线程也有可能来操作共

享变量，干扰了前一个线程的操作



一条语句对应多个指令，并发时多线程可能交错进行

```java
int number=0
Runnable increment = () -> {
	for (int i=0; i<1000; i++){
		number++
	}
}

ArrayList<Thread> ts = new ArrayList<>();
for (int i = 0; i < 5; i++) {
    Thread t = new Thread(increment);
    t.start();
    ts.add(t);
}

for (Thread t : ts) {
    t.join();
}

System.out.println("number = " + number);
// 结果不一定是5000，可能小于5000

number++ 

getstatic #12
iconst_1
iadd
putstatic #12
```

### 有序性

有序性 Ordering：程序中代码的执行顺序，Java在编译时和运行时会对代码进行优化，会导致程序最终的执行顺序不一定就是我们编写代码时的顺序。

```java
@JCStressTest
@Outcome(id = {"1"， "4"}， expect = Expect.ACCEPTABLE， desc = "ok")
@Outcome(id = "0"， expect = Expect.ACCEPTABLE_INTERESTING， desc = "danger")
@State
public class Test03Orderliness {
    int num = 0;
    boolean ready = false;
    // 线程一执行的代码
    @Actor
    public void actor1(I_Result r) {
        if(ready) {
        	r.r1 = num + num;
        } else {
        	r.r1 = 1;
        }
    }
    // 线程2执行的代码
    @Actor
    public void actor2(I_Result r) {
        num = 2;
        ready = true;
    }
}
```

## Java内存模型(JMM)

### 缓存

CPU的运算速度和内存的访问速度相差比较大。这就导致CPU每次操作内存都要耗费很多等待时间。内存的读写速度成为了计算机运行的瓶颈。于是就有了在CPU和主内存之间增加缓存的设计。最靠近CPU的缓存称为L1，然后依次是 L2，L3和主内存

CPU Cache分成了三个级别: L1， L2， L3。级别越小越接近CPU，速度也更快，同时也代表着容量越
小。
1. L1是最接近CPU的，它容量最小，例如32K，速度最快，每个核上都有一个L1 Cache。
2. L2 Cache 更大一些，例如256K，速度要慢一些，一般情况下每个核上都有一个独立的L2 Cache。
3. L3 Cache是三级缓存中最大的一级，例如12MB，同时也是缓存中最慢的一级，在同一个CPU插槽之间的核共享一个L3 Cache。



程序在运行的过程中，CPU接收到指令后，它会最先向CPU中的一级缓存（L1 Cache）去寻找相关的数据，如果命中缓存，CPU进行计算时就可以直接对CPU Cache中的数据进行读取和写人，当运算结束之后，再将CPUCache中的最新数据刷新
到主内存当中，CPU通过直接访问Cache的方式替代直接访问主存的方式极大地提高了CPU 的吞吐能力。但是由于一级缓存（L1 Cache）容量较小，所以不可能每次都命中。这时CPU会继续向下一级的二级缓存（L2 Cache）寻找，同样的道理，当所需要的数据在二级缓存中也没有的话，会继续转向L3Cache、内存(主存)和硬盘。

### Java内存模型

Java Memory Molde (Java内存模型/JMM)，和Java内存结构（堆栈）不同

Java内存模型，是Java虚拟机规范中所定义的一种内存模型，Java内存模型是标准化的，屏蔽掉了底层不同计算机的区别。
Java内存模型是一套规范，描述了Java程序中各种变量(线程共享变量)的访问规，以及在JVM中将变量存储到内存和从内存中读取变量这样的底层细节，具体如下

- 主内存
  主内存是所有线程都共享的，都能访问的。所有的共享变量都存储于主内存。
- 工作内存
  每一个线程有自己的工作内存，工作内存只存储该线程对共享变量的副本。线程对变量的所有的操作(读，取)都必须在工作内存中完成，而不能直接读写主内存中的变量，不同线程之间也不能直接访问对方工作内存中的变量。

### Java内存模型与硬件内存

Java内存模型是硬件内存的上一层抽象

> Java内存模型和硬件内存架构并不完全一致。对于硬件内存来说只有寄存器、缓存内存、主内存的概念，并没有工作内存和主内存之分，也就是说Java内存模型对内存的划分对硬件内存并没有任何影响，因为JMM只是一种抽象的概念，是一组规则，不管是工作内存的数据还是主内存的数据，对于计算机硬件来说都会存储在计算机主内存中，当然也有可能存储到CPU缓存或者寄存器中，因此总体上来说，Java内存模型和计算机硬件内存架构是一个相互交叉的关系，是一种抽象概念划分与真实物理硬件的交
> 叉。

### Java内存模型数据交互

Java内存模型中定义了以下8种操作来完成，主内存与工作内存之间具体的交互协议，即一个变量如何从主内存拷贝到工作内存、如何从工作内存同步回主内存之类的实现细节，虚拟机实现时必须保证下面提及的每一种操作都是原子的、不可再分的。

```
lock --> read --> load --> use --> assign --> store --> write -- unlock
```



1. 如果对一个变量执行lock操作，将会清空工作内存中此变量的值
2. 对一个变量执行unlock操作之前，必须先把此变量同步到主内存

## synchronized保证三大特性

synchronized能够保证在同一时刻最多只有一个线程执行该段代码，以达到保证并发安全的效果

1. synchronized保证只有一个线程拿到锁，能够进入同步代码块。
2. 执行synchronized时，会对应lock原子操作会刷新工作内存中共享变量的值
3. 加synchronized后，依然会发生重排序，只不过，我们有同步代码块，可以保证只有一个线程执行同步代码中的代码。保证有序性

## synchronized特性

### 可重入特性

```java
synchronized (Demo01.class) {
    System.out.println("我是run"); // 该方法内部也有synchronized
    test01();
}
```

原理：synchronized的锁对象中有一个计数器（recursions变量）会记录线程获得几次锁

优点：

1. 可以避免死锁

2.可以让我们更好的来封装代码

小结：synchronized是可重入锁，内部锁对象中会有一个计数器记录线程获取几次锁啦，在执行完同步代码块时，计数器的数量会-1，知道计数器的数量为0，就释放这个锁。

### 不可中断性

不可中断：一个线程获得锁后，另一个线程想要获得锁，必须处于阻塞或等待状态，如果第一个线程不释放锁，第二个线程会一直阻塞或等待，不可被中断。

> 打断线程的阻塞或等待？

```java
/*
目标:演示synchronized不可中断
1.定义一个Runnable
2.在Runnable定义同步代码块
3.先开启一个线程来执行同步代码块,保证不退出同步代码块
4.后开启一个线程来执行同步代码块(阻塞状态)
5.停止第二个线程
*/
public class Demo02_Uninterruptible {
    private static Object obj = new Object();
    public static void main(String[] args) throws InterruptedException {
        // 1.定义一个Runnable
        Runnable run = () -> {
            // 2.在Runnable定义同步代码块
            synchronized (obj) {
                String name = Thread.currentThread().getName();
                System.out.println(name + "进入同步代码块");
                // 保证不退出同步代码块
                try {
                	Thread.sleep(888888);
                } catch (InterruptedException e) {
                	e.printStackTrace();
                }
            }
        };
        
        // 3.先开启一个线程来执行同步代码块
        Thread t1 = new Thread(run);
        t1.start();
        Thread.sleep(1000);
        
        // 4.后开启一个线程来执行同步代码块(阻塞状态)
        Thread t2 = new Thread(run);
        t2.start();
        
        // 5.停止第二个线程
        System.out.println("停止线程前");
        t2.interrupt();
        System.out.println("停止线程后");
        System.out.println(t1.getState()); // TIMED_WAITING
        System.out.println(t2.getState()); // BLOCKED
    }
}
```

### ReentrantLock可中断

```java
package cn.itcast.test;

import lombok.extern.slf4j.Slf4j;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

@Slf4j
public class Test {
	private static Lock lock = new ReentrantLock();
	public static void main(String[] args) throws InterruptedException {
		 test01();
//		test02();
	}
	// 演示Lock可中断
	public static void test02() throws InterruptedException {
		Runnable run = () -> {
			String name = Thread.currentThread().getName();
			boolean b = false;
			try {
				b = lock.tryLock(3, TimeUnit.SECONDS);
				if (b) {
					System.out.println(name + "获得锁,进入锁执行");
					Thread.sleep(88888);
				} else {
					System.out.println(name + "在指定时间没有得到锁做其他操作");
				}
			} catch (InterruptedException e) {
				e.printStackTrace();
			} finally {
				if (b) {
					lock.unlock();
					System.out.println(name + "释放锁");
				}
			}
		};
		Thread t1 = new Thread(run);
		t1.start();
		Thread.sleep(1000);
		Thread t2 = new Thread(run);
		t2.start();
		// Thread-0获得锁,进入锁执行
		//Thread-1在指定时间没有得到锁做其他操作
	}

	// 演示Lock不可中断
	public static void test01() throws InterruptedException {
		Runnable run = () -> {
			String name = Thread.currentThread().getName();
			try {
				lock.lock();
				System.out.println(name + "获得锁,进入锁执行");
				Thread.sleep(88888);
			} catch (InterruptedException e) {
				e.printStackTrace();
			} finally {
				lock.unlock();
				System.out.println(name + "释放锁");
			}
		};
		Thread t1 = new Thread(run);
		t1.start();
		Thread.sleep(1000);
		Thread t2 = new Thread(run);
		t2.start();
		Thread.sleep(1000);
		System.out.println("t2"+t2.getState());
		System.out.println("停止t2线程前");
		t2.interrupt();
		System.out.println("停止t2线程后");
		Thread.sleep(1000);
		System.out.println(t1.getState());
		System.out.println(t2.getState());
		/*
			t2WAITING
			停止t2线程前
			停止t2线程后
			TIMED_WAITING
			WAITING
		 */
	}
}

```

小结

不可中断是指，当一个线程获得锁后，另一个线程一直处于阻塞或等待状态，前一个线程不释放锁，后一个线程会一直阻塞或等待，不可被中断。
synchronized属于不可被中断
Lock的lock方法是不可中断的
Lock的tryLock方法是可中断的

## synchronized原理

```java
public class Demo01 {
    private static Object obj = new Object();
    public static void main(String[] args) {
        synchronized (obj) {
            System.out.println("1");
        }
    }
    
    public synchronized void test() {
        System.out.println("a");
    }
}
```

反编译得`javap -p -v -c xxx.class`

```java
public static void main(java.lang.String[]);
descriptor: ([Ljava/lang/String;)V
flags: ACC_PUBLIC, ACC_STATIC
Code:
stack=2, locals=4, args_size=1
0: iconst_0
1: istore_1
2: getstatic #2 // Field obj:Ljava/lang/Object;
5: dup
6: astore_2
7: monitorenter
8: iinc 1, 1
11: aload_2
12: monitorexit
13: goto 21
16: astore_3
17: aload_2
18: monitorexit
19: aload_3
20: athrow
21: return
Exception table:
from to target type
8 13 16 any
16 19 16 any
LineNumberTable:
line 8: 0
line 9: 2
line 10: 8
line 11: 11
line 12: 21
LocalVariableTable:
Start Length Slot Name Signature
monitorenter
首先我们来看一下JVM规范中对于monitorenter的描述：
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-6.html#jvms-6.5.monitorenter
Each object is associated with a monitor. A monitor is locked if and only if it has an owner.
The thread that executes monitorenter attempts to gain ownership of the monitor
associated with objectref， as follows: • If the entry count of the monitor associated with
objectref is zero， the thread enters the monitor and sets its entry count to one. The thread
is then the owner of the monitor. • If the thread already owns the monitor associated with
objectref， it reenters the monitor， incrementing its entry count. • If another thread
0 22 0 args [Ljava/lang/String;
2 20 1 number I
StackMapTable: number_of_entries = 2
frame_type = 255 /* full_frame */
offset_delta = 16
locals = [ class "[Ljava/lang/String;", int, class java/lang/Object ]
stack = [ class java/lang/Throwable ]
frame_type = 250 /* chop */
offset_delta = 4
public synchronized void test();
descriptor: ()V
flags: ACC_PUBLIC, ACC_SYNCHRONIZED
Code:
stack=2, locals=1, args_size=1
0: getstatic #3 // Field
java/lang/System.out:Ljava/io/PrintStream;
3: ldc #4 // String a
5: invokevirtual #5 // Method
java/io/PrintStream.println:(Ljava/lang/String;)V
8: return
LineNumberTable:
line 15: 0
line 16: 8
LocalVariableTable:
Start Length Slot Name Signature
0 9 0 this
Lcom/itheima/demo04_synchronized_monitor/Demo01
```

```
synchronized 编译成字节码后

monitorenter

代码逻辑

monitorexit
```

### monitorenter

https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-6.html#jvms-6.5.monitorenter
 每一个对象都会和一个监视器monitor关联。监视器被占用时会被锁住，其他线程无法来获
取该monitor。 当JVM执行某个线程的某个方法内部的monitorenter时，它会尝试去获取当前对象对应
的monitor的所有权。其过程如下：
1. 若monior的进入数为0，线程可以进入monitor，并将monitor的进入数置为1。当前线程成为monitor的owner（所有者）
2. 若线程已拥有monitor的所有权，允许它重入monitor，则进入monitor的进入数加1
3. 若其他线程已经占有monitor的所有权，那么当前尝试获取monitor的所有权的线程会被阻塞，直到monitor的进入数变为0，才能重新尝试获取monitor的所有权。



monitorenter小结:
synchronized的锁对象会关联一个monitor,这个monitor不是我们主动创建的,是JVM的线程执行到这个同步代码块,发现锁对象没有monitor就会创建monitor,monitor内部有两个重要的成员变量owner:拥有这把锁的线程,recursions会记录线程拥有锁的次数,当一个线程拥有monitor后其他线程只能等待

### monitorexit

1. 能执行monitorexit指令的线程一定是拥有当前对象的monitor的所有权的线程。

2. 执行monitorexit时会将monitor的进入数减1。当monitor的进入数减为0时，当前线程退出monitor，不再拥有monitor的所有权，此时其他被这个monitor阻塞的线程可以尝试去获取这个monitor的所有权



monitorexit释放锁。
monitorexit插入在方法结束处和异常处，JVM保证每个monitorenter必须有对应的monitorexit。

```java
    7: monitorenter
    8: iinc 1, 1
    11: aload_2
    12: monitorexit
    13: goto 21
    16: astore_3
    17: aload_2
    18: monitorexit // 根据Exception table，当发生异常时会执行monitorexit释放锁
    19: aload_3
    20: athrow
    21: return
        
Exception table:
from to target type
8 13 16 any
```



面试题synchroznied出现异常会释放锁吗?
会释放锁

### 同步方法

可以看到同步方法在反汇编后，会增加 ACC_SYNCHRONIZED 修饰。会隐式调用monitorenter和monitorexit。在执行同步方法前会调用monitorenter，在执行完同步方法后会调用monitorexit。

```java
public synchronized void test();
    descriptor: ()V
    flags: ACC_PUBLIC, ACC_SYNCHRONIZED
    Code:
    stack=2, locals=1, args_size=1
    0: getstatic #3 // Field
    java/lang/System.out:Ljava/io/PrintStream;
    3: ldc #4 // String a
    5: invokevirtual #5 // Method
    java/io/PrintStream.println:(Ljava/lang/String;)V
    8: return
LineNumberTable:
    line 15: 0
    line 16: 8
LocalVariableTable:
    Start Length Slot Name Signature
    0 9 0 this
```

### synchronized与Lock的区别

1. synchronized是关键字，而Lock是一个接口。
2. synchronized会自动释放锁，而Lock必须手动释放锁。
3. synchronized是不可中断的，Lock可以中断也可以不中断。
4. 通过Lock可以知道线程有没有拿到锁，而synchronized不能。
5. synchronized能锁住方法和代码块，而Lock只能锁住代码块。
6. Lock可以使用读锁提高多线程读效率。
7. synchronized是非公平锁，ReentrantLock可以控制是否是公平锁。

## 源码分析

http://openjdk.java.net/ --> Mercurial --> jdk8 --> hotspot --> zip

在HotSpot虚拟机中，monitor是由ObjectMonitor实现的。其源码是用c++来实现的，位于HotSpot虚拟机源码ObjectMonitor.hpp文件中(src/share/vm/runtime/objectMonitor.hpp)。ObjectMonitor主要数据结构如下：

```c++
ObjectMonitor() {
    _header = NULL;
    _count = 0;
    _waiters = 0，
    _recursions = 0; // 线程的重入次数
    _object = NULL; // 存储该monitor的对象
    _owner = NULL; // 标识拥有该monitor的线程
    _WaitSet = NULL; // 处于wait状态的线程，会被加入到_WaitSet
    _WaitSetLock = 0 ;
    _Responsible = NULL;
    _succ = NULL;
    _cxq = NULL; // 多线程竞争锁时的单向列表
    FreeNext = NULL;
    _EntryList = NULL; // 处于等待锁block状态的线程，会被加入到该列表
    _SpinFreq = 0;
    _SpinClock = 0;
    OwnerIsThread = 0;
}
```

1. _owner：初始时为NULL。当有线程占有该monitor时，owner标记为该线程的唯一标识。当线程释放monitor时，owner又恢复为NULL。owner是一个临界资源，JVM是通过CAS操作来保证其线程安全的。
2. \_cxq：竞争队列，所有请求锁的线程首先会被放在这个队列中（单向链接）。_cxq是一个临界资
源，JVM通过CAS原子指令来修改_cxq队列。修改前_cxq的旧值填入了node的next字段，_cxq指
向新值（新线程）。因此_cxq是一个后进先出的stack（栈）。
3. \_EntryList：_cxq队列中有资格成为候选资源的线程会被移动到该队列中。
4. _WaitSet：因为调用wait方法而被阻塞的线程会被放在该队列中。



每一个Java对象都可以与一个监视器monitor关联，我们可以把它理解成为一把锁，当一个线程想要执行一段被synchronized圈起来的同步方法或者代码块时，该线程得先获取到synchronized修饰的对象对应的monitor。
我们的Java代码里不会显示地去创造这么一个monitor对象，我们也无需创建，事实上可以这么理解：monitor并不是随着对象创建而创建的。我们是通过synchronized修饰符告诉JVM需要为我们的某个对象创建关联的monitor对象。每个线程都存在两个ObjectMonitor对象列表，分别为free和used列表。
同时JVM中也维护着global locklist。当线程需要ObjectMonitor对象时，首先从线程自身的free表中申请，若存在则使用，若不存在则从global list中申请。
ObjectMonitor的数据结构中包含：_owner、_WaitSet和_EntryList，它们之间的关系转换可以用下表示：

_owner: 竞争到锁的线程

WaitSet：处于等待状态的线程

_EntryList：处于阻塞状态的线程