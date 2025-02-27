## 解题思想

算法 = 数据结构 + 控制结构 

看到一个题先读懂，然后思考用什么数据结构。

如果正向求解比较麻烦，可以使用逆向思维

## 解题过程

算法 = 数据结构+控制结构

1. 检验算法输入
2. 参数初始化
3. 确定**遍历的次数**(for)，或**停止的条件**(while)
4. 循环体：执行判断语句，标志判断
5. 循环体：执行操作
6. 返回



### while，for

循环不变量：在循环的过程中保持不变的性质, 可以用于证明算法的正确性

> 循环不变量是一个断言，在初始化，保持，终止这三个阶段都为真时，则循环正确
>
> 初始化：循环的第一次迭代之前，它为真
>
> 保持：循环的某次迭代之前它为真，那么下次迭代之前它仍为真
>
> 终止：在循环终止时，



- for ：知道要**循环的次数**时使用，且**查找方向是固定**的场景，如数组。 
  - 可以当做一个指针来使用
- while：知道**循环停止的时机**时使用，可以改变查找方向 

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



## 序列

一组按**特定顺序排列**的元素。每个元素在序列中都有一个**确定的位置**（或索引），并且序列通常具有**一定的长度**。序列是很多数据结构的基础概念之一，它可以表示为**线性结构或有序集合** 

1. 数组（Array） ：长度固定，元素按索引排列，可以通过索引访问
2. 链表（LinkedList） ：通过节点连接起来的序列 
3. 字符串（String）： 元素是字符，并且通常是不可变的 
4. 栈（Stack）后进先出（LIFO）
5. 队列（Queue）：先进先出（FIFO）
6.  动态数组（如 ArrayList）：与普通数组不同，动态数组能够根据需要扩展大小 



区间 nums[left...right]的长度  = right-left +1

区间 nums[left...right)的长度  = right-left 



## 循环/搜索

**线性搜索**：无序数据，效率不高

**二分搜索**：有序数据，效率较高。

**图的搜索算法（DFS、BFS）**：适用于图或树的遍历和路径查找。

**哈希表**：适用于需要快速查找的数据，通常是 O(1)O(1)O(1) 时间复杂度。

**字符串匹配（KMP）**：用于高效的字符串搜索。



1. 一个指针，分阶段多次循环
2. 每个循环中的语义尽量简短
3. 



### 循环方向-一维数组

```
// 正序
for(int i=0; i<arr.length; i++) {
    
}

// 倒序
for(int i=arr.length-1; i>=0; i--) {
    
}
```

### 循环方向-二维数组

```
		int len = matrix.length;
        // 行不变，遍历列。先遍历行，再遍历列
        for (int row = 0; row < len; row++) {
            for (int col = 0; col < len; col++) {
                int tem = matrix[row][col];
                System.out.println(tem);
            }
        }

        //  列不变，遍历行。先遍历列，再遍历行
        for (int col = 0; col < len; col++) {
            for (int row = 0; row < len; row++) {
                int tem = matrix[row][col];
                System.out.println(tem);
            }
        }
        
        // 行不变，遍历列，列的起始点为对角线上的下一列。i.e.:遍历数组右上角
        for(int i=0; i<len; i++){
            for(int j=i+1; j<len; j++){
         
         
         // 九宫格的
         for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                Set<Character> set = new HashSet<>();
                for (int x = 0; x < 3; x++) {
                    for (int y = 0; y < 3; y++) {     
```





## 指针

指针作用

1：搜索满足条件的元素，

2：维护数组下标

快慢指针: 一般情况下，慢指针维护了[0, r]位满足条件的区间， 快指针使用for循环用来遍历整个数组，寻找满足条件的元素

- 快指针：可以使用`for(int j=0; j<nums.length; j++)`循环
- 慢指针：`int i=0` 当满足条件时，移动指针, **注意慢指针是先更新数据还是先移动指针** 

滑动窗口：维护一个满足条件的窗口, 题目中通常会出现**连续**两个字，如连续子数组，连续字符串等。

指针碰撞：从两端向中间移动，当指针碰撞时停止循环

## 数组

二分查找前提：数组有序，数组中无重复元素

int mid = left + (right - left) / 2;  // 防止int溢出 

index + 1 = len  



arr\[i]\[j\]  ,  第i行，第j列，第四象限代表二维数组 

```java

 System.arraycopy(nums2, 0, nums1, 0, j + 1);
 System.arraycopy(Object src, int srcPos, Object dest, int destPos,int length)
```

## 二叉树

```
二叉树递归时，一个节点会被访问三次，分别时第一次进入节点A时，遍历节点A的左子树后，遍历节点A的右子树后。
如果是先根遍历，则在第一次进入节点时就收集结果
中根遍历时，遍历节点A的左子树后收集结果

		 1
	2		  3
null null   null null
dfs(root){
    if(root == null) return;
    // dosomething
}
遍历时，如果树的高度为n，则最大的递归深度为n+1，i.e.:调用 dfs方法共n+1次。因为要遍历到空节点才返回。 如上图的树，其高度为2，最大的递归深度为3，我们调用dfs方法次数为3。
优先看叶子节点, 如叶子节点2，它的左右节点都为空，

```

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



