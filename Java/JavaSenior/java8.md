Java是面向对象语音，所以必须要创建一个类，由类的实例对象中的某个方法来封装代码

Java 是强类型语言，必须声明参数类型

lambda表达式: (参数类型 变量，……) -> 表达式。

 如果参数类型可被推导，则参数类型可被省略，如果没有参数或只有一个参数，小括号也可省略



函数式接口 只包含一个抽象方法的接口

Lambda表达式 函数式接口的实例



方法引用：传递给其他代码的操作已经有实现的方法

```java
button.setOnAction(event -> System.out.println(event));

// 方法引用, 使用 :: 来分隔方法名和 （对象或类）的名字
button.setOnAction(System.out::println);

对象 :: 实例方法
类 :: 静态方法
类 :: 实例方法    
this :: 方法
super :: 方法    
```

构造器引用

```java
Button[] buttons = stream.toArray(Button[] :: new)
```


一个内部类可以访问任何有效的final局部变量

接口中的默认方法:如果在接口中定义一个抽象方法, 那么该抽象需要在所有的实现类中实现该方法. 如果子类数量太多,那么要在所有的实现类中实现该方法则显得不现实,所以可以为顶层接口定义默认方法供所有实现类使用



对于流来说,我们不需要告诉流怎么做,只要告诉流做什么就行



操作Stream流的三个阶段

1. 创建一个Stream
2. 在一个或多个步骤中,指定将初始Stream转换为另一个Stream的中间操作.
3. 使用一个终止操作来产生一个结果.该操作会强制它之前的延迟操作立即执行.在这之后,该Stream就不会再被使用



lambda表达式中的参数可以是任意合法变量名，代表流中的每一个元素，

### 创建流


```java
        // 数组：Arrays.stream(arr)
        int[] ints = {1, 2, 3};
        IntStream stream = Arrays.stream(ints);
        Stream<int[]> ints1 = Stream.of(ints);

        // 单列集合: 集合对象.stream()
        List<Author> authors = getAuthors();
        Stream<Author> stream1 = authors.stream();

        // 双列集合: 先将双列对象转换成单例后再创建
        Map<String, String> map = new HashMap<>();
        map.put("Mike", "male");
        map.put("Lucy", "female");
        map.put("Lisa", "female");

        Set<Map.Entry<String, String>> entries = map.entrySet();
        entries.stream()
                .filter(entry-> "male".equals(entry.getValue()))
                .forEach(System.out::println);
        // Mike=male
```

### 中间操作

每一次中间操作都会将收集到的值到一个新的流

- filter

- map:相当于对数据进行一个操作，可以自定义返回值等

- distinct:返回一个具有相同顺序，且流中无重复元素的新流，注意（该方法依赖的Object的equals方法来判断是否是相同对象，所以要重写equals方法，否则只有对象地址一样时才会被认为是重复）

- sorted:可以对流中的元素进行排序，传入空参时使用的是实体类的比较方法

- limit:设置流的最大长度，超出部分将被抛弃

- skip:跳过流中的前n个元素，返回剩下的元素

- flatMap: map能把一个对象转换成另外一个对象来作为流中的元素，而flatMap可以把一个对象转换成多个对象作为流中的元素

### 终结操作（聚合方法）

- forEach:遍历所有元素
- count:计算元素数量
- min&max:返回的是option对象，这里和sorted一样，得指定比较规则
- collect:把当前流转换成一个集合（list, set, map）

  - Collectors.toList()
  - Collectors.toSet()
  - Collectors.toMap(key, value)



- anyMatch（相当于in的操作）:可以用来判断是否有任意符合匹配条件的元素，结果为boolean类型，
- allMatch:可以用来判断是否都匹配条件，结果也是boolean类型，都符合则为true
- noneMatch:是否都不符合，都不符合则为true
- findAny:获取流中的任意一个元素，该方法无法保证获取的是流中的第一个元素，一旦匹配到就返回。速度比findFirst块
- findFirst:获取流中的第一个元素
- reduce:对流中的数据按照你制定的计算方式计算出一个结果，并返回一个Optional描述归约值（如果有）



## Optional

Optional\<T\>对象：对T类型对象的封装，或者表示不是任何对象



1. ```java
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


   	// 推荐用法
       // 1. 当可选值存在时，对该值操作, 不返回任何值。否则不操作
       optionalValue.ifPresent(v -> Process v);
   	
   	if(optionalValue.isPresent()){
           value = optionalValue.get();
           Process value;
       }
       // 2. 当可选值存在时，对该值操作, 返回true。否则返回false
   	Optional<Boolean> isDone =optionalValue.map(v -> Process v);
       // 3. 当可选值不存在时，产生替代值
       Optional.orElse();
         
        Optional.orElseGet();
        Optional.orElseThrow();
   
   	// 封装一个可能为null的对象，如果obj != null,则执行Optional.of(obj), 否则 Optional.emp
   	Optional.ofNullable(obj); 
   	
   ```



   ```





Optional.