Java是面向对象语音，所以必须要创建一个类，由类的实例对象中的某个方法来封装代码

Java 是强类型语言，必须声明参数类型

样板代码模糊了代码本意

面向对象编程是对数据进行抽象，而函数式编程是对行为进行抽象

传递对象，传递行为（方法）

参数可以是对象，也可以时方法

Java 8 还让集合类可以拥有一些额外的方法：default 方法

函数式编程：使用**不可变值**和**函数**，函数对一个**值**进行处理，**映射成另一个值**

java中f.apply(0,1) 等价于数学中的 f(1)


对外暴露Stream 工厂而不是一个 List 或 Set 对象。因为 Stream 暴露集合的最大优点在于，它很好地封装了内部实现的数据结构。仅暴露一个 Stream 接口，用户在实际操作中无论如何使用，都不会影响内部的 List 或 Set。

高阶函数：高阶函数是指接受另外一个**函数作为参数**，或返回一个函数的函数，f(g(x)),  Comparator 函数接口

## 函数式接口

**函数式接口**： **只包含一个抽象方法的接口**，用来表示 Lambda 表达式的类型，程序员只要定义了改接口的参数类型，那么在Lambda 表达式中不需要重复定义参数类型

1. 使用@FunctionalInterface标识
2. 常见的函数式接口
   - Consumer 消费接口：可以对传入的参数进行消费        
   - Function 计算转换接口：根据其中抽象方法的参数列表和返回值类型可以看到，可以在方法中对传入的参数计算或转换，把结果返回
   - Predicate 判断接口：可以在方法对传入的参数条件进行判断，返回判断结果
   - Supplier 生产型接口：可以在方法中创建对象，把创建好的对象返回

3. 常用的默认方法
   - and ：我们在使用Predicate接口的时候可能需要进行判断条件的拼接，而and方法相当于使用&&来拼接两个判断条件
   - or

| 接口               | 参数 | 返回类型 |
| ------------------ | ---- | -------- |
| Predicate\<T>      | T    | boolean  |
| Consumer\<T>       | T    | void     |
| Function<T,R>      | T    | R        |
| Supplier\<T>       | None | T        |
| BinaryOperator\<T> | T，T | T        |

```
Comparator
```



## Lambda

当传递行为时，由于匿名内部类的写法难以阅读，所以使用lambda表达式简写。 Lambda 表达式无需指定类型，编译器javac可以从上下文中的方法签名中进行类型推断

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



