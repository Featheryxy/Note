## Json

JSON(JavaScript Object Notation),

- JSON只允许使用UTF-8编码，不存在编码问题；
- JSON只允许使用双引号作为key，特殊字符用`\`转义，格式简单；
- 浏览器内置JSON支持，如果把数据用JSON发送给浏览器，可以用JavaScript直接处理

### JSON 文件

- JSON 文件的文件类型是 ".json"
- JSON 文本的 MIME 类型是 "application/json"

### 数据类型

JSON可以表示四个基本类型（String、Numbers、Booleans和Null）和两个结构化类型（Objects和Arrays）

#### 基本类型

- 字符串 String：`"abc"`
- 数值（整数和浮点数）Numbers：`12.34`
- 布尔值 Booleans：`true`或`false`
- 空值 Null：`null`

#### 结构化类型

- 对象 Objects：`{"key": value}` 无序的键值对集合，键名必须是字符串，并且不能同名
- 数组 Arrays：`[1, 2, 3]`

### 语法

- 数据在名称/值对中
- 数据由逗号分隔
- 花括号保存对象
- 方括号保存数组

```json
{   
    "employees": [   
        { "firstName":"John" , "lastName":"Doe" },   
        { "firstName":"Anna" , "lastName":"Smith" },   
        { "firstName":"Peter" , "lastName":"Jones" }   
    ]
}
```

对象 "employees" 是包含三个对象的数组。每个对象代表一条关于某人（有姓和名）的记录

## FastJson

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