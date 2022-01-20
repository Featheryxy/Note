# 1 Java比较器

- 在Java中经常会涉及到对象数组的排序问题，那么就涉及到**对象之间**
  **的比较**问题。
- Java实现对象排序的方式有两种：
  - 自然排序： java.lang.Comparable
  - 定制排序： java.util.Comparator  

## 2 自然排序  

### 2.1 介绍

- Comparable接口强行对**实现它的每个类的对象**进行整体排序。这种排序被称为类的自然排序  

- 实现 Comparable 的类必须实现 compareTo(Object obj) 方法，两个对象即通过 compareTo(Object obj) 方法的返回值来比较大小。 

  - 如果当前对象this大于形参对象obj， 则返回正整数，
  - 如果当前对象this小于形参对象obj， 则返回负整数，
  - 如果当前对象this等于形参对象obj， 则返回零。  

- Comparable 的典型实现： (默认都是**从小到大排列**的)，以下类型已经继承了Comparable接口,可直接使用

  - String：按照字符串中字符的Unicode值进行比较

  - Character：按照字符的Unicode值来进行比较

  - 数值类型对应的包装类以及BigInteger、 BigDecimal：按照它们对应的数值大小进行比较

  - Boolean： true 对应的包装类实例大于 false 对应的包装类实例

  - Date、 Time等：后面的日期时间比前面的日期时间大  

```java
    public final class String implements Serializable, Comparable<String>, CharSequence {
      ....
    }
```

```java
      public void test1(){
          String[] arr = new String[]{"AA","CC","KK","MM","GG","JJ","DD"};
          //
          Arrays.sort(arr);
  
          System.out.println(Arrays.toString(arr));
  //          [AA, CC, DD, GG, JJ, KK, MM]
      }
```

  ### 2.1 重写compareTo方法

**Goods.java**

```java
public class Goods implements  Comparable{

    private String name;
    private double price;
        //指明商品比较大小的方式:按照价格从低到高排序,再按照产品名称从高到低排序
    @Override
    public int compareTo(Object o) {
        if(o instanceof Goods){
            Goods goods = (Goods)o;
            if(this.price > goods.price){
//                System.out.println(this.price+"---"+goods.price+"---1");
                return 1;
            }else if(this.price < goods.price){
                System.out.println(this.price+"---"+goods.price+"--- -1");
                return -1;
            }else{
                // 二级排序,String默认从低到高排序，添加“ - ”号，从高到低排序
                System.out.println(this.price+"---"+goods.price+"---0");
                return -this.name.compareTo(goods.name);
//                return 0;
            }
        }else {
            throw new RuntimeException("传入的数据类型不一致");
        }
    }
}

```

```java
    @Test
    public void test2(){
        Goods[] arr = new Goods[5];
        arr[0] = new Goods("lenovoMouse",34);
        arr[1] = new Goods("dellMouse",43);
        arr[2] = new Goods("xiaomiMouse",12);
        arr[3] = new Goods("huaweiMouse",65);
        arr[4] = new Goods("microsoftMouse",43);

        Arrays.sort(arr);

        System.out.println(Arrays.toString(arr));
//        [Goods{name='xiaomiMouse', price=12.0}, 
//        Goods{name='lenovoMouse', price=34.0}, 
//        Goods{name='microsoftMouse', price=43.0}, 
//        Goods{name='dellMouse', price=43.0}, 
//        Goods{name='huaweiMouse', price=65.0}]
    }
```

## 3 定制排序

### 3.1 介绍

- 可以**将 Comparator 传递给 sort 方法**（如 Collections.sort 或 Arrays.sort），从而允许在排序顺序上实现精确控制。
-  还可以使用 Comparator 来控制某些数据结构（如有序 set或有序映射）的顺序，或者为那些没有自然顺序的对象 collection 提供排序。  

Comparator接口的使用：定制排序

- 背景
  当**元素的类型没有实现java.lang.Comparable接口而又不方便修改代码**，或者**实现了java.lang.Comparable接口的排序规则不适合当前的操作**，那么可以考虑使用 Comparator 的对象来排序

### 3.2 .重写compare()方法

重写compare(Object o1,Object o2)方法，比较o1和o2的大小：

- 如果方法返回正整数，则表示o1大于o2；
- 如果返回0，表示相等；
- 返回负整数，表示o1小于o2。

```java
    @Test
    public void copy_test3(){
        String[] arr = new String[]{"AA","CC","KK","MM","GG","JJ","DD"};
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s, String t1) {
                return -s.compareTo(t1);
            }
        });
        System.out.println(Arrays.toString(arr));
//      [MM, KK, JJ, GG, DD, CC, AA]
    }
```

```java
    @Test
    public void copy_test4(){
        Goods[] arr = new Goods[6];
        arr[0] = new Goods("lenovoMouse",34);
        arr[1] = new Goods("dellMouse",43);
        arr[2] = new Goods("xiaomiMouse",12);
        arr[3] = new Goods("huaweiMouse",65);
        arr[4] = new Goods("huaweiMouse",224);
        arr[5] = new Goods("microsoftMouse",43);

        Arrays.sort(arr, new Comparator<Goods>() {
            @Override
            public int compare(Goods goods, Goods t1) {
                //指明商品比较大小的方式:按照产品名称从低到高排序,再按照价格从高到低排序
                // String 类型的equals重写了Object的equals方法
                if (goods.getName().equals(t1.getName())){
                    return -Double.compare(goods.getPrice(), t1.getPrice());
                }else{
                    return goods.getName().compareTo(t1.getName());
                }
            }
        });
        System.out.println(Arrays.toString(arr));
//        [Goods{name='dellMouse', price=43.0},
//        Goods{name='huaweiMouse', price=224.0},
//        Goods{name='huaweiMouse', price=65.0}, 
//        Goods{name='lenovoMouse', price=34.0}, 
//        Goods{name='microsoftMouse', price=43.0}, 
//        Goods{name='xiaomiMouse', price=12.0}]
    }
```