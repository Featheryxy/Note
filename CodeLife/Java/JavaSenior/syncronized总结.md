#### Java内存模型

- 主内存：所有线程共享， 共享变量存储在主内存中
- 工作内存：每一个线程有自己的工作内存，工作内存只存储该线程对共享变量的副本。线程对变量的所有的操作(读，取)都必须在工作内存中完成，而不能直接读写主内存中的变量，不同线程之间也不能直接访问对方工作内存中的变量。

#### 缓存一致性问题

由于Java内存模型分为工作内存和主内存, 所以带来了下属三个问题

如果所有线程都只是去读取主内存的数据,那么不会有任何问题. 但是如果有写的操作时, 就会有问题. 假设现在又两个线程A和B

A 去写, B去读, 没有问题

A去读, B 再去写, A读取不到B修改后的值, **可见性**

A, B 同时去写 

	1. 指令的交替运行，造成指令重排 **原子性** 
	1. 代码重排 **有序性**

#### 并发编程中的三个特性（问题）

1. 可见性：A线程修改后，其他线程看到修改后的值
2. 原子性（指令）：一行代码可能有多个指令，并发时指令会交错进行
3. 有序性（代码）：代码最终的执行顺序和我们写的顺序不同

#### 同步代码块

同步代码块: 由synchronized标注的代码

```java
synchronized (Demo01.class) {
    ...
}
System.out.println("我是run"); // 该方法内部也有
```

#### Synchronized 保证并发三大特性

1. 可见性：执行synchronized时，lock原子操作会刷新工作内存
2. 原子性：只有一个线程能拿到锁从而执行同步代码块
3. 有序性：依然会发生，但是只有一个线程进入同步代码块，从而保证了有序性。

> 原子性和有序性在单线程中没有问题,所以我们在多线程同步写入主内存的过程中,只要模拟单线程就可解决问题,因此添加锁机制. 多线程并发时, 只有获得锁的那一个线程才能写入主内存. 每次获的锁的那个线程都会先执行lock操作, 然后再去写入主内存

多个线程抢夺锁来获得执行同步代码块的权力

#### Synchronized 特征

1. 可重入性：一个线程可以多次执行synchronized,重复获取同一把锁。避免死锁
2. 不可中断性：一个线程获得锁后，另一个线程想要获得锁，必须处于阻塞或等待状态，如果第一个线程不释放锁，第二个线程会一直阻塞或等待，不可被中断。

> 那么一块代码由多个synchronized标注时, 假设一个线程已经抢夺到了锁, 他进入内部同步代码块,发现还需要获得锁,如果他已经获得锁后再也无法获得锁,那么这个线程就会在这卡死,这显然不正确, 所以当一个线程或的锁后,他还可以获的锁, 使他还可以进入同步代码块中,这就是synchronized的可重入性.
>
> 如果一个线程已经获得了锁,那么其他线程还能获得锁吗?如果能,那该线程就是可被中断的,否则,不可被中断, synchronized标识的代码不可被中断

#### synchronized 原理

synchronized的锁对象会关联一个锁monitor, 这个monitor不是我们主动创建的，是JVM的线程执行到这个同步代码块， 发现锁对象没有monitor就会创建monitor

```
synchronized 编译成字节码后

monitorenter

代码逻辑

monitorexit
```

那么什么是锁呢?锁就是monitor

monitor对象的属性主要有:

```c++
ObjectMonitor() {
    _header = NULL;
    _count = 0;
    _waiters = 0，
    _recursions = 0; // 线程的重入次数
    _object = NULL;  // 存储该monitor的对象
    _owner = NULL;   // 标识拥有该monitor的线程
    _WaitSet = NULL; // 处于wait状态的线程，会被加入到_WaitSet
    _WaitSetLock = 0 ;
    _Responsible = NULL;
    _succ = NULL;
    _cxq = NULL;     // 多线程竞争锁时的单向列表
    FreeNext = NULL;
    _EntryList = NULL; // 处于block状态的线程，会被加入到该列表
    _SpinFreq = 0;
    _SpinClock = 0;
    OwnerIsThread = 0;
}
```

_EntryList：处于阻塞状态的线程，未曾获得锁

_owner: 竞争到锁的线程

_WaitSet：处于等待状态的线程，获得锁后释放锁

\_cxq：竞争队列

#### synchronized 的使用建议

1. 减少synchronized 的范围：减少同步代码块中代码的执行时间从而减少其他线程的等待时间
2. 降低synchronized锁的粒度：将一个锁拆分为多个锁提高并发度，
3. 读写分离：读时不加锁，新增修改删除时加锁

#### synchronized与Lock的区别

1. synchronized是关键字，而Lock是一个接口。
2. synchronized会自动释放锁，而Lock必须手动释放锁。
3. synchronized是不可中断的，Lock可以中断也可以不中断。
4. 通过Lock可以知道线程有没有拿到锁，而synchronized不能。
5. synchronized能锁住方法和代码块，而Lock只能锁住代码块。
6. Lock可以使用读锁提高多线程读效率。
7. synchronized是非公平锁，ReentrantLock可以控制是否是公平锁。