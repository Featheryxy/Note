# Json

JSON(JavaScript Object Notation),

- JSON只允许使用UTF-8编码，不存在编码问题；
- JSON只允许使用双引号作为key，特殊字符用`\`转义，格式简单；
- 浏览器内置JSON支持，如果把数据用JSON发送给浏览器，可以用JavaScript直接处理

数据类型

- 键值对：`{"key": value}`
- 数组：`[1, 2, 3]`
- 字符串：`"abc"`
- 数值（整数和浮点数）：`12.34`
- 布尔值：`true`或`false`
- 空值：`null`

# FastJson

用于加密（序列化）和解析（反序列化）对象

```java
// 序列化
String jsonString = JSON.toJSONString(obj);
// 反序列化
VO vo = JSON.parseObject("...", VO.class);
```

```java
public static void main(String[] args) {
		// encoding
		Group group = new Group();
		group.setId(0L);
		group.setName("admin");

		User guestUser = new User();
		guestUser.setId(2L);
		guestUser.setName("guest");

		User rootUser = new User();
		rootUser.setId(3L);
		rootUser.setName("root");

		group.addUser(guestUser);
		group.addUser(rootUser);

		String jsonString = JSON.toJSONString(group);

		System.out.println(jsonString);
		// {"id":0,"name":"admin","users":[{"id":2,"name":"guest"},{"id":3,"name":"root"}]}

		Group grp = JSON.parseObject(jsonString, Group.class);
		System.out.println(grp);
		// Group{id=0, name='admin', users=[jsondemo.User@ba8a1dc, jsondemo.User@4f8e5cde]}
	}
```