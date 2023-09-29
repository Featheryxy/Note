## 概念

面向对象编程对数据进行抽象，传递对象，从而导致很多样板代码。而函数式编程对行为进行抽象，传递行为。

**函数式编程**：使用**不可变值(final 修饰的变量，i.e. 常量)**和**函数**，函数对一个**值**进行处理，**映射成另一个值**

**高阶函数**：高阶函数是指接受另外一个**函数作为参数**，或返回一个函数的函数，f(g(x)),  Comparator 函数接口

**函数式接口**： 只包含一个抽象方法的接口

1. @FunctionalInterface标识
2. 常见的函数式接口
   - Supplier\<T> 生产者接口：获取一个类型为T的对像
   - Consumer\<T> 消费接口：对类型为T的对像进行处理，无返回值
   - Function<T,R>  计算转换接口：传入类型为T的对像，返回类型为R的对像
   - Predicate\<T>  判断接口：传入类型为T的对像，返回True or False
   - Comparator\<T>
   - BinaryOperator\<T>  





Java 8 还让集合类可以拥有一些额外的方法：default 方法

java中f.apply(0,1) 等价于数学中的 f(1)

## 接口默认方法与静态方法

**接口中的默认方法**：如果在接口中定义一个抽象方法, 那么该抽象需要在所有的实现类中实现该方法. 如果子类数量太多，那么要在所有的实现类中实现该方法则显得不现实, 所以可以为顶层接口定义默认方法供所有实现类使用。

**接口的多继承：**

1. 类胜于接口。如果在继承链中有方法体或抽象的方法声明，那么就可以忽略接口中定义

的方法。

2. 子类胜于父类。如果一个接口继承了另一个接口，且两个接口都定义了一个默认方法，
   那么子类中定义的方法胜出。
3. 没有规则三。如果上面两条规则不适用，子类要么需要实现该方法，要么将该方法声明
   为抽象方法。

接口允许多重继承，却没有成员变量；

抽象类可以继承成员变量，却不能多重继承

## 内部类

在一个类中定义另一个类，前者称为**内部类**，后者称为**外部类**

分类：

- 成员内部类（static成员内部类和非static成员内部类）
- 局部内部类（不谈修饰符,  方法内，代码块内，构造器内）、匿名内部类

**内部类可以直接访问外部类的成员，包括私有。**

外部类要访问内部类的成员，必须创建内部类对象。

## Lambda

Java是面向对象语音，所以必须要创建一个类，由类的实例对象中的某个方法来封装代码。

当传递行为时，行为的代码同样需要封装（匿名内部类）。匿名内部类是局部内部类的一种特殊形式，没有类名。

其在创建对象的时候定义类，其本质**是一个接口或者抽象类的实现类**。但由于匿名内部类的写法难以阅读，所以使

用lambda表达式简写，省去类的定义和方法定义。

Java 是强类型语言，必须声明参数类型。 因为在加载匿名内部类之前已经加载了父类或父接口，而父类或父接口

已经有了该匿名内部类的类定义和方法定义，所以编译器javac可以从上下文中的方法签名中进行类型推断，所以

Lambda 表达式无需指定类的定义和方法定义。



**Lambda表达式**： 函数式接口的实例，匿名内部类的简写，

- 形式：(参数类型 变量，……) -> {表达式}， 
- 省略参数类型：如果参数类型可被推导，则参数类型可被省略。
- 省略小括号：如果没有参数或只有一个参数，小括号也可省略。
- 省略大括号：只有一行表达式时

```java
BinaryOperator<Long> add = new BinaryOperator<Long>() {
    @Override
    public Long apply(Long x, Long y) {
        return x + y;
    }
};

BinaryOperator<Long> add = (x, y) -> x + y;

BinaryOperator<Long> add = Long::sum;


BinaryOperator<Long> addLongs = (x, y) -> x + y;

// error
BinaryOperator add = (x, y) -> x + y; 
```

