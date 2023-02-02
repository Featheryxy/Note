---
title: for,foreach,iterator的比较
date: 2020-10-21 22:03:39
tags:
categories: Java
---



for,foreach,iterator的比较

<!-- more -->

# for, foreach, iterator

foreach是语法糖，底层使用的也是iterator。

对于ArrayList, 循环时优先使用for循环，按地址取值

对于LinkedList应该使用迭代器或foreach，因为其在get任何一个位置的数据的时候，都会把前面的数据走一遍

foreach不可以修改，删除遍历的元素。

## 语法糖

指计算机语言中添加的某种语法，这种语法对语言的功能并没有影响，语法糖能够增加程序的可读性，编写的效率。编译器会帮我们做转换

## for

```java
List<String> list = new ArrayList<String>();
String[] arr = new String[]{"1,2,3,4"};
for(int i = 0;i < arr.length;i++){
    System.out.println(arr[i]);
}
for(int i = 0;i < list.size();i++){
    System.out.println(list.get(i));
}
```

## foreach

```java
List<Integer> integers = Arrays.asList(1, 2, 3);
for (Integer num:integers) {
    System.out.println(num);
}
```

```java
         0: iconst_3
         1: anewarray     #2                  // class java/lang/Integer
         4: dup
         5: iconst_0
         6: iconst_1
         7: invokestatic  #3                  // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
        10: aastore
        11: dup
        12: iconst_1
        13: iconst_2
        14: invokestatic  #3                  // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
        17: aastore
        18: dup
        19: iconst_2
        20: iconst_3
        21: invokestatic  #3                  // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
        24: aastore
        25: invokestatic  #4                  // Method java/util/Arrays.asList:([Ljava/lang/Object;)Ljava/util/List;
        28: astore_1
        29: aload_1
        30: invokeinterface #5,  1            // InterfaceMethod java/util/List.iterator:()Ljava/util/Iterator;
        35: astore_2
        36: aload_2
        37: invokeinterface #6,  1            // InterfaceMethod java/util/Iterator.hasNext:()Z
        42: ifeq          65
        45: aload_2
        46: invokeinterface #7,  1            // InterfaceMethod java/util/Iterator.next:()Ljava/lang/Object;
        51: checkcast     #2                  // class java/lang/Integer
        54: astore_3
        55: getstatic     #8                  // Field java/lang/System.out:Ljava/io/PrintStream;
        58: aload_3
        59: invokevirtual #9                  // Method java/io/PrintStream.println:(Ljava/lang/Object;)V
```





```java
// LinkedList的get
public E get(int index) {
    return entry(index).element;
}
private Entry<E> entry(int index) {
    if (index < 0 || index >= size)
        throw new IndexOutOfBoundsException("Index: "+index+
                                            ", Size: "+size);
    Entry<E> e = header;
    if (index < (size >> 1)) {
        // 如果index 位于前一半，从前向后遍历
        for (int i = 0; i <= index; i++)
            e = e.next;
    } else {
        for (int i = size; i > index; i--)
            e = e.previous;
    }
     return e;
}

// ArrayList的get方法源代码
// 直接获取地址O(1)
public E get(int index) {
    rangeCheck(index);
    return elementData(index);
}
```

## Reference



https://www.cnblogs.com/cxuanBlog/p/10927538.html

https://blog.csdn.net/weixin_34087307/article/details/86216558?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param
