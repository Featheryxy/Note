## 解题过程

1. 检验算法输入
2. 参数初始化
3. 确定遍历的次数(for)，或停止的条件(while)
4. 循环体：执行判断语句，标志判断
5. 循环体：执行操作
6. 返回

## 指针

快慢指针

- 快指针：可以使用`for(int j=0; j<nums.length; j++)`循环
- 慢指针：`int i=0` 当满足条件时，移动指针

滑动窗口

指针碰撞

## Arrays

| 0    | method                                | 简述                                   |
| ---- | ------------------------------------- | -------------------------------------- |
| 1    | boolean equals(int[] a,int[] b)       | 判断两个数组是否相等。                 |
| 2    | String toString(int[] a)              | 输出数组信息。                         |
| 3    | void fill(int[] a,int val)            | 将指定值填充到数组之中。               |
| 4    | void sort(int[] a)                    | 对数组进行排序。                       |
| 5    | int binarySearch(int[] a,int key)     | 对排序后的数组进行二分法检索指定的值。 |
| 6    | copyOf(int[] original, int newLength) | copy数组                               |

```java
    public static void main(String[] args) {
        int [] arr = new int []{1,2,3};
        int[] copy = Arrays.copyOf(arr, 5);
        System.out.println(Arrays.toString(copy));
        // [1, 2, 3, 0, 0]
    }
```

## Collection

```
add(Object obj)
remove(Object obj)

size()
clear()
isEmpty()
contains(Object obj)
equals(Object obj)

addAll(Collection coll)
removeAll(Collection coll)
retainAll(Collection c)
containsAll(Collection c)
```

## List

```java
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

PS:  

1. Collection中只能对集合进行add和remove操作，而List还可以进行get和set操作
2. Collection中使用add(Object obj)，而Map中使用put(Object key,Object value)



## Map

 * 添加：put(Object key,Object value)
 * 删除：remove(Object key)
 * 修改：put(Object key,Object value)
 * 查询：get(Object key)
 * 长度：size()
 * 遍历：keySet() / values() / entrySet()
 * 包含：containsKey(Object key)，containsValue(Object value)

```java
for(Integer num: nums){
    Integer count = map.get(num);
    count = count == null? 1: ++count;
    map.put(num, count);
}

Map<String, Integer> map = new HashMap<>();
map.put("1", map.getOrDefault("1", 0)+1);
System.out.println(map);
// {1=1}
```

## Stack(Deprecated)

```
Stack<Character> stack = new Stack();

stack.push(ch);

// 查看此堆栈顶部的对象，而不从堆栈中删除它。
stack.peek();

// 删除此堆栈顶部的对象，并将该对象作为此函数的值返回。
stack.pop();

stack.isEmpty();
```

## ArrayDeque




## String2Basis

基本数据类型、包装类--->String类型

- 调用String重载的valueOf(Xxx xxx)

```java
int num1 = 10;

//方式1：连接运算
String str1 = num1 + "";
System.out.println(str1);

//方式2：调用String的valueOf(Xxx xxx)
float f1 = 12.3f;
String str2 = String.valueOf(f1);
System.out.println(str2); //"12.3"

Double d1 = new Double(12.4);
String str3 = String.valueOf(d1);
System.out.println(str3);//"12.4"
```

String类型 --->基本数据类型、包装类

- 调用包装类的`parseXxx(String s)`
- 调用包装类的`valueOf(String s)`

```java
String str1 = "123";
int num2 = Integer.parseInt(str1);
System.out.println(num2+1); // 124

String str2 = "true";
boolean b1 = Boolean.parseBoolean(str2);
System.out.println(b1); // true

String str3 = "true1";
boolean b2 = Boolean.parseBoolean(str3);
System.out.println(b2); // false
```

## String2Char

String ---> CharArray

- 调用String类的`toCharArray()`

```java
String str = "ABCD";
char[] chars = str.toCharArray();
System.out.println(chars[0]); // A

char a = str.charAt(0);
```

CharArray ---> String

- 掉用String类的构造函数

```java
char[] chars = new char[]{'a', 'b', 'c'};
String charStr = new String(chars);
System.out.println(charStr);
// abc
```

## Arr2List

Array ----> List

- `List list = Arrays.asList(arr)`,  `arr`一定为包装类型的数组, `List list = new ArrayList(list)` 
- `Collections.addAll(list, arr);`

List ---> Array

- `list.toArray()`

```java
    public static void main(String[] args) {
        List<Integer> integers = Arrays.asList(1, 2, 3);
        System.out.println(integers);
//        [1, 2, 3]

        Object[] objects = integers.toArray();
        for (Object object: objects){
            System.out.println(object);
        }
//        1
//        2
//        3
        System.out.println("+++++++++++++++++++++++++++++++");
        Integer [] arr = new Integer[]{1,2,3};
        ArrayList<Integer> list = new ArrayList<>(arr.length);
        Collections.addAll(list, arr);
        System.out.println(list.size());
//        3

        System.out.println("+++++++++++++++++++++++++++++++");
        Integer [] arr1 = new Integer[]{1,2,3};
        List<Integer> list1 = Arrays.asList(arr1);
        System.out.println(list1);
//        [1, 2, 3]
    }
```

```java
// Arrays.asList() 返回的是Arrays的内部类ArrayList， 而不是java.util.ArrayList
List<Integer> integers = Arrays.asList(1, 3, 3, 5, 7);
// Arrays的内部类ArrayList和java.util.ArrayList都继承了AbstractList中的remove、add等方法
// AbstractList中是默认throw UnsupportedOperationException而且不作任何操作。
// java.util.ArrayList重写了这些方法而Arrays的内部类ArrayList没有重新，所以会抛出异常。

