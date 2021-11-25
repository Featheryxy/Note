# BigDecimal

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



