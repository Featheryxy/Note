# BigDecimal





BigDecimal用来对超过16位有效位的数进行精确的运算。

双精度浮点型变量double可以处理16位有效数 

Double.valueOf(String) 和Float.valueOf(String)会丢失精度 

```java
BigDecimal a =new BigDecimal(0.1);
System.out.println("a values is:"+a);
System.out.println("=====================");
BigDecimal b =new BigDecimal("0.1");
System.out.println("b values is:"+b);

a values is:0.1000000000000000055511151231257827021181583404541015625
=====================
b values is:0.1

因为0.1无法准确地表示为 double（或者说对于该情况，不能表示为任何有限长度的二进制小数） ，而String可以   

先使用 Double.toString(double) 方法，然后使用 BigDecimal(String)。
要获取该结果，使用static valueOf(double)方法
```

## String2BigDicmal

```java
// BigDecimal bigDecimal = new BigDecimal(new String("100.00"));
BigDecimal bigDecimal = new BigDecimal(100.00);

String string = bigDecimal.toString();
```

## compareTo

```java
a != b?(a>b?:1:-1):0

//前提为a、b均不能为null
if(a.compareTo(b) == -1){
    System.out.println("a小于b");
}
 
if(a.compareTo(b) == 0){
    System.out.println("a等于b");
}
 
if(a.compareTo(b) == 1){
    System.out.println("a大于b");
}
 
if(a.compareTo(b) > -1){
    System.out.println("a大于等于b");
}
 
if(a.compareTo(b) < 1){
    System.out.println("a小于等于b");
}
```