**final**：一个 lambda 访问的局部变量必须是 final 的，自 Java 8 起，从匿名类或是 lambda 访问的元素都是隐式 final 的，即Lambda 表达式引用的是值（常量），而不是变量。使用 final 变量时， 只能给该变量赋值一次，实际上是在使用赋给该变量的一个特定的值。

仅使用一次的函数可以被定义为匿名实例。

**方法引用**：更简短的写法，当 lambda 的实现是一个单参的方法调用时, 引用其他类的方法。Classname::methodName

```java
button.setOnAction(event -> System.out.println(event));

// 方法引用, 使用 :: 来分隔对象和方法名
button.setOnAction(System.out::println);
方法引用：用于替换这个 lambda 的语法
Function<Double, Double> sin = Math::sin;
Function<Double, Double> sin2 = a -> Math.sin(a);

对象 :: 实例方法
类 :: 静态方法
类 :: 实例方法    
this :: 方法
super :: 方法    

构造器引用
Button[] buttons = stream.toArray(Button[] :: new)
```

## Stream

- 外部迭代
  - fori  goto
  - foreache iterator
- 内部迭代
  - steam 

特点

1. 惰性求值方法：只描述 Stream，最终不产生新集合的方法，方法返回值为stream
2. 及早求值方法：从 Stream 产生值的方法，返回值是不是stream或为空
3. 创造流的集合有序，则流有序



lambda表达式中的参数可以是任意合法变量名，代表流中的每一个元素，

### 基本类型

相对于int, Integer 在计算时会带来额外的开销

装箱：将基本类型包装成为一个对象。反之称为拆箱

装箱和拆箱都需要额外的计算开销，为了提高性能，Stream 类的某些方法对基本类型和装箱类型做了区分。在命名上有明确的规范。如果方法返回类型为基本类型，则在基本类型前加 To，如`ToLongFunction`；如果参数是基本类型，则不加前缀只需类型名即可，如`LongFunction`；如果高阶函数使用基本类型，则在操作后加后缀 To 再加基本类型，如 `mapToLong`。这些基本类型都有与之对应的 Stream，以基本类型名为前缀，如 `LongStream`

```java
public interface ToLongFunction<T> {

    /**
     * Applies this function to the given argument.
     *
     * @param value the function argument
     * @return the function result
     */
    long applyAsLong(T value);
}

@FunctionalInterface
public interface LongFunction<R> {

    /**
     * Applies this function to the given argument.
     *
     * @param value the function argument
     * @return the function result
     */
    R apply(long value);
}

LongStream mapToLong(DoubleToLongFunction mapper);


public static void printTrackLengthStatistics(Album album) {
    IntSummaryStatistics trackLengthStats
            = album.getTracks()
                   .mapToInt(track -> track.getLength())
                   .summaryStatistics();

    System.out.printf("Max: %d, Min: %d, Ave: %f, Sum: %d",
                      trackLengthStats.getMax(),
                      trackLengthStats.getMin(),
                      trackLengthStats.getAverage(),
                      trackLengthStats.getSum());
}
```



### 类型推断

系统可能会推断出多种类型。这时，javac 会挑出最具体的类型。