// integers.remove(1); // UnsupportedOperationException

List list = new ArrayList(integers);
list.remove(0);
System.out.println(Arrays.toString(list.toArray()));
// [3, 3, 5, 7]

list.remove(new Integer(3)); // 只删除第一个
//             for (int index = 0; index < size; index++)
//                if (o.equals(elementData[index])) {
//                    fastRemove(index);
//                    return true;
//                }

System.out.println(Arrays.toString(list.toArray()));
// [3, 5, 7]
```

## 数字的处理

- 将数字转换成字符串进行处理
- 逐项操作

```
#　取个位数字
num % 10	

#　删除个位数字
num // 10	
int(num / 10)

# num 能被2整除
num % 2 == 0
```

## 数组

数组属性：位置，值，前后，组，排序

##  while，for

- for ：知道要**循环的次数**时使用
  - 可以当做一个指针来使用
- while：知道**循环停止的时机**时使用

```java
while(l<r && nums[r] == nums[--r]);

// 等价于

--r;
while(l<r && nums[r] == nums[r]){
	
}

// ----------------------------------------------------------
j = 0;
while(j<n){
    
    j++;
}

// 等价于
for(int j=0; j<n; j++){
    
} 
```

## if-else

- **使用if的时候一定要想到else.**

- if。if为真时，执行if子句

- if-else。if为假时，执行else子句，if-else中的语句中不能相同，如有相同，应放置在if-else语句块外。

```
if(true):
	return 
else 
	return 

# 等价于

if True:
	return 
return 
```



  ```
if True:
	a = 1
	c += 1
else:
	b = 2
	c += 1

# 等价于

if True:
	a = 1
else:
	b = 2
    
c += 1
  ```

- if-elif 。注重次序，只有一个子句执行

```
  if False:
  	print('if')
  else:
	if True:
  		print('elif')
  	else:
  		print('else')
  		
  # elif
```

- if-elif-else	当if子句和elif子句都为假时，执行else子句

- for-else 当for循环正常结束时（即不是通过break跳出结束的），会执行else中的语句

- 在循环中先执行判断语句

```java
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            if(set.contains(nums[i])) {
                return true;
            }
            set.add(nums[i]);
            if(set.size() > k) {
                set.remove(nums[i - k]);
            }
        }
        return false;
    }
}
```

## 常用函数

```java
 System.arraycopy(nums2, 0, nums1, 0, j + 1);
 System.arraycopy(Object src, int srcPos, Object dest, int destPos,int length)
```



## 表达式

- 考虑边界（带入思考）

  ```java
  // 当i=0或者i>0时，是否要执行
  if(i>=0){
  
  }
  ```

- 逻辑运算

  ```java
  // 当i>=0 并且 j>=0 时，继续执行
  // 当i<0 或者 j<0 时，跳出循环
  while(i>=0 && j>=0){
  	// suite
  }
  ```


## 运算符等级

高到低

- 括号，如 ( ) 和 [ ]
- 一元运算符，如 -、++、- -和 !
- 算术运算符，如 *、/、%、+ 和 -
- 关系运算符，如 >、>=、<、<=、== 和 !=
- 逻辑运算符，如 &、^、|、&&、||
- 条件运算符和赋值运算符，如 ? ：、=、*=、/=、+= 和 -=

## a++与++b

a++：先将a参与运算，最后再对a加1

++a：先对a进行加1，此时a = a+1, 再将a参与其他运算

```java
int a = 1;
System.out.println(a++); // 1
System.out.println(a); // 2

int b = 1;
System.out.println(++b); // 2
System.out.println(b); // 2

// -------------------------------------
int b=a++ + ++a-a--+a--;
// 2+2-3+2
System.out.println(a); // 1
System.out.println(b); // 3

a=a++ + (++a) - a-- + a--; /* 此时先运算++a ,a内存值为2 */
==>
a=(a++) + 2 - a-- + a--; /*此时先计算 取 a++ 到temp=2 然后 a内存值+1 为3 */
a=2+2 - (a)-- + a--; /此时取 a-- 到temp=3 然后 a内存值-1 为2*/
a=2+2-3 +(a--); 此时去 a-- 到temp=2 然后 a内存值 -1 为 1*/
a=2+2-3+2=3;

```



## 位运算

- << 左移动运算符：运算数的各二进位全部左移若干位，由 **<<** 右边的数字指定了移动的位数，高位丢弃，低位补0
- \>> 右移动运算符：把”>>”左边的运算数的各二进位全部右移若干位，**>>** 右边的数字指定了移动的位数

- n<< 1 等价于 n*2
- n>>1  等价于 n/2

## 与运算

二进制下，0&0 = 1， 1&0  = 0， 1 & 1 = 1

- n & 1 === 1, 说明n的二进制最后一位是1
- n & 1 === 0, 说明n的二进制最后一位是0
- 每执行一次x = x&(x-1)，会将x用二进制表示时**最右边的一个1变为0，**因为x-1将会将该位(x用二进制表示时最右边的一个1)变为0。

```java
     	System.out.println(Integer.toBinaryString(10));
        System.out.println(Integer.toBinaryString(9));
        System.out.println(10&9);
        System.out.println(Integer.toBinaryString(8));
        // 1010
        // 1001
        // 8
        // 1000
```

## Max

```java
// left = Math.max(map.get(tem)+1, left);
if(map.get(tem)+1 > left){
    left = map.get(tem)+1 ;
}
```