**final**：一个 lambda 访问的局部变量必须是 final 的，自 Java 8 起，从匿名类或是 lambda 访问的元素都是隐式 final 的，即Lambda 表达式引用的是值，而不是变量。使用 final 变量时， 只能给该变量赋值一次，实际上是在使用赋给该变量的一个特定的值

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
```

**构造器引用**

```java
Button[] buttons = stream.toArray(Button[] :: new)
```


一个内部类可以访问任何有效的final局部变量

**接口中的默认方法**：如果在接口中定义一个抽象方法, 那么该抽象需要在所有的实现类中实现该方法. 如果子类数量太多，那么要在所有的实现类中实现该方法则显得不现实, 所以可以为顶层接口定义默认方法供所有实现类使用。

类胜于接口。如果在继承链中有方法体或抽象的方法声明，那么就可以忽略接口中定义
的方法。

2. 子类胜于父类。如果一个接口继承了另一个接口，且两个接口都定义了一个默认方法，
    那么子类中定义的方法胜出。
3. 没有规则三。如果上面两条规则不适用，子类要么需要实现该方法，要么将该方法声明
    为抽象方法。

默认方法提供了某种形式上的多重继承功能。

接口允许多重继承，却没有成员变量；抽象类可以继承成员变量，却不能多重继承



创造流的集合有序，则流有序

## Stream

- 外部迭代
  - fori  goto
  - foreache iterator
- 内部迭代
  - steam 

对于流来说,我们不需要告诉流怎么做,只要告诉流做什么就行

惰性求值方法：只描述 Stream，最终不产生新集合的方法，方法返回值为stream

及早求值方法：从 Stream 产生值的方法，返回值是不是stream或为空

操作Stream流的三个阶段

1. 创建一个Stream
2. 在一个或多个步骤中,指定将初始Stream转换为另一个Stream的**中间操作**.
3. 使用一个**终止操作**来产生一个结果.该操作会强制它之前的延迟操作立即执行.在这之后,该Stream就不会再被使用

特点：

1. stream不存储数据，而是按照特定的规则对数据进行计算，一般会输出结果。
2. stream不会改变数据源，通常情况下会产生一个新的集合或一个值。
3. stream具有延迟执行特性，只有调用终止操作时，中间操作才会执行。



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

- filter：流中保留为true的值
- map： 能把一个对象转换成另外一个对象来作为流中的元素
- flatMap：返回值是一个stream, 可以将多个stream合并成一个stream

```java
    public void flatMapCharacters() {
        // BEGIN flatmap_characters
List<Integer> together = Stream.of(asList(1, 2), asList(3, 4))
                               .flatMap(numbers -> numbers.stream())
                               .collect(toList());

assertEquals(asList(1, 2, 3, 4), together);
        
        
    public static int countLowercaseLetters(String string) {
        return (int) string.chars()
                .filter(Character::isLowerCase)
                .count();
    }  
        
	    public static Optional<String> mostLowercaseString(List<String> strings) {
        return strings.stream()
                      .max(Comparator.comparingInt(StringExercises::countLowercaseLetters));
    }        
```

- distinct:返回一个具有相同顺序，且流中无重复元素的新流，注意（该方法依赖的Object的equals方法来判断是否是相同对象，所以要重写equals方法，否则只有对象地址一样时才会被认为是重复）

- sorted:可以对流中的元素进行排序，传入空参时使用的是实体类的比较方法

- limit:设置流的最大长度，超出部分将被抛弃

- skip:跳过流中的前n个元素，返回剩下的元素

  

### 终结操作（聚合方法）

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
- reduce：从一组值中生成一个值，并返回一个Optional描述归约值（如果有）

	​		

```java


List<Track> tracks = asList(new Track("Bakai", 524),
new Track("Violets for Your Furs", 378),
new Track("Time Was", 451));

Track shortestTrack = tracks.get(0);
for (Track track : tracks) {
    if (track.getLength() < shortestTrack.getLength()) {
        shortestTrack = track;
    }
}

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

public static List<String> getNamesAndOrigins(List<Artist> artists) {
    return artists.stream()
        .flatMap(artist -> Stream.of(artist.getName(), artist.getNationality()))
        .collect(toList());
}
```

装箱：将基本类型包装成为一个对象。反之称为拆箱

装箱和拆箱都需要额外的计算开销，为了提高性能，Stream 类的某些方法对基本类型和装箱类型做了区分。在命名上有明确的规范。如果方法返回类型为基本类型，则在基本类型前加 To，如`ToLongFunction`；如果参数是基本类型，则不加前缀只需类型名即可，如`LongFunction`；如果高阶函数使用基本类型，则在操作后加后缀 To 再加基本类型，如 `mapToLong`。这些基本类型都有与之对应的 Stream，以基本类型名为前缀，如 `LongStream`

## Optional

Optional\<T\>对象：对T类型对象的封装，或者表示不是任何对象



```java
Optional emptyOptional = Optional.empty();
Optional alsoEmpty = Optional.ofNullable(null);
assertFalse(emptyOptional.isPresent());
// 例 4-22 中定义了变量 a
assertTrue(a.isPresent());

assertEquals("b", emptyOptional.orElse("b"));
assertEquals("c", emptyOptional.orElseGet(() -> "c"));

// 推荐用法
// 1. 当可选值存在时，对该值操作, 不返回任何值。否则不操作
optionalValue.ifPresent(v -> Process v);
// 等价于
if(optionalValue.isPresent()){
    value = optionalValue.get();
    Process value;
}
// 2. 当可选值存在时，对该值操作, 返回true。否则返回false
Optional<Boolean> isDone =optionalValue.map(v -> Process v);
// 3. 当可选值不存在时，产生替代值或抛出异常
Optional.orElse();
Optional.orElseGet();
Optional.orElseThrow();

// 封装一个可能为null的对象，如果obj != null,则执行Optional.of(obj), 否则 Optional.emp
Optional.ofNullable(obj); 

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

Java 8 中的另一个变化是引入了默认方法和接口的静态方法

```
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

相对于int, Integer 在计算时会带来额外的开销

```
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
    系统可能会推断出多种类型。这时，javac 会挑出最具体的类型。
    
如果只有一个可能的目标类型，由相应函数接口里的参数类型推导得出；
如果有多个可能的目标类型，由最具体的类型推导得出；
如果有多个可能的目标类型且最具体的类型不明确，则需人为指定类型
```



转换成其他集合

```java
    @Test
    public void toCollectionTreeset() {
        Stream<Integer> stream = Stream.of(1, 2, 4, 5,2,4);
        TreeSet<Integer> collect = stream.collect(toCollection(TreeSet::new));
        System.out.println(collect); // [1, 2, 4, 5]
    }
```

数据分块 partitioningBy

```java
public Map<Boolean, List<Artist>> bandsAndSolo(Stream<Artist> artists) {
	return artists.collect(partitioningBy(artist -> artist.isSolo()));
}
```

数据分组 groupingBy

```java
    public Map<Artist, List<Album>> albumsByArtist(Stream<Album> albums) {
        return albums.collect(groupingBy(album -> album.getMainMusician()));
    }
```

字符串

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
```

组合收集器

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

// ----- 
    // BEGIN NAME_OF_ALBUMS_DUMB
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

定制收集器

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
```



```java
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



## 时间

java.time

java.util.Date与UNIX中月份从0开始,年份从1900开始计算, 而java.time月份从1开始

### 时间线

一个Instant对象表示时间轴上的一点, 原点规定为1970年1月1日的午夜.从原点开始,时间按照每天86400秒进行计算.

Duration是两个时点之间的间隔时间

### 本地日期

- 本地日期/时间: 表示一个日期/或一天中的时间 如:2022-08-13
- 带时区的时间