数组中使用`arr.length` , 类似于数组对象的成员属性，其实是`length`由JVM的指令生成

- "[I"(数组对象)直接由JVM创建

字符串中使用`str.length()`，String对象的成员方法


```java
int[] nums = {-1,0,1,2,-1,-4};
int[][] nums2 = new int[2][2];

System.out.println(nums);  // [I@4554617c
System.out.println(nums.getClass().getName());  // [I
System.out.println(nums2.getClass().getName());  // [[I

System.out.println(nums.length); // 6
```

