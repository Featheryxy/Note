# JavaBean

JavaBean是一种Java语言写成的可重用组件

所谓javaBean，是指符合如下标准的Java类

- 类是公共的
- 有一个无参的公共的构造器
- 有属性，且有对应的get、 set方法

JavaBean示例

```
public class JavaBean {
    private String name; // 属性一般定义为private
    private int age;
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
}
```



