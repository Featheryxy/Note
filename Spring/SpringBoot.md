```java
// 使用org.springframework.beans.BeanUtils.copyProperties方法进行对象之间属性的赋值，
// 避免通过get、set方法一个一个属性的赋值
public static void copyProperties(Object source, Object target) throws BeansException {
        copyProperties(source, target, (Class)null, (String[])null);
}
```