```java
private void overloadedMethod(Object o) {
    System.out.print("Object");
}

private void overloadedMethod(String s) {
    System.out.print("String");
}

    @Test
    public void mostSpecific() {
        overloadedMethod("abc");
        // String
    }
    
    
如果只有一个可能的目标类型，由相应函数接口里的参数类型推导得出；
如果有多个可能的目标类型，由最具体的类型推导得出；
如果有多个可能的目标类型且最具体的类型不明确，则需人为指定类型
```



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
```

### 常用方法

- filter, `Stream<T> filter(Predicate<? super T> predicate)` : 流中保留为true的元素
- distinct: 返回一个具有相同顺序，且流中无重复元素的新流，注意（该方法依赖的Object的equals方法来判断是否是相同对象，所以要重写equals方法，否则只有对象地址一样时才会被认为是重复）
- sorted: 可以对流中的元素进行排序，传入空参时使用的是实体类的比较方法
- limit: 设置流的最大长度，超出部分将被抛弃
- skip: 跳过流中的前n个元素，返回剩下的元素 

- forEach:遍历所有元素
- count:计算元素数量
- min&max:返回的是option对象，这里和sorted一样，得指定比较规则
- collect:把当前流转换成一个集合（list, set, map）

  - Collectors.toList() ：	`List<String> collected = Stream.of("a", "b", "c") .collect(Collectors.toList()); `
  - Collectors.toSet()
  - Collectors.toMap(key, value)

- anyMatch（相当于in的操作）:可以用来判断是否有任意符合匹配条件的元素，结果为boolean类型，
- allMatch:可以用来判断是否都匹配条件，结果也是boolean类型，都符合则为true
- noneMatch:是否都不符合，都不符合则为true
- findAny:获取流中的任意一个元素，该方法无法保证获取的是流中的第一个元素，一旦匹配到就返回。速度比findFirst块
- findFirst:获取流中的第一个元素



### map and flatmap

- map： 将流中的每个元素从一个对象转换成另外一个对象
- flatMap：返回值是一个stream, 可以将多个stream合并成一个stream 

```java
<R> Stream<R> map(Function<? super T, ? extends R> mapper);

<R> Stream<R> flatMap(Function<? super T, ? extends Stream<? extends R>> mapper);


    public void test2(){
        List<People> peopleList = List.of(new People("milo", 27), new People("lucy", 18));
        List<Stream<? extends Serializable>> china = peopleList.stream().
                map(p -> Stream.of(p.getName(), "China")).
                collect(Collectors.toList());
        System.out.println(china);
//      [java.util.stream.ReferencePipeline$Head@394df057, java.util.stream.ReferencePipeline$Head@4961f6af]
        
        List<String> people = peopleList.stream().
                flatMap(p -> Stream.of(p.getName(), "China")).
                collect(Collectors.toList());
        System.out.println(people);
//        [milo, China, lucy, China]
    }
```

### reduce

给定一个初始值和函数，对流中的每个元素执行函数，返回一个Optional描述归约值（如果有）

```
reduce 模式
accumulator 累加器；积聚者
Object accumulator = initialValue;
for(Object element : collection) {
	accumulator = combine(accumulator, element);
}
这个模式中的两个可变项是 initialValue 初始值和 combine 函数

int count = Stream.of(1, 2, 3).reduce(0, (acc, element) -> acc + element);
// 等价于
int acc = 0;
for (Integer element : asList(1, 2, 3)) {
	acc = acc + element;
}
```

### 收集器

#### 转换成其他集合

调用 toList 或者 toSet 方法时，不需要指定具体的类型。Stream 类库在背后自动为你
挑选出了合适的类型

```java
    @Test
    public void test3(){
        Stream<Integer> stream = Stream.of(1, 2, 4, 5, 2, 4);
        TreeSet<Integer> collect = stream.collect(Collectors.toCollection(TreeSet::new));
        System.out.println(collect); 
        // [1, 2, 4, 5]
    }
```

#### 转换成值

```java
        Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5);
        int sum = stream.mapToInt(Integer::intValue) // 转换成IntStream
                .sum();
```

#### 数据分块

partitioningBy, 将数据分成 ture 和 false 两部分

```java
public Map<Boolean, List<Artist>> bandsAndSolo(Stream<Artist> artists) {
	return artists.collect(partitioningBy(artist -> artist.isSolo()));
}
```

#### 数据分组

groupingBy

```java
    public Map<Artist, List<Album>> albumsByArtist(Stream<Album> albums) {
        return albums.collect(groupingBy(album -> album.getMainMusician()));
    }
```

#### 字符串

```java
StringBuilder builder = new StringBuilder("[");
for (Artist artist : artists) {
    if (builder.length() > 1)
    	builder.append(", ");
    
    String name = artist.getName();
    builder.append(name);
}
builder.append("]");
String result = builder.toString();

String result =
	artists.stream()
		.map(Artist::getName)
		.collect(Collectors.joining(", ", "[", "]"));

