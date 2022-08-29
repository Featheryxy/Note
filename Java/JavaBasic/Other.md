# Other

@JsonProperty 此注解用于属性上，作用是把该属性的名称序列化为另外一个名称, 即重命名key

```java
    //@JsonProperty 指定将java对象转化为json格式的时候，对应的key 为"u",不再为url
    @JsonProperty(value = "u")
    private String url;
```

```java
public static void main(String[] args) {
		System.out.println(1);
		// 等价于
		String s = String.valueOf(1);
		System.out.println(s);
	}
```

1. 初始化赋默认值，默认值通常使结果返回false
2. try...catch 捕捉异常
3. 在catch中打印日志，抛出exception

```java
IDataset dataset = null;
		try {
			dataset = session.getDataSet("select channels from tbtrans where trans_code = ", transCode);
		} catch (SQLException e) {
			LcptLog.getConsoleLog().error("渠道查询失败!", e);
			throw new BizBussinessException(IErrMsg.ERR_DBSELECT, "渠道查询失败!");
		}
		return dataset.getString("channels");
```

Java.lang不需要导入