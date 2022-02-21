## 1 概述

Java 集合可分为 Collection 和 Map 两种体系

- Collection接口： 单列数据， 定义了存取一组对象的方法的集合
  - List： 元素有序、可重复的集合
  - Set： 元素无序、不可重复的集合
-  Map接口： 双列数据，保存具有映射关系“key-value对”的集合  



继承树

![Collection](https://github.com/Featheryxy/JavaBasic/blob/main/Collection%20and%20Map.assets/Collection.png)

![Map](https://github.com/Featheryxy/JavaBasic/blob/main/Collection%20and%20Map.assets/Map.png)

## 2 Collection

### 2.1 添加

**add(Object obj)**

```java
        Collection coll = new ArrayList();

        //add(Object e):将元素e添加到集合coll中
        coll.add("AA");
        coll.add("BB");
        coll.add(123);//自动装箱
        coll.add(new Date());
        System.out.println(coll);
//      coll: [AA, BB, 123, Wed Jun 24 12:36:17 CST 2020]
```

**addAll(Collection coll)**

```java
        //addAll(Collection coll1):将coll1集合中的元素添加到当前的集合中
        Collection coll1 = new ArrayList();
        coll1.add(456);
        coll1.add("CC");
        coll.addAll(coll1);
//      [AA, BB, 123, Wed Jun 24 12:36:17 CST 2020, 456, CC]
```

### 2.2 获取有效元素的个数

**int size()**

```java
        Collection coll = new ArrayList();

        //add(Object e):将元素e添加到集合coll中
        coll.add("AA");
        coll.add("BB");
        coll.add(123);//自动装箱
        coll.add(new Date());
        System.out.println(coll);

        System.out.println("coll: "+coll);
//      coll: [AA, BB, 123, Wed Jun 24 12:36:17 CST 2020]

        //size():获取添加的元素的个数
        System.out.println("coll.size()->"+coll.size());
//      coll.size()->4
```

### 2.3 清空集合

 **void clear()**

```java
        //clear():清空集合元素
        coll.clear();

```

### 2.4 是否是空集合

**boolean isEmpty()**

```
        //isEmpty():判断当前集合是否为空
        System.out.println(coll.isEmpty());
```

### 2.5 是否包含某个元素

**boolean contains(Object obj)**：判断当前集合中是否包含obj，我们在**判断时会调用obj对象所在类的equals()**。

```
        Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        
        coll.add(new Person("Jerry",20));
        System.out.println(coll.contains(new Person("Jerry",20)));
        //false 调用object类的equals方法，对比对象的引用是否相等

        coll.add(new String("Tom"));
        System.out.println(coll.contains(new String("Tom")));
        //true  String的equals方法重写了Object,比较的是对象的值是否相等
        
        System.out.println(coll);
//      [123, 456, Person{name='Jerry', age=20}, Tom]
```

通过重写Person类中的equals()可以得到想要的结果

```java
    @Override
    public boolean equals(Object o) {
        System.out.println("Person equals()....");
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age &&
                Objects.equals(name, person.name);
    }
```

```java
		Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        
        coll.add(new Person("Jerry",20));
        System.out.println(coll.contains(new Person("Jerry",20)));
//      Person equals()....
//      Person equals()....
//      Person equals()....
//      true
```

**boolean containsAll(Collection c)**： 也是调用元素的equals方法来比较的。 拿两个集合的元素挨个比较。  

```java
        Collection coll1 = Arrays.asList(123,4567);
        System.out.println(coll.containsAll(coll1));
//      false
```

### 2.6 删除

**boolean remove(Object obj)** ： 通过元素的equals方法判断是否是要删除的那个元素。 只会删除找到的第一个元素

```java
        Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        coll.add(new Person("Jerry",20));
        coll.add(new String("Tom"));
        coll.add(false);

        coll.remove(1234);
        System.out.println(coll);
//      [123, 456, Person{name='Jerry', age=20}, Tom, false]

        coll.remove(new Person("Jerry",20));
        System.out.println(coll);
//      Person equals()....
//      Person equals()....
//      Person equals()....
//      [123, 456, Tom, false]
   
```

**boolean removeAll(Collection coll)**： 取当前集合的差集  

```java
        Collection coll1 = Arrays.asList(123,456);
        coll.removeAll(coll1);
        System.out.println(coll);
        // [Tom, false]
```

### 2.7 取两个集合的交集

**boolean retainAll(Collection c)**： 把交集的结果存在当前集合中，不影响c  

```java
        Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        coll.add(new Person("Jerry",20));
        coll.add(new String("Tom"));
        coll.add(false);

        Collection coll1 = Arrays.asList(123,456,789);
        coll.retainAll(coll1);
        System.out.println(coll);
//        Person equals()....
//        Person equals()....
//        Person equals()....
//        [123, 456]
```

### 2.8 集合是否相等

 **boolean equals(Object obj)**  要想返回true，需要当前集合和形参集合的元素都相同。

```java
        Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        coll.add(new Person("Jerry",20));
        coll.add(new String("Tom"));
        coll.add(false);

        Collection coll1 = new ArrayList();
        coll1.add(456);
        coll1.add(123);
        coll1.add(new Person("Jerry",20));
        coll1.add(new String("Tom"));
        coll1.add(false);

        System.out.println(coll.equals(coll1));
//      false
```

### 2.9 转成对象数组

 **Object[] toArray()**  

```java
        Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        coll.add(new Person("Jerry",20));
        coll.add(new String("Tom"));
        coll.add(false);

        //8.集合 --->数组：toArray()
        Object[] arr = coll.toArray();
        for(int i = 0;i < arr.length;i++){
            System.out.println(arr[i]);
        }
//        123
//        456
//        Person{name='Jerry', age=20}
//        Tom
//        false

        //拓展：数组 --->集合:调用Arrays类的静态方法asList()
        List<String> list = Arrays.asList(new String[]{"AA", "BB", "CC"});
        System.out.println(list);
//      [AA, BB, CC]
        
        List arr1 = Arrays.asList(new int[]{123, 456});
        System.out.println(arr1.size());//1

        List arr2 = Arrays.asList(new Integer[]{123, 456});
        System.out.println(arr2.size());//2
```

### 2.10 获取集合对象的哈希值

**hashCode()**  返回当前对象的哈希值

```
        Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        coll.add(new Person("Jerry",20));
        coll.add(new String("Tom"));
        coll.add(false);

        //7.hashCode():返回当前对象的哈希值
        System.out.println(coll.hashCode());
//      -1953130211
```

### 2. 11 遍历

#### 2.11.1 iterator

**iterator()**： 返回迭代器对象，用于集合遍历  

  * 集合元素的遍历操作，使用迭代器Iterator接口
  * 内部的方法：hasNext() 和  next()
  * 集合对象每次调用iterator()方法都得到一个全新的迭代器对象，
  * 默认游标都在集合的第一个元素之前。
  * 内部定义了remove(),可以在遍历的时候，删除集合中的元素。此方法不同于集合直接调用remove()
  ```java
        Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        coll.add(new Person("Jerry",20));
        coll.add(new String("Tom"));
        coll.add(false);

        Iterator iterator = coll.iterator();
        //方式一：
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());
//        System.out.println(iterator.next());
//        //报异常：NoSuchElementException
//        System.out.println(iterator.next());

        //方式二：不推荐
//        for(int i = 0;i < coll.size();i++){
//            System.out.println(iterator.next());
//        }

        //方式三：推荐
        ////hasNext():判断是否还有下一个元素
        while(iterator.hasNext()){
            //next():①指针下移 ②将下移以后集合位置上的元素返回
            System.out.println(iterator.next());
        }
  ```

**remove()**

如果还未调用next()或在上一次调用 next 方法之后已经调用了 remove 方法，再调用remove都会报IllegalStateException。

```java
 		Collection coll = new ArrayList();
        coll.add(123);
        coll.add(456);
        coll.add(new Person("Jerry",20));
        coll.add(new String("Tom"));
        coll.add(false);

        //删除集合中"Tom"
        Iterator iterator = coll.iterator();
        while (iterator.hasNext()){
//            iterator.remove();   // IllegalStateException
            Object obj = iterator.next();
            if("Tom".equals(obj)){
//                iterator.remove();
            }

        }
        //遍历集合
        iterator = coll.iterator();
        while (iterator.hasNext()){
            System.out.println(iterator.next());
        }
    }
```

#### 2.11.2 foreach

```java
    Collection coll = new ArrayList();
    coll.add(123);
    coll.add(456);
    coll.add(new Person("Jerry",20));
    coll.add(new String("Tom"));
    coll.add(false);

    //for(集合元素的类型 局部变量 : 集合对象)
    //内部仍然调用了迭代器。
    for(Object obj : coll){
        System.out.println(obj);
    }
```

区别

```java
        String[] arr = new String[]{"MM","MM","MM"};

        //方式一：普通for赋值
        for(int i = 0;i < arr.length;i++){
            arr[i] = "GG";
        }

        //方式二：增强for循环
//        for(String s : arr){
//            s = "GG";
//        }
//        输出：arr = ["MM","MM","MM"]

//      方式二等价于
//        for(int i = 0; i < arr.length; i++){
//            String s = arr[i];
//         			 s = "GG";
//        }

        for(int i = 0;i < arr.length;i++){
            System.out.println(arr[i]);
        }
//        GG
//        GG
//        GG
```

## 3 List

### 3.1 ArrayList, LinkedList, Vector

```
*    |----Collection接口：单列集合，用来存储一个一个的对象
*          |----List接口：存储有序的、可重复的数据。  -->“动态”数组,替换原有的数组
*              |----ArrayList：作为List接口的主要实现类；线程不安全的，效率高；底层使用Object[] elementData存储
*              |----LinkedList：对于频繁的插入、删除操作，使用此类效率比ArrayList高；底层使用双向链表存储
*              |----Vector：作为List接口的古老实现类；线程安全的，效率低；底层使用Object[] elementData存储
*
*
*   2. ArrayList的源码分析：
*   2.1 jdk 7情况下
*      ArrayList list = new ArrayList();//底层创建了长度是10的Object[]数组elementData
*      list.add(123);//elementData[0] = new Integer(123);
*      ...
*      list.add(11);//如果此次的添加导致底层elementData数组容量不够，则扩容。
*      默认情况下，扩容为原来的容量的1.5倍，同时需要将原有数组中的数据复制到新的数组中。
*
*      结论：建议开发中使用带参的构造器：ArrayList list = new ArrayList(int capacity)
*
*   2.2 jdk 8中ArrayList的变化：
*      ArrayList list = new ArrayList();//底层Object[] elementData初始化为{}.并没有创建长度为10的数组
*
*      list.add(123);//第一次调用add()时，底层才创建了长度10的数组，并将数据123添加到elementData[0]
*      ...
*      后续的添加和扩容操作与jdk 7 无异。
*   2.3 小结：jdk7中的ArrayList的对象的创建类似于单例的饿汉式，而jdk8中的ArrayList的对象
*            的创建类似于单例的懒汉式，延迟了数组的创建，节省内存。
*
*  3. LinkedList的源码分析：
*      LinkedList list = new LinkedList(); 内部声明了Node类型的first和last属性，默认值为null
*      list.add(123);//将123封装到Node中，创建了Node对象。
*
*      其中，Node定义为：体现了LinkedList的双向链表的说法
*      private static class Node<E> {
            E item;
            Node<E> next;
            Node<E> prev;

            Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
            }
        }
*
*   4. Vector的源码分析：jdk7和jdk8中通过Vector()构造器创建对象时，底层都创建了长度为10的数组。
*      在扩容方面，默认扩容为原来的数组长度的2倍。
*
*  面试题：ArrayList、LinkedList、Vector三者的异同？
*  同：三个类都是实现了List接口，存储数据的特点相同：存储有序的、可重复的数据
*  不同：见上

```

### 3.2  新增方法

相比于Collection接口，List新增了带有index的操作

```
void add(int index, Object ele):在index位置插入ele元素
boolean addAll(int index, Collection eles):从index位置开始将eles中的所有元素添加进来
Object get(int index):获取指定index位置的元素
int indexOf(Object obj):返回obj在集合中首次出现的位置
int lastIndexOf(Object obj):返回obj在当前集合中末次出现的位置
Object remove(int index):移除指定index位置的元素，并返回此元素
Object set(int index, Object ele):设置指定index位置的元素为ele
List subList(int fromIndex, int toIndex):返回从fromIndex到toIndex位置的子集合
```

```java
        ArrayList list = new ArrayList();
        list.add(123);
        list.add(456);
        list.add("AA");
        list.add(new Person("Tom",12));
        list.add(456);
        //int indexOf(Object obj):返回obj在集合中首次出现的位置。如果不存在，返回-1.
        int index = list.indexOf(4567);
        System.out.println(index);

        //int lastIndexOf(Object obj):返回obj在当前集合中末次出现的位置。如果不存在，返回-1.
        System.out.println(list.lastIndexOf(456));

        //Object remove(int index):移除指定index位置的元素，并返回此元素
        Object obj = list.remove(0);
        System.out.println(obj);
        System.out.println(list);

        //Object set(int index, Object ele):设置指定index位置的元素为ele
        list.set(1,"CC");
        System.out.println(list);

        //List subList(int fromIndex, int toIndex):返回从fromIndex到toIndex位置的左闭右开区间的子集合
        List subList = list.subList(2, 4);
        System.out.println(subList);
        System.out.println(list);

-1
4
123
[456, AA, Person{name='Tom', age=12}, 456]
[456, CC, Person{name='Tom', age=12}, 456]
[Person{name='Tom', age=12}, 456]
[456, CC, Person{name='Tom', age=12}, 456]

Process finished with exit code 0
```

```java
        ArrayList list = new ArrayList();
        list.add(123);
        list.add(456);
        list.add("AA");
        list.add(new Person("Tom",12));
        list.add(456);

        System.out.println(list);

        //void add(int index, Object ele):在index位置插入ele元素
        list.add(1,"BB");
        System.out.println(list);

        //boolean addAll(int index, Collection eles):从index位置开始将eles中的所有元素添加进来
        List list1 = Arrays.asList(1, 2, 3);
        list.addAll(list1);
//        list.add(list1);
        System.out.println(list.size());//9

        //Object get(int index):获取指定index位置的元素
        System.out.println(list.get(0)); //123
```

### 3.4 循环

```java
ArrayList list = new ArrayList();
list.add(123);
list.add(456);
list.add("AA");

//方式一：Iterator迭代器方式
 iterator = list.iterator();
while(iterator.hasNext()){
    System.out.println(iterator.next());
}

System.out.println("***************");

//方式二：增强for循环
for(Object obj : list){
    System.out.println(obj);
}

System.out.println("***************");

//方式三：普通for循环
for(int i = 0;i < list.size();i++){
    System.out.println(list.get(i));
}
```

### 3.5 总结

```
增：add(Object obj)
删：remove(Object obj) / remove(int index)
改：set(int index, Object ele)
查：get(int index)
插：add(int index, Object ele)
长度：size()
遍历：① Iterator迭代器方式
     ② 增强for循环
     ③ 普通的循环
```

### 3.6  remove(Object obj) / remove(int index)

```java
    public void testListRemove() {
        List list = new ArrayList();
        list.add(1);
        list.add(2);
        list.add(3);
        updateList(list);
        System.out.println(list);//[1, 2]
    }

    private void updateList(List list) {
        list.remove(2); // 方法重载，remove(int index)
//        list.remove(new Integer(2)); [1, 3]
    }
```

## 4 Set

### 4.1 简绍

set接口没有提供额外的方法  

```
一、Set：存储无序的、不可重复的数据
以HashSet为例说明：
1. 无序性：不等于随机性。存储的数据在底层数组中并非按照数组索引的顺序添加，而是根据数据的哈希值决定的。即存的时候按照散列函数求得的值在底层数组中进行存储，取的时候顺序一样。

2. 不可重复性：保证添加的元素按照equals()判断时，不能返回true.即：相同的元素只能添加一个。

二、添加元素的过程：以HashSet为例：
    我们向HashSet中添加元素a,首先调用元素a所在类的hashCode()方法，计算元素a的哈希值，
    此哈希值接着通过某种算法计算出在HashSet底层数组中的存放位置（即为：索引位置），判断
    数组此位置上是否已经有元素：
        如果此位置上没有其他元素，则元素a添加成功。 --->情况1
        如果此位置上有其他元素b(或以链表形式存在的多个元素），则比较元素a与元素b的hash值：
            如果hash值不相同，则元素a添加成功。--->情况2
            如果hash值相同，进而需要调用元素a所在类的equals()方法：
                   equals()返回true,元素a添加失败
                   equals()返回false,则元素a添加成功。--->情况2

    对于添加成功的情况2和情况3而言：元素a 与已经存在指定索引位置上数据以链表的方式存储。
    jdk 7 :元素a放到数组中，指向原来的元素。
    jdk 8 :原来的元素在数组中，指向元素a
    总结：七上八下

    HashSet底层：数组+链表的结构。
```

### 4.2 HashSet

- 不能保证元素的排列顺序

- HashSet 不是线程安全的

- 集合元素可以是 null  

```
        Set set = new HashSet();
        set.add(456);
        set.add(123);
        set.add(123);
        set.add("AA");
        set.add("CC");
        //
        set.add(new User("Tom",12));
        set.add(new User("Tom",12));
        set.add(129);

        Iterator iterator = set.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
        /*
        AA
        CC
        User{name='Tom', age=12}
        129
        456
        123
        User{name='Tom', age=12}
         */
```

### 4.3 LinkedSet

- LinkedHashSet作为HashSet的子类，在添加数据的同时，每个数据还维护了两个引用，记录此数据前一个数据和后一个数据。
- 优点：对于频繁的遍历操作，LinkedHashSet效率高于HashSet

```java
    public void test2(){
        Set set = new LinkedHashSet();
        set.add(456);
        set.add(123);
        set.add(123);
        set.add("AA");
        set.add("CC");
        set.add(new User("Tom",12));
        set.add(new User("Tom",12));
        set.add(129);

        Iterator iterator = set.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
//        456
//        123
//        AA
//        CC
//        User{name='Tom', age=12}
//        User{name='Tom', age=12}
//        129
```

### 4.4 方法重写

重写User的equals方法和hashCode() 方法

```
    @Override
    public boolean equals(Object o) {
        System.out.println("User equals()....");
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        User user = (User) o;

        if (age != user.age) return false;
        return name != null ? name.equals(user.name) : user.name == null;
    }
//
    @Override
    public int hashCode() { //return name.hashCode() + age;
        System.out.println("User hashCode()....");
        int result = name != null ? name.hashCode() : 0;
        result = 31 * result + age;
        return result;
    }
```

```java
        Set set = new LinkedHashSet();
        set.add(456);
        set.add(123);
        set.add(123);
        set.add("AA");
        set.add("CC");
        set.add(new User("Tom",12));
        set.add(new User("Tom",12));
        set.add(129);

        Iterator iterator = set.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
//        User hashCode()....
//        User hashCode()....
//        User equals()....
//        456
//        123
//        AA
//        CC
//        User{name='Tom', age=12}
//        129
```

### 4.5 TreeSet

- TreeSet 是 SortedSet 接口的实现类， TreeSet 可以确保集合元素处于排序状态。
- TreeSet底层使用红黑树结构存储数据  

1.向TreeSet中添加的数据，要求是**相同类的对象**。
2.两种排序方式：自然排序（实现Comparable接口） 和 定制排序（Comparator）
3.**自然排序**中，比较两个对象是否相同的标准为：**compareTo()**返回0.不再是equals().
4.**定制排序**中，比较两个对象是否相同的标准为：**compare()**返回0.不再是equals().

- 向TreeSet中添加的数据，要求是**相同类的对象**。

```java
        TreeSet set = new TreeSet();

        //失败：不能添加不同类的对象
        set.add(123);
        set.add(456);
        set.add("AA");
        set.add(new User("Tom",12)); //ClassCastException
```

- 集合元素处于排序状态, 默认以升序排列

```java
		TreeSet set = new TreeSet();
        set.add(34);
        set.add(-34);
        set.add(43);
        set.add(11);
        set.add(8);

        Iterator iterator = set.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }

//        -34
//        8
//        11
//        34
//        43
```

### 4.6 面试题

#### 4.6.1 在List内去除重复数字值，要求尽量简单  

```
public static void main(String[] args) {
    List list = new ArrayList();
    list.add(new Integer(1));
    list.add(new Integer(2));
    list.add(new Integer(2));
    list.add(new Integer(4));
    list.add(new Integer(4));
    List list2 = duplicateList(list);

    Iterator iterator = list2.iterator();
    while (iterator.hasNext()){
        System.out.println(iterator.next());
    }

}

private static List duplicateList(List list) {
    Collection<List> coll = new HashSet<>();
    coll.addAll(list);
    return new ArrayList(coll);
}
```

#### 4.6.2 add

```java
public void test3(){
        HashSet set = new HashSet();
        Person p1 = new Person(1001,"AA");
        Person p2 = new Person(1002,"BB");

        set.add(p1);
        set.add(p2);
//        System.out.println(set);
//        [Person{id=1002, name='BB'}, Person{id=1001, name='AA'}]

        p1.name = "CC";
        set.remove(p1); // p1的内容发生了变化，其返回的hash值也将发生变化
        System.out.println(set);
//        [Person{id=1002, name='BB'}, Person{id=1001, name='CC'}]
//        删除时先判断Set中是否存在p1，该过程就要调用hashCode(),equals()方法，
//        由于改变p1中的值，hashCode()返回的值发生了变化，所以认为更改后的p1在原set中不存在，所以不删除


        set.add(new Person(1001,"CC"));
        System.out.println(set);
//        [Person{id=1002, name='BB'}, Person{id=1001, name='CC'}, Person{id=1001, name='CC'}]
//        set中存储new Person(1001,"AA")的hash值，并没有存放new Person(1001,"CC")的hash值

        set.add(new Person(1001,"AA"));
        System.out.println(set);
//        [Person{id=1002, name='BB'}, Person{id=1001, name='CC'}, Person{id=1001, name='CC'}]
//        先判断hash值，与原来的set中想同，再判断值是否相同，原set中存储的是Person{id=1001, name='CC'}，内容不同，可以添加
    }
```

## 5 Map

- Map 中的 key 和 value 都可以是任何引用类型的数据

-  Map 中的 **key 用Set来存放，不允许重复**，即同一个 Map 对象所对应的类，须重写hashCode()和equals()方法  ,value可以重复
- **key ------ Set**
- **value-------Collection**

HashMap可以存放null的key和value

```java
    @Test
    public void test1(){
        Map map = new HashMap();
//        Map map = new Hashtable(); // NullPointerException
        map.put(null,123);
        System.out.println(map);
        map.put(null,null);
        System.out.println(map);
    }
// {null=123}
// {null=null}
```

### 5.1Map的实现类的结构：

```
*  |----Map:双列数据，存储key-value对的数据   ---类似于高中的函数：y = f(x)
*         |----HashMap:作为Map的主要实现类；线程不安全的，效率高；存储null的key和value
*              |----LinkedHashMap:保证在遍历map元素时，可以按照添加的顺序实现遍历。
*                      原因：在原有的HashMap底层结构基础上，添加了一对指针，指向前一个和后一个元素。
*                      对于频繁的遍历操作，此类执行效率高于HashMap。
*         |----TreeMap:保证按照添加的key-value对进行排序，实现排序遍历。此时考虑key的自然排序或定制排序
*                      底层使用红黑树
*         |----Hashtable:作为古老的实现类；线程安全的，效率低；不能存储null的key和value
*              |----Properties:常用来处理配置文件。key和value都是String类型
*
*
*      HashMap的底层：数组+链表  （jdk7及之前）
*                    数组+链表+红黑树 （jdk 8）
*
*
*  面试题：
*  1. HashMap的底层实现原理？
*  2. HashMap 和 Hashtable的异同？
*  3. CurrentHashMap 与 Hashtable的异同？（暂时不讲）
```

### 5.2 Map结构的理解

```
*  二、Map结构的理解：
*    Map中的key:无序的、不可重复的，使用Set存储所有的key  ---> key所在的类要重写equals()和hashCode() （以HashMap为例）
*    Map中的value:无序的、可重复的，使用Collection存储所有的value --->value所在的类要重写equals()
*    一个键值对：key-value构成了一个Entry对象。
*    Map中的entry:无序的、不可重复的，使用Set存储所有的entry
*
```

### 5.3 HashMap的底层实现原理

```
* HashMap的底层实现原理？以jdk7为例说明：
*      HashMap map = new HashMap():
*      在实例化以后，底层创建了长度是16的一维数组Entry[] table。
*      ...可能已经执行过多次put...
*      map.put(key1,value1):
*      首先，调用key1所在类的hashCode()计算key1哈希值，此哈希值经过某种算法计算以后，得到在Entry数组中的存放位置。
*      如果此位置上的数据为空，此时的key1-value1添加成功。 ----情况1
*      如果此位置上的数据不为空，(意味着此位置上存在一个或多个数据(以链表形式存在)),比较key1和已经存在的一个或多个数据
*      的哈希值：
*              如果key1的哈希值与已经存在的数据的哈希值都不相同，此时key1-value1添加成功。----情况2
*              如果key1的哈希值和已经存在的某一个数据(key2-value2)的哈希值相同，继续比较：调用key1所在类的equals(key2)方法，比较：
*                      如果equals()返回false:此时key1-value1添加成功。----情况3
*                      如果equals()返回true:使用value1替换value2。
*
*       补充：关于情况2和情况3：此时key1-value1和原来的数据以链表的方式存储。
*
*      在不断的添加过程中，会涉及到扩容问题，当超出临界值(且要存放的位置非空)时，扩容。默认的扩容方式：扩容为原来容量的2倍，并将原有的数据复制过来。
*
*      jdk8 相较于jdk7在底层实现方面的不同：
*      1. new HashMap():底层没有创建一个长度为16的数组
*      2. jdk 8底层的数组是：Node[],而非Entry[]
*      3. 首次调用put()方法时，底层创建长度为16的数组
*      4. jdk7底层结构只有：数组+链表。jdk8中底层结构：数组+链表+红黑树。
*         4.1 形成链表时，七上八下（jdk7:新的元素指向旧的元素。jdk8：旧的元素指向新的元素）
          4.2 当数组的某一个索引位置上的元素以链表形式存在的数据个数 > 8 且当前数组的长度 > 64时，此时此索引位置上的所数据改为使用红黑树存储。
*
*      DEFAULT_INITIAL_CAPACITY : HashMap的默认容量，16
*      DEFAULT_LOAD_FACTOR：HashMap的默认加载因子：0.75
*      threshold：扩容的临界值，=容量*填充因子：16 * 0.75 => 12
*      TREEIFY_THRESHOLD：Bucket中链表长度大于该默认值，转化为红黑树:8
*      MIN_TREEIFY_CAPACITY：桶中的Node被树化时最小的hash表容量:64
```

### 5.4 LinkedHashMap的底层实现原理

```
 *  四、LinkedHashMap的底层实现原理（了解）
 *      源码中：
 *      static class Entry<K,V> extends HashMap.Node<K,V> {
             Entry<K,V> before, after;//能够记录添加的元素的先后顺序
             Entry(int hash, K key, V value, Node<K,V> next) {
                super(hash, key, value, next);
             }
         }
```

### 5.5 Map中定义的方法

```
 添加、删除、修改操作：
 Object put(Object key,Object value)：将指定key-value添加到(或修改)当前map对象中
 void putAll(Map m):将m中的所有key-value对存放到当前map中
 Object remove(Object key)：移除指定key的key-value对，并返回value
 void clear()：清空当前map中的所有数据
 元素查询的操作：
 Object get(Object key)：获取指定key对应的value
 boolean containsKey(Object key)：是否包含指定的key
 boolean containsValue(Object value)：是否包含指定的value
 int size()：返回map中key-value对的个数
 boolean isEmpty()：判断当前map是否为空
 boolean equals(Object obj)：判断当前map和参数对象obj是否相等
 元视图操作的方法：
 Set keySet()：返回所有key构成的Set集合
 Collection values()：返回所有value构成的Collection集合
 Set entrySet()：返回所有key-value对构成的Set集合
```

#### 5.5.1 添加、删除、修改操作

```
   public void test3(){
        Map map = new HashMap();
        //添加
        map.put("AA",123);
        map.put(45,123);
        map.put("BB",56);
        //修改
        map.put("AA",87);

        System.out.println(map);
//        {AA=87, BB=56, 45=123}

        Map map1 = new HashMap();
        map1.put("CC",123);
        map1.put("DD",123);

        map.putAll(map1);
        System.out.println(map);
//        {AA=87, BB=56, CC=123, DD=123, 45=123}

        //remove(Object key)
        Object value = map.remove("CC");
        System.out.println(value);
//        123
        System.out.println(map);
//        {AA=87, BB=56, DD=123, 45=123}

        //clear()
        map.clear();//与map = null操作不同
        System.out.println(map.size()); // 0
        System.out.println(map);
//        {}
    }
```

#### 5.5.2 元素查询

```java
    public void test4(){
        Map map = new HashMap();
        map.put("AA",123);
        map.put(45,123);
        map.put("BB",56);

        // Object get(Object key)
        System.out.println(map.get(45)); //123

        //containsKey(Object key)
        boolean isExist = map.containsKey("BB");
        System.out.println(isExist); // true

        isExist = map.containsValue(123);
        System.out.println(isExist); // true

        map.clear();

        System.out.println(map.isEmpty()); //true
    }
```

#### 5.5.3 元视图操作

- Set keySet()：返回所有key构成的Set集合
- Collection values()：返回所有value构成的Collection集合
- Set entrySet()：返回所有key-value对构成的Set集合

```java
    @Test
    public void test5(){
        Map map = new HashMap();
        map.put("AA",123);
        map.put(45,1234);
        map.put("BB",56);

        //遍历所有的key集：keySet()
        Set set = map.keySet();
            Iterator iterator = set.iterator();
            while(iterator.hasNext()){
                System.out.println(iterator.next());
        }
        System.out.println();

        //遍历所有的value集：values()
        Collection values = map.values();
        for(Object obj : values){
            System.out.println(obj);
        }
        System.out.println();

        //遍历所有的key-value
        //方式一：entrySet()
        Set entrySet = map.entrySet();
        Iterator iterator1 = entrySet.iterator();
        while (iterator1.hasNext()){
            Object obj = iterator1.next();
            //entrySet集合中的元素都是entry
            Map.Entry entry = (Map.Entry) obj;
            System.out.println(entry.getKey() + "---->" + entry.getValue());
        }
        System.out.println();

        //方式二：
        Set keySet = map.keySet();
        Iterator iterator2 = keySet.iterator();
        while(iterator2.hasNext()){
            Object key = iterator2.next();
            Object value = map.get(key);
            System.out.println(key + "=====" + value);
        }

    }
```

####  5.5.4 总结：常用方法

 * 添加：put(Object key,Object value)
 * 删除：remove(Object key)
 * 修改：put(Object key,Object value)
 * 查询：get(Object key)
 * 长度：size()
 * 遍历：keySet() / values() / entrySet()

### 5.6 TreeMap

## 6 Collections工具类  

- Collections 是一个操作 **Set、 List 和 Map** 等集合的工具类
- Collections 中提供了一系列静态的方法对集合元素进行排序、查询和修改等操作，还提供了对集合对象设置不可变、对集合对象实现同步控制等方法
- 排序操作： （均为static方法）
  reverse(List)： 反转 List 中元素的顺序
  shuffle(List)： 对 List 集合元素进行随机排序
  sort(List)： 根据元素的自然顺序对指定 List 集合元素按升序排序
  sort(List， Comparator)： 根据指定的 Comparator 产生的顺序对 List 集合元素进行排序
  swap(List， int， int)： 将指定 list 集合中的 i 处元素和 j 处元素进行交换  

ps: 操作数组的工具类： Arrays  

```
reverse(List)：反转 List 中元素的顺序
shuffle(List)：对 List 集合元素进行随机排序
sort(List)：根据元素的自然顺序对指定 List 集合元素按升序排序
sort(List，Comparator)：根据指定的 Comparator 产生的顺序对 List 集合元素进行排序
swap(List，int， int)：将指定 list 集合中的 i 处元素和 j 处元素进行交换

Object max(Collection)：根据元素的自然顺序，返回给定集合中的最大元素
Object max(Collection，Comparator)：根据 Comparator 指定的顺序，返回给定集合中的最大元素
Object min(Collection)
Object min(Collection，Comparator)
int frequency(Collection，Object)：返回指定集合中指定元素的出现次数
void copy(List dest,List src)：将src中的内容复制到dest中
boolean replaceAll(List list，Object oldVal，Object newVal)：使用新值替换 List 对象的所有旧值
```

```java
public void test2(){
        List list = new ArrayList();
        list.add(123);
        list.add(43);
        list.add(765);
        list.add(-97);
        list.add(0);

        //报异常：IndexOutOfBoundsException("Source does not fit in dest")
//        List dest = new ArrayList(list.size()); // 指定底层数组容量长度，并非当前List的长度size。
//        System.out.println(dest.size()); // 0
//        Collections.copy(dest,list);

        //正确的：
        List dest = Arrays.asList(new Object[list.size()]);
        System.out.println(dest.size());//list.size();
        Collections.copy(dest,list);

        System.out.println(dest);


        /*
        Collections 类中提供了多个 synchronizedXxx() 方法，
        该方法可使将指定集合包装成线程同步的集合，从而可以解决
        多线程并发访问集合时的线程安全问题

         */
        //返回的list1即为线程安全的List
        List list1 = Collections.synchronizedList(list);

    }
```

