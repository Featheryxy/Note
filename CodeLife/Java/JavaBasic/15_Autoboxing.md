## Autoboxing and Autowrapping

包装器：Integer，Long, Float, Double, Short, Byte, Character, Boolean

- 包装器类使用final修饰符修饰
- 尖括号中的参数不能是基本类型
- 自动装箱和自动拆箱是编译器的工作，JVM不参与

```java
// autoboxing
Integer a = 3;
Integer a1 = Integer.valueOf(3);

// autowrapping
int b = a;
int b1 = a.intValue();
//自动装箱和自动拆箱是编译器的工作。
```