public static int countLowercaseLetters(String string) {
    return (int) string.chars()
            .filter(Character::isLowerCase)
            .count();
}  
    
public static Optional<String> mostLowercaseString(List<String> strings) {
    return strings.stream()                .max(Comparator.comparingInt(StringExercises::countLowercaseLetters));
}  
```

#### 组合收集器

```java
    public Map<Artist, Integer> numberOfAlbumsDumb(Stream<Album> albums) {
        Map<Artist, List<Album>> albumsByArtist
                = albums.collect(groupingBy(album -> album.getMainMusician()));

        Map<Artist, Integer> numberOfAlbums = new HashMap<>();
        for (Entry<Artist, List<Album>> entry : albumsByArtist.entrySet()) {
            numberOfAlbums.put(entry.getKey(), entry.getValue().size());
        }
        return numberOfAlbums;
    }

	public Map<Artist, Long> numberOfAlbums(Stream<Album> albums) {
        return albums.collect(groupingBy(album -> album.getMainMusician(),
                counting()));
    }

// ---------
    public Map<Artist, List<String>> nameOfAlbumsDumb(Stream<Album> albums) {
        Map<Artist, List<Album>> albumsByArtist =
                albums.collect(groupingBy(album -> album.getMainMusician()));

        Map<Artist, List<String>> nameOfAlbums = new HashMap<>();
        for (Entry<Artist, List<Album>> entry : albumsByArtist.entrySet()) {
            nameOfAlbums.put(entry.getKey(), entry.getValue()
                    .stream()
                    .map(Album::getName)
                    .collect(toList()));
        }
        return nameOfAlbums;
    }

    // mapping 下游收集器，用以收集最终结果的一个子集
	//  averagingInt、summarizingLong
    public Map<Artist, List<String>> nameOfAlbums(Stream<Album> albums) {
        return albums.collect(groupingBy(Album::getMainMusician,
                mapping(Album::getName, toList())));
    }
```

#### 定制收集器

compute, computeIfAbsent

```java
public Artist getArtist(String name) {
    Artist artist = artistCache.get(name);
    if (artist == null) {
        artist = readArtistFromDB(name);
        artistCache.put(name, artist);
    }
    return artist;
}

public Artist getArtist(String name) {
	return artistCache.computeIfAbsent(name, this::readArtistFromDB);
}

compute：计算并更新值
computeIfAbsent：Value不存在时才计算
computeIfPresent：Value存在时才计算

/**
* 来源：Java技术栈
*/
default V compute(K key,
        BiFunction<? super K, ? super V, ? extends V> remappingFunction) {
        
    // 函数式接口不能为空    
    Objects.requireNonNull(remappingFunction);
    
    // 获取旧值
    V oldValue = get(key);

    // 获取计算的新值
    V newValue = remappingFunction.apply(key, oldValue);
    
    if (newValue == null) { // 新值为空
        // delete mapping
        if (oldValue != null || containsKey(key)) { // 旧值存在时
            // 移除该键值
            remove(key);
            return null;
        } else {
            // nothing to do. Leave things as they were.
            return null;
        }
    } else { // 新值不为空
        // 添加或者覆盖旧值
        put(key, newValue);
        return newValue;
    }
}


Map<Artist, Integer> countOfAlbums = new HashMap<>();
for(Map.Entry<Artist, List<Album>> entry : albumsByArtist.entrySet()) {
    Artist artist = entry.getKey();
    List<Album> albums = entry.getValue();
	countOfAlbums.put(artist, albums.size());
}

Map<Artist, Integer> countOfAlbums = new HashMap<>();
    albumsByArtist.forEach((artist, albums) -> {
    countOfAlbums.put(artist, albums.size());
});

public long countRunningTime() {
    long count = 0;
    for (Album album : albums) {
        for (Track track : album.getTrackList()) {
            count += track.getLength();
        }
    }
    return count;
}

public long countRunningTime() {
    return albums.stream()
            .mapToLong(album -> album.getTracks()
                                     .mapToLong(track -> track.getLength())
                                     .sum())
            .sum();
}

