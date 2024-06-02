# JavaBean

JavaBean是一种Java语言写成的可重用组件

所谓javaBean，是指符合如下标准的Java类

- 类是公共的，所有属性都是private
- 有一个无参的公共的构造器
- 有属性，且有对应的get、 set方法，如果是boolean类型，会变成is\<PropertyName>
- 实现Serializable接口

重要：声明布尔类型变量时，**优先使用success**，而不是isSuccess，

JavaBean示例

```java
public class JavaBean {
    private String name; // 属性一般定义为private
    private int age;
	private boolean success;
    
	public JavaBean() {
    }
    public int getAge() {
        return age;
    }
    public void setAge(int a) {
        age = a;
    }
    public String getName() {
        return name;
    }
    public void setName(String n) {
        name = n;
    }
    
        public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }
}
```
