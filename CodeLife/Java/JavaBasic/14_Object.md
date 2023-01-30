# Object

- 每个类都扩展了Object类
- 可以使用Object类型的变量引用任何类型的对象

## equals()

```java
public boolean equals(Object obj) {
     return (this == obj);
 }

// String 类重写了Object类的String方法。只比较内容是否相同
```

## hashCode()

- Object的hashCode()方法由对象的存储地址得出，每个对象都有一个默认的散列码
- String重写了Object的hashCode()方法，只比较内容是否相同

```java
		String s = "OK";
		StringBuilder sb = new StringBuilder(s);
		System.out.println(s.hashCode()+" "+sb.hashCode()); // 2524 2016447921

		String t = "OK";
		StringBuilder tb = new StringBuilder(s);
		System.out.println(t.hashCode()+" "+tb.hashCode()); // 2524 666988784
```

## toString()

返回对象值的一个字符串。

```java
public String toString() {
    return getClass().getName() + "@" + Integer.toHexString(hashCode());
}
```