```



## Optional

Optional\<T\>对象：对T类型对象的封装，或者表示不是任何对象

```java
// 1. 当可选值存在时，对该值操作, 不返回任何值。否则不操作
optionalValue.ifPresent(v -> Process v);
// 等价于
if(optionalValue.isPresent()){
    value = optionalValue.get();
    Process value;
}

// 2. 当可选值存在时，对该值操作, 返回true。否则返回false
Optional<Boolean> isDone =optionalValue.map(v -> Process v);

// 3. 当可选值存在时，返回可选值。当可选值不存在时，产生替代值或抛出异常
Optional.orElse();
Optional.orElseGet();
Optional.orElseThrow();

// 封装一个可能为null的对象，如果obj != null,则执行Optional.of(obj), 否则 Optional.empy
Optional.ofNullable(obj); 

Author author = getAuthor(); 
// author 为空不报错
Optional<Author> author = Optional.ofNullable(author);`
// 不推荐 author 为空报错
Optional.of(author);
// 封装 null 对象
Optional.empty();
```











Lambda测试

```
public static List<String> elementFirstToUppercase(List<String> words) {
    return words.stream()
    .map(Testing::firstToUppercase)
    .collect(Collectors.<String>toList());
}
public static String firstToUppercase(String value) { 
    char firstChar = Character.toUpperCase(value.charAt(0));
    return firstChar + value.substring(1);
}

@Test
public void twoLetterStringConvertedToUppercase() {
    String input = "ab";
    String result = Testing.firstToUppercase(input);
    assertEquals("Ab", result);
}
```

流有一个方法让你能查看每个值，同时能继续操作流。这就是 peek 方法

## advise

### 单元测试

1. lambda表达式分行
2. 使用方法引用
3. 使用peek打印中间状态，在peek

### 对外暴露Stream 工厂, 而不是一个 List 或 Set 对象

因为 Stream 暴露集合的最大优点在于，它很好地封装了内部实现的数据结构。仅暴露一个 Stream 接口，用户在实际操作中无论如何使用，都不会影响内部的 List 或 Set。

### 使用高阶函数

如果有一个整体上大概相似的模式，只是行为上有所不同，就可以试着加入一个 Lambda 表达式

```java
Logger logger = new Logger();
if (logger.isDebugEnabled()) {
	logger.debug("Look at this: " + expensiveOperation());
}
// 将logger.isDebugEnabled()封装到debug方法中
Logger logger = new Logger();
logger.debug(() -> "Look at this: " + expensiveOperation());

public long countRunningTime() {
	long count = 0;
	for (Album album : albums) {
		for (Track track : album.getTrackList()) {
			count += track.getLength();
		}
	}
	return count;
}

public long countMusicians() {
	long count = 0;
	for (Album album : albums) {
		count += album.getMusicianList().size();
	}
	return count;
}

// 改为流
public long countRunningTime() {
	return albums.stream()
		.mapToLong(album -> album.getTracks()
								.mapToLong(track -> track.getLength())
								.sum())
		.sum();
}
public long countMusicians() {
	return albums.stream()
		.mapToLong(album -> album.getMusicians().count())
		.sum();
}

// 改为领域行为
public long countFeature(ToLongFunction<Album> function) {
	return albums.stream()
				.mapToLong(function)
				.sum();
}
public long countTracks() {
	return countFeature(album -> album.getTracks().count());
}
public long countRunningTime() {
	return countFeature(album -> album.getTracks()
						.mapToLong(track -> track.getLength())
						.sum());
}
```



## 时间

java.time

java.util.Date与UNIX中月份从0开始,年份从1900开始计算, 而java.time月份从1开始

### 时间线

一个Instant对象表示时间轴上的一点, 原点规定为1970年1月1日的午夜.从原点开始,时间按照每天86400秒进行计算.

Duration是两个时点之间的间隔时间

### 本地日期

- 本地日期/时间: 表示一个日期/或一天中的时间 如:2022-08-13
- 带时区的时间