##  TreeSet

 默认正序，可以用`Collections.reverse(treeSet)`倒序



## Map

 * 添加：put(Object key,Object value)
 * 删除：remove(Object key)
 * 修改：put(Object key,Object value)
 * 查询：get(Object key)
 * 长度：size()
 * 遍历：keySet() / values() / entrySet()
 * 包含：**containsKey(Object key)，containsValue(Object value)**
 * 常用：**getOrDefault(Object key， 0)**

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

// 删除此堆栈顶部的对象，并将该对象作为此函数的值返回。栈为空时报错
stack.pop();

stack.isEmpty();
```

## ArrayDeque

```
动态数组：ArrayDeque 使用动态数组作为底层数据结构，可以根据需要自动扩展大小。
双端操作：支持从队列的两端进行操作（即插入、删除元素）。
性能：相较于 LinkedList，ArrayDeque 在某些操作上（如访问元素、在两端插入和删除元素）通常更高效。
不允许空元素：不能向 ArrayDeque 中添加 null 元素，如果尝试添加 null，将抛出 NullPointerException。
线程不安全：ArrayDeque 是非线程安全的。如果需要线程安全的队列，可以使用 Collections.synchronizedDeque() 包装 ArrayDeque。

添加元素：

addFirst(E e)：将元素添加到队列的头部。
addLast(E e)：将元素添加到队列的尾部。
offerFirst(E e)：将元素添加到队列的头部（如果添加成功，返回 true；否则返回 false）。
offerLast(E e)：将元素添加到队列的尾部（如果添加成功，返回 true；否则返回 false）。
删除元素：

removeFirst()：移除并返回队列头部的元素。如果队列为空，将抛出 NoSuchElementException。
removeLast()：移除并返回队列尾部的元素。如果队列为空，将抛出 NoSuchElementException。
pollFirst()：移除并返回队列头部的元素，如果队列为空，返回 null。
pollLast()：移除并返回队列尾部的元素，如果队列为空，返回 null。
访问元素：

getFirst()：获取队列头部的元素（不移除）。
getLast()：获取队列尾部的元素（不移除）。
peekFirst()：获取队列头部的元素（不移除），如果队列为空，返回 null。
peekLast()：获取队列尾部的元素（不移除），如果队列为空，返回 null。
```



## String

子串：一个字符串的子串是该字符串中任意一个字符或一段字符连续出现的序列 

> 例如，在字符串 "Hello World" 中，"H"、"e"、"l"、"o"、"W"、"o"、"r"、"l"、"d"，以及 "Hello"、"World"、"o Wor"、"lo W"、"ld" 等都是其子串 

索引+1 = 长度

```java
str.lastIndexOf(int index);
str.subString(int begIndex);
str.subString(int begIndex, int endIndex);
str.contains(String s);

String.format("%-4d", 99); // 99空格空格
String.format("%04d", 99); // 0099

str.matches(String regx); // 完全匹配

Pattern pat = Pattern.compile(String regx);
boolean pat.matcher(str).find(); // 只要能匹配到就能返回true;

// 循环中substring的用法
for (int i = 0; i < len; i++)
    for (int j = i + 1; j <= len; j++) {
        String test = s.substring(i, j);
    }
}

for (int i = 0; i < len; i++)
    for (int j = i + 1; j < len; j++) {
        String test = arr[];
    }
}
```




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
- str.charAt(int index)

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

## Collections

```java
Collection.min(List lis);
Collection.sort(List lis);
Collection.reverse(List lis);

```

## Char

```
Ascii
48 0 11000_b
57 9 
65 A
97 a


A与a 相差32（二进制：100000）
char2int:
int tmp = '9'-'0'; // tmp = 9

```

## Swap

```java
int a = 1;
int b = 2;
int tmp = 0;

public void static swap1(){
    int tmp = a;
    int a = b;
    int b = tmp;
}

// a must be 'R' or 'B';
public static swap1(char a){
	retrun 'R'+'B'-a
}


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

  > n<< 1 等价于 n*2

- \>> 有符号右移动运算符：把”>>”左边的运算数的各二进位全部右移若干位，**>>** 右边的数字指定了移动的位数，如果值为负数，高位补1；值为正数，高位补1

  > n>>1  等价于 n/2

- \>>> 无符号右移， 无论正负，高位都补0

- (n>>2) & 1 取n的二进制的第2位（从右（最低位）向左（最高位）计数）



二进制下，0&0 = 1， 1&0  = 0， 1 & 1 = 1

- n & 1 === 1, 说明n的二进制最后一位是1, 表示奇数
- n & 1 === 0, 说明n的二进制最后一位是0, 表示偶数
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

