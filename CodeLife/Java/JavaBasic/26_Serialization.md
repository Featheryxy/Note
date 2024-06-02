# Serialization

序列化的目的是为了持久化对象，将对象转换成可存储或传输的形式的过程。反之称为反序列化

一个类想序列化需要实现 Serializable 接口，否则会抛出NotSerializable Exception,因为在序列化操作时会对类的类型进行检查，类型必须属于Enum，Array，Serializable类型中的一种

transient变量在序列化时会被忽略，在反序列化时被设置为初始值

在序列化时会检查字节流中的 serialVersionUID 和本地实体类中的serialVersionUID是否相同，不同这回报错。所以在一个类实现Serializable 接口时，必须手动添加一个`private static final long serialVersionUID`变量，并设置初始值。

序列化可以破坏单例模式，因为序列化是通过反射来调用无参构造器来创建一个新的对象。

可以通过序列化来实现深拷贝`User1 newUser = JSON.parseObject(JSON.toJSONString(user1), User1.class);`



```
public class User1 implements Serializable{
	private static final long serialVersionUID = 6529685098267757690L;

}
```



序列化机制：

- 基于属性：Gson

- 基于setter/getter：fastJson,jackson(Spring默认)

  

```
private boolean isSuccess

        User1 user1 = new User1();
        user1.setName("milo");
        user1.setAge(28);
        user1.setSuccess(true);

        System.out.println(JSON.toJSONString(user1));
        // {"name":"milo","success":true} 属性名不一致
```

