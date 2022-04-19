## Optional

Java 8 引入了Optional来避免空指针异常, Optional就像是包装类，可以把我们的具体数据封装Optional对象内部



```java
	Author author = getAuthor(); 

	// author 为空不报错
	Optional<Author> author = Optional.ofNullable(author);`

    // 不推荐 author 为空报错
    Optional.of(author);
    // 封装 null 对象
    Optional.empty();

    // 会先去判断是否为空，不为空才会去执行消费代码，优雅避免空指针
	Optional.ifPresent();
	// 判断数据是否存在，空则返回false，否则true
	Optional.isPresent() 
        
    // 不推荐，当Optional的get方法为空时会出现异常
	Optional.get();
	Optional.orElseGet();
    Optional.orElseThrow()
	
	// filter
   author.filter(author -> author.getAge() > 18)
       .ifPresent(author -> System.out.println(author.getName()));

	// map
	Optional<List<Book>> books = author.map(author -> author.getBookList());
```

