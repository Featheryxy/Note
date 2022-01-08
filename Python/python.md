# python

## 一、 禅

- Beautiful is better than ugly.

  优美胜于丑陋（Python以编写优美的代码为目标）

- Explicit is better than implicit.

   明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似） 

- Simple is better than complex.

     简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现） 

- Complex is better than complicated.

   复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）

- Flat is better than nested.

  扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套） 

- Sparse is better than dense.

   间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）

- Readability counts.

  可读性很重要（优美的代码是可读的） 

- Special cases aren't special enough to break the rules.Although practicality beats purity.

   即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上） 

- Errors should never pass silently.Unless explicitly silenced.

   不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写except:pass风格的代码） 

- In the face of ambiguity, refuse the temptation to guess.

   当存在多种可能，不要尝试去猜测 

- There should be one-- and preferably only one --obvious way to do it.

   而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法） 

- Although that way may not be obvious at first unless you're Dutch.

   虽然这并不容易，因为你不是 Python 之父（这里的Dutch是指Guido） 

- Now is better than never.Although never is often better than *right* now.

   做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量） 

- If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.

  如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准） 

- Namespaces are one honking great idea -- let's do more of those!

   命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）

## 二、 简介

### 1. python 是脚本语言

​        脚本语言(Scripting language)是**电脑编程语言**，因此也能让开发者藉以编写出让电脑听命行事的程序。以简单的方式快速完成某些复杂的事情通常是创造脚本语言的重要原则，基于这项原则，使得脚本语言通常比 C语言、C++语言 或 Java 之类的**系统编程语言**要简单容易

### 2. python的特点

1. 一切皆为对象

2. 变量并不直接存储值，而只是引用一个内存地址

3. 使用缩进标识代码块

4. 标识符区分大小写

### 3. 代码构成

1. python程序由模块构成
2. 模块包含语句
3. 语句包含表达式（值+操作符，值）
4. 表达式建立并处理对象

### 4. 术语

- 模块：一个包含Python代码的文本文件
- 工厂函数：用于创建某种类型的新的数据项
- 方法（method）: 与类和实例有绑定关系的function
- 方法串链：从左向右读，对数据应用一组方法
- 函数（function）: 与类和实例无绑定关系的function
- 函数串链：从右向左读，对数据应用一组函数
- 列表推导：在一行上指定一个转换
- 分片：从一个列表访问多个列表项 list()[3: 6]
- 原地排序：排序转换后**替换** sort()
- 复制排序：排序转换后**返回** sorted()
- BIF(built-in functions) 内置函数
- suite 代码块
- PypI(Python Package Index) Python包索引
- exception 异常：因运行时错误而出现，会产生一个traceback

### 4. 小技巧

- 平方 **2

### 5. 变量命名规则

​	类名采用驼峰命名，即每个单词的首字母大写，不适用下划线

​	实例名，变量名，模块名采用小写，每个单词采用下划线连接

## 三、基础

### 1. 注释

- 单行注释 #
- 多行注释 \"""   **文档字符串**
  - object.\_\_doc\_\_ 得到一个对象的文档字符串.i.e.说明性文字的字符串

### 2. 赋值

- +=   可用于字符串和列表的连接

- -=

- *=   可用于字符串和列表的复制

- /=

- %=


```
序列赋值
>>> x = 1
>>> y = 2
# a, b 和x, y 为元祖，只是省略了括号
>>> a, b = x, y 
>>> a, b
(1, 2)

>>> c, d = [1, 2]
>>> c, d
(1, 2)
```

### 3. dir()与help()

1. `dir()`返回由对象所定义的名称列表

- 如果这一对象是模块，则该列表会包括函数内所定义的函数，类与变量
- 该函数可接受参数。如果参数是模块名称，函数将返回这一指定模块的**名称列表**。如果没有提供参数，函数将返回当前模块的名称列表

1. `help() `   函数用于查看函数或模块用途的详细说明。

1. `type()` 返回类型

### 4. 占位符 _

```
# you don't intend to use that value, _ 为占位符
for _ in range(3):
```

### 5. 三目运算符

```
a = 3
a = 1 if a>0 else 0  
print(a)
# a 

bin()
S.replace(old, new[, count]) -> str

>>> bin(2796202)
'0b1010101010101010101010'
int(x, base=10) -> integer

S.find(sub[, start[, end]]) -> int

```

### 6. 平方与开方

```
>>> a = 4
>>> a**2
16
>>> a**0.5
2.0
```

### 7. 物理分行

- 物理行：编写程序时，程序员所看到的内容
- 逻辑行：Python所看到的单个语句
Python假定每一个物理行会对应一个逻辑行使用 \  讲一个很长的物理行分成多个物理行

```
i = \
5       
# 等于
i = 5
```



## 四、 迭代器与生成器

### 1. generator

generator使用场景：

　　1  当我们需要一个公用的，按需生成的数据

　　2  某个事情执行一部分，另一部分在某个事件发生后再执行下一部分，实现异步。

注意事项：

  1  yield from generator_obj 本质上类似于 for item in generator_obj: yield item

  2  generator函数中允许使用return，但是return 后不允许有返回值

在python的函数（function）定义中，只要出现了yield表达式（Yield expression），那么事实上定义的是一个*generator function*， 调用这个generator function返回值是一个*generator*。这根普通的函数调用有所区别，For example：

```
def gen_generator():
    yield 1


def gen_value():
    return 1

if __name__ == '__main__':
    ret = gen_generator()
    print(ret, type(ret))    # <generator object gen_generator at 0x000002B2153AA5F0> <class 'generator'>
    ret = gen_value()
    print(ret, type(ret))    # 1 <class 'int'>
```


## 五、 流程控制

### 1. 基本流程

- for
- while
- if。if为真时，执行if子句
- if-else。if为假时，执行else子句，
- if-elif。注重次序，只有一个子句执行
- if-elif-else    当if子句和elif子句都为假时，执行else子句
- for-else 当for循环正常结束时（即不是通过break跳出结束的），会执行else中的语句，将for-else看成一个整体

### 2. for循环和while循环的装换

for(循环变量初始化;循环条件判断;循环变量改变)：

​	{     //...循环体 } 



while(循环条件判断)

{     //...循环体     循环变量改变; }

### 3. Python中的for循环

for 循环无法改变循环次数，应该使用while

```python
for i in range(10):
    print(i, end=' ')
    i += 2
# 0 1 2 3 4 5 6 7 8 9
```

### 4. break与continue

- break: 结束**当前循环体**

- continue: 结束**本次循环**

## 六、数据类型

### 1. 数字

- 整数 `int()`

- 浮点数  `float()`

  \#  `53.3E-4`  代表 53.3 * 10^-4

#### 1.1 数学操作符

表达式结果为数字

- \**
- %
- //
- /
- \*   可用于字符串和列表的复制
- \+   可用于字符串和列表的连接
- -

### 2. 字符串  `str()`

 	在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

**字符串是单个文本字符的列表**，可进行资格测试（in, not in），索引操作(切片，)

   - 单引号 '   '

   - 双引号 "   "

     \#  单双引号之间没有任何区别

   - 三引号      """         """ 或'''      '''

       \# 内可穿插单引号和双引号

       \# “三重引号” 之间的所有引号、 制表符或换行， 都被认为是字符串的一部分 

#### 2.1 拼接

```
>>> 'A' + 'B'
'AB'
```

#### 2.2 复制

```
>>> 'A' * 5
'AAAAA'
```

#### 2.3 原始字符串

```
>>> 'That is Alices\'s cat'
"That is Alices's cat"

>>> r'That is Alices\'s cat'
"That is Alices\\'s cat"


```

#### 2.4 “”   “”

三重引号” 之间的所有引号、 制表符或换行， 都被认为是字符串的一部分

```
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')


Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
```

#### 2.5 常用方法

- upper()

- lower()

- isupper()

- islower()

- startswith()

- endswith()

- join()    S.join(iterable) -> str

- split()

- replace  str.replace(old, new[, max])

  ```
  >>> ', '.join(['cats', 'rats', 'bats'])
  'cats, rats, bats'
  
  >>> ' '.join(['My', 'name', 'is', 'Simon'])
  'My name is Simon'
  
  >>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
  'MyABCnameABCisABCSimon'
  
  >>> 'My name is Simon'.split()
  ['My', 'name', 'is', 'Simon']
  
  >>> 'My name is Simon'.split('m')
  ['My na', 'e is Si', 'on']
  ```

- rjust(), ljust(), center()

```
# 右对齐
>>> 'Hello'.rjust(7, '*')
'**Hello'

>>> 'Hello'.ljust(7, '-')
'Hello--'

>>> 'Hello'.center(7, '=')
'=Hello='

>>> 'Hello'.center(7)
' Hello '
```

- strip()（两边）、 rstrip()和 lstrip() 删除空白字符（空格，制表符，换行符）

### 3. 布尔值 `bool()`

   - `True`，`False `
   - 布尔值可以用`and`、`or`和`not`运算

#### 3.1 比较操作符

表达式结果为布尔值

- ==
- !=
- <
- \>
- <=
- \>=
- <、 >、 <=和>=操作符仅用于整型和浮点型值 

#### 3.2 布尔操作符

**Python 先求值 not 操作符， 然后是 and 操作符， 然后是 or 操作符** 

- not
- or 
- and

#### 3.3 in 和 not in 操作符

表达式结果为布尔值

```
>>> animals = ['cat', 'dog', 'pig']
>>> 'cat' in animals
True
>>> 'fish' in animals
False
>>> 'fish' not in animals
True
```

###  4. None

- 可用于判断函数有无返回值

  ```
  >>> spam = print('Hello')
  Hello
  >>> None == spam
  True
  ```

## 七、数据结构

- 查找有无：元素 'a' 是否存在？可以使用 set 集合这种数据结构

- 查找对应关系（键值对应）：元素 'a' 出现了几次？可以使用 dict 字典这种数据结构

### 1 概述

**不可变对象**： 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会**创建新的对象**并返回，这样，就保证了不可变对象本身永远是不可变的

**数字，字符串，元组不可变**

**列表，字典可变**

1. list   []   打了激素的数组。
   - 以自然数为下标，有序，可以存储任意类型的数据（包括list）
2. truple ()  不可更改的列表。
   - 元组内的数值不可改变
3. dict   {key : value}  以自定义的key为下标，无序

   - dict中的项目是无序的，不能通过索引引用 
4. set {} 无序，唯一，确定

### 2 序列

序列：有序的集合(array-like?)

**列表list，元组trupe，字符串str, range**可以看作序列（Sequence）的某种表现形式

主要功能：

1. 资格测试（Membership Test） 也就是 in 与 not in 表达式
2. 索引操作（Indexing Operations）能够允许我们直接获取序列中的特定项目

- seq[i]： 返回序列中的第i个元素。
- len(sep)： 返回序列长度。
- seq1 + seq2： 返回两个序列的连接（不适用于range）。
- n*seq： 返回一个重复了n次seq的序列。
- seq[start:end]： 返回序列的一个切片。
- e in seq： 如果序列包含e，则返回True，否则返回False。
- e not in seq： 如果序列不包含e，则返回True，否则返回False。
- for e in seq： 遍历序列中的元素。 

###  3 切片

切片运算符：允许我们得到序列中的一部分  可以对str使用切片

[start: stop:  step] 默认start = 0，步长为1

[: : -1]  start，stop默认被交换，返回反转过的文本

[start: stop]    [start, stop)

[:] 从头到尾

[start:] 从start到列表尾部

[:stop]  从列表头部到stop

### 4 列表 list

- L.append(e)： 将**对象e**追加到L的末尾， return None
- L.extend(L1)： 将L1中的**item**追加到L末尾。
- L.count(e)： 返回e在L中出现的次数。
- L.insert(i, e)： 将对象e插入L中索引值为i的位置, return None
- L.remove(e)： 从L中删除第一个出现的e。
- L.index(e)： 返回e第一次出现在L中时的索引值。如果e不在L中，则抛出一个异常（参见第7章）。
- L.pop(i)： 删除并返回L中索引值为i的项目。如果L为空，则抛出一个异常。
  - 如果i被省略，则i的默认值为-1，删除并返回L中的最后一个元素。
- L.sort()： 升序排列L中的元素，ASCII 字符顺序 
- L.reverse()： 翻转L中的元素顺序。


#### 1. 创建

`list_name = list()`

`list_name = []  `

索引值为-1代表最后一个元素

列表为空时返回False

#### 2. 增

`insert(index，value)`

`append(object) `向列表尾部添加一个对象

```python
a = [1, 2, 3]
b = [1, 2]
a.append(b)
print(a)

# [1, 2, 3, [1, 2]]
```

`extend(sequence) `把一个序列seq的内容添加到列表中

```python
a = [1, 2, 3]
b = [1, 2]
a.extend(b)
print(a)

# [1, 2, 3, 1, 2]
```

对于list类型，`+=`操作相当于list的extend方法

```python
a = [1, 2, 3]
b = [1, 2]
a += b
print(a)

# [1, 2, 3, 1, 2]
```

#### 3 删

- `del list_name[index]`
- `pop()` 弹出列表末尾数据
- `pop(index)`
- `remove（value）` 删除列表中第一次出现的值

```
>>> b
[1, 1, 1]
>>> del b[1]
>>> b
[1, 1]
```

#### 4 改

`list_name[index] = 'name'`

#### 5 列表遍历

```python
numbers = [1, 2, 3]
for number in numbers:
	print(number)

for index in range(len(numbers)):
	print(number[i])
```

#### 6 数值列表

```python
numbers = list(range(1,6))
print(numbers)  # [1, 2, 3, 4, 5]
min(numbers)
max(numbers)
sum(numbers)
```

#### 7 列表复制

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

import copy
friend_foods = copy.copy(my_foods)
```

#### 8 列表推导

```python
squares =[]
for value in range(1, 11):
	square = value**2
	squares.append(square)
	

a = [value**2 for value in range(1, 11) if value%2 == 0]
# [4, 16, 36, 64, 100]
```

#### 9 乘法与加法

```python
b = [10] * 10
# [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

>>> a = list(range(1,6))
>>> b = list(range(6,10))
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

```

#### 10 长度

1. `len(lis)`

#### 11 修改正在遍历中的列表

Python使用一个内置计数器跟踪程序在列表中的位置，内部计数器在每次迭代结束时都会增加1。当计数器的值等于列表的当前长度时，循环终止。如果循环过程中列表没有发生改变，那么这种机制是有效的，但如果列表发生改变，就会产生出乎意料的结果。本例中，内置计数器从0开始计数，程序发现了L1[0]在L2中，于是删除了它——将L1的长度减少到3。然后计数器增加1，代码继续检查L1[1]的值是否在L2中。请注意，这时已经不是初始的L1[1]的值（2）了，而是当前的L1[1]的值（3）。避免这种问题的方法是使用切片操作克隆（即复制）这个列表，并使用**for e1 in L1[:]**这种写法

```python
# 错误版本：
def removeDups(L1, L2):
    """假设L1和L2是列表，
    删除L1中出现的L2中的元素"""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
            
# 正确版本
def removeDups_T(L1, L2):
    """假设L1和L2是列表，
    删除L1中出现的L2中的元素"""
    for e1 in L1[:]:
        if e1 in L2:
            L1.remove(e1)
            
L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print('L1 =', L1)
# L1 = [2, 3, 4]

removeDups_T(L1, L2)
# L1 = [3, 4]
```

#### 12 引用传递

```python
a = [1, 2]
b = a
b[0] = 0
print(a)
# [0, 2]
```

### 5 元组 truple

#### 1 简介

`tuple_name = ()`

`tuple_name = tuple()`

元组：不可变的列表

不可修改元组中元素的值，但可以给元组变量赋值

```python
>>> T = tuple(range(1,5))
>>> T + (5,6)
(1, 2, 3, 4, 5, 6)
>>> T
(1, 2, 3, 4)
```

#### 2 只有1个元素的tuple

定义一个只有1个元素的tuple，定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

所以，只有1个元素的tuple定义时必须加一个逗号,

```
>>> t = (1)
>>> t
1

>>> t = (1,)
>>> t
(1,)
```

#### 3 不变性

 tuple所谓的“不变”是说，tuple的每个元素，**指向（引用）**永远不变

```
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

#### 4 加法

```
>>> t1 = (1, 'two', 3)
>>> t2 = (t1, 3.25)
>>> t2
((1, 'two', 3), 3.25)
>>> t1 + t2
(1, 'two', 3, (1, 'two', 3), 3.25)
>>> (t1 + t2)[3]
(1, 'two', 3)
```

 ### 6 字典 dict

字典：键__值对，无序

- len(d)： 返回d中项目的数量。
- d.keys()： 返回d中所有键的视图。
- d.values()： 返回d中所有值的视图。
- k in d： 如果k在d中，则返回True。
- d[k]： 返回d中键为k的Item。
- d.get(k, v)： 如果k在d中，则返回d[k]，否则返回v。
- d[k] = v： 在d中将值v与键k关联。如果已经有一个与k关联的值，则替换。
- del d[k]： 从d中删除键k。
- for k in d： 遍历d中的键。

#### 1 创建

`dict_name = dict() `

`dict_name = {}`

#### 2 增

```python
dict_nam['name'] = 'Eric'
dict_nam = {"name": 'Eric"}
```

#### 3 删

```
del dict_nam['name'] 
pop(key)
>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85}
```

#### 4 改

`dict_nam['name'] = 'Tom'`

#### 5 遍历

```python
for key, value in user_0.items():
	print("Key: " + key)
	print("Value: " + value)
	print("\n")

# 遍历所有键
for name in user_0.keys():
	print(name.title())
# keys() 返回一个列表

# 遍历所有值
for language in favorite_languages.values():
	print(language.title())
```

#### 6 in

```python
>>> dic = {'a':1, 'b':2}
>>> 'a' in dic
True
>>> 1 in dic
False
```

#### 7 注意点

1.  要避免key不存在的错误，有两种办法，一是通过`in`判断key是否存在
2. 二是通过dict提供的`get()`方法，如果key不存在，可以返回None，或者自己指定的value

   - D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
3.  和list的比较：空间来换取时间

           1. 查找和插入的速度极快，不会随着key的增加而变慢；
           2. 需要占用大量的内存，内存浪费多

### 7 集合 set

#### 1 简介

集合：无序，唯一，确定

`set_name = set()`  

过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果

## 八、函数

### 1 概述

1. ***args是可变参数，args接收的是一个tuple**；

2. **\**kw是关键字参数，kw接收的是一个dict**

函数

```python
def 函数名(参数列表):
	suite

```

- 形参：函数中**定义**的参数
- 实参：**调用函数时传入**的参数     
  - 定义时为形参，调用时为实参
- 位置实参： 将每个实参按顺序一一关联到函数定义中的形参，考虑函数调用中的实参顺序
- 关键字实参： 传递给函数的  Key--Value  对
- 默认值实参： 
  1. 使用默认值时，在形参列表中必须**先列出没有默认值的形参**，再列出有默认值的形参
  2. 调用函数时如果没有指定形参，函数将自动调用默认值
  3. **默认参数一定要用不可变对象**，如果是可变对象，程序运行时会有逻辑错误！

**PS:  **

​	在python中，**函数名加()，表示返回的是一个函数的结果，不加括号表示的是对函数的调用。函数名其实就是指向一个函数对象的引用**，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

```python
>>> a = abs # 变量a指向abs函数
>>> a(-1) # 所以也可以通过a调用abs函数
1
```

### 2 空函数

如果想定义一个什么事也不做的空函数，可以用pass语句

```python
def nop():
	pass
```

pass语句什么都不做，那有什么用？实际上**pass可以用来作为占位符**，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

### 3 关键字实参

```python
def describe_pet(animal_type, pet_name):
	print("I have a " + animal_type)
	print("My " + animal_type + "'s name is " + pet_name.title())
	
describe_pet(animal_type = 'hamster', pet_name = "harry")
```

### 4 默认值

```python
def describe_pet(pet_name, animal_type = 'dog'):
	print("I have a " + animal_type)
	print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet("harry")
```

 ### 5 传递任意数量的参数

1. *toppings为空元组，将所有受到的值到装入该元组中
2. 如果让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后

```python
def make_pizza(*toppings):
	print(toppings)
	
make_pizza('pepperoni') 
make_pizza("mushroom", 'green peppers')

```

### 6 传递任意数量的关键字实参

**user_info 为dict

```python
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
    	profile[key] = value
    return profile

 

user_profile = build_profile('albert', 'einstein',
                                location = 'princeton',
                                field = 'physics')
print(user_profile)


# {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
```

### 7 返回值

- 函数返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
-  对于所有没有 return 语句的函数定义， Python 都会在末尾加上 return
    None 

### 8 作用域

​	一个函数被调用时， 就创建了一个局部作用域。在这个函数内赋值的所有变量，存在于该局部作用域内。该函数返回时，这个局部作用域就被销毁了， 这些变量就丢失了。下次调用这个函数， 局部变量不会记得该函数上次被调用时它们保存的值。 

- 局部作用域 ：在被调用函数内赋值的变元和变量 
- 全局作用域 ：在所有函数之外赋值的变量 
- 局部变量 ：处于局部作用域的变量 
- 全局变量 ：处于全局作用域的变量 

**PS：**一个变量必是其中一种，不能既是局部的又是全局的 

- 局部变量不能在全局作用域内使用 
- 局部作用域可以访问全局变量 
- 一个函数的局部作用域中的代码，不能使用其他局部作用域中的变量 

```\
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'
    
eggs = 'global'
bacon()
print(eggs) # prints 'global'

# bacon local
# spam local
# bacon local
# global

def spam():
    print(eggs) 
    eggs = 'spam local' # ERROR!
    
eggs = 'global'
spam()
# eggs 为全局变量，在spam中修改全局变量，会报错
```

### 9 global

- 如果想在一个函数中修改全局变量中存储的值，就必须对该变量使用 global语句 

```
def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)

# spam
```

- 区分

  1．如果变量在全局作用域中使用（即在所有函数之外），它就总是全局变量。
  2．如果在一个函数中，有针对该变量的 global 语句，它就是全局变量。
  3．否则，如果该变量用于函数中的赋值语句，它就是局部变量。
  4．但是，如果该变量没有用在赋值语句中，它就是全局变量。 

```
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local
    
def ham():
    print(eggs) # this is the global
    
eggs = 42 # this is the global
spam()
print(eggs)

# spam
```



## 九、面向对象

### 8.1 简介

​	类与对象是面向对象编程的两个主要方面。一个类（Class）能够创建一种新的类型（Type），其中对象（Object）就是类的实例（Instance)。类的属性（Attribute)有字段（Field）和类的方法（Method）

- 方法（method）: 与类和实例有绑定关系的function

- 字段：绑定到类与对象的命名空间的普通变量，仅在这些类与对象所存在的上下文中有效

- 实例变量（Instance Variables）：由类的每一个独立的对象或实例所拥有

- 类变量（Class Vaariables）：可以被属于该类的所有实例访问。该类变量只拥有一个副本，当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现

类支持两种操作：

- 实例化：创建类的实例 
- 属性引用：通过点标记法访问与类关联的属性 



  类方法和普通函数的区别，前者必须有self，相当与java中的this

1.  self为指向实例本生的一个引用

2. 类中的每个方法都必须提供self作为第一个参数

3. 类中的每个属性前面必须有self，从而将数据与其实例关联

### 8.2 类

```python
class Athlete:
	Athlete_nums = 0 # 类变量
	def __init__(self, arg1, arg2):
		self.arg1 = "arg1"  对象的属性
		self.arg2 = "arg2"
		
	@classmethod  #使用装饰器（Decorator） 将fun方法标记为类方法
	def fun(self)
		suite
        
a = Athlete()  #  实际上调用了Athlete().__init__(a, arg1, arg2)
```

​	以self为前缀的变量可供类中的所有方法使用，还可通过类的任何实例来访问属性(通过实例访问的对象)的修改

1. 直接访问类中的属性并修改
2. 通过方法修改属性的值

### 8.3 继承

子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法，也可以覆盖超类的属性和方法

1. 创建子类时，父类必须包含在当前文件中，且位于子类前面
2. 定义子类时，必须在括号内指定父类的名称

如果在子类中定义了\_\_init\_\_方法，Python不会自动调用基类的构造函数，必须自己显式地调用它。相反，如果我们没有在一个子类中定义一个\_\_init\_\_方法，Python将会自动调用基类的构造函数

```python
# 子类添加新属性和方法
class ElectricCar(Car):
	def __init__(self, make, model, year):
        # Car.__init__(self, make, model, year)
		super().__init__(make, model, year)  # 显式调用父类的构造函数 
		self.battery_size = 70 
		
	def describe_battery(self):  
		print("This car has a "+str(self.battery_size))
		
my_tesla = ElectricCar("tesla", 'model s', 2016)
print(my_tesla.get_dec())
my_tesla.describe_battery()
```

### 8.4 实例作为属性

```python
定义子类时，必须在括号内指定父类的名称class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model 
		self.year = year 
		self.odometer_reading = 0
	
	def get_dec(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_od(self):
		print("This car has " + str(self.odometer_reading )+' miles on in')


class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
	def describe_battery(self):  
		print("This car has a "+str(self.battery_size))

# 继承。子类ElectricCar继承了其父类Car的所有属性和方法，同时还可以定义自己的属性battery和方法
# 定义子类时，必须在括号内指定父类的名称
class ElectricCar(Car):
	def __init__(self, make, model, year):
        # 子类中定义了__init__方法，Python不会自动调用基类Car的构造函数，必须自己显式地调用它
		super().__init__(make, model, year) # 显式地调用基类Car的构造函数
		self.battery = Battery()  # 将实例作为属性


my_tesla = ElectricCar("tesla", 'model s', 2016)
print(my_tesla.get_dec())
my_tesla.battery.describe_battery()

# 2016 Tesla Model S
# This car has a 70
```

## 十、模块

### 1. 简介

**模块**：变量名的封装，被认作是命名空间。在一个包中的变量名就是所谓的属性。一个包含Python代码的文本文件,扩展名为.py

1. 每个模块都有一个名称\_\_name\_\_属性
2. from 把变量从一个文件复制到另一个文件中
3. 当模块第一次被导入时，它所包含的代码将被执行
4. dir()返回由对象所定义的变量列表
   - 该函数可接受参数。如果参数是模块名称，函数将返回这一指定模块的名称列表。如果没有提供参数，函数将返回当前模块的名称列表(包括函数内所定义的函数，类与变量)

### 2.导入模块

```python
# 导入模块
import module_name

# 使用模块
module_name.function_name()
 
# 导入特定的函数
from module_name import function_name0, function_name1
# 使用特定的函数
function_name0 # 不能指定模块名

# 导入模块中的所有函数
from module_name import *

# 使用as给函数指定别名
from module_name import function_name as fn
# 使用as给模块指定别名
import module_name as mn
```

**包**：变量通常位于函数内部，函数和全局变量通常位于模块内部。
包是指一个包含模块与一个特殊的\_\_init\_\_.py 文件的文件夹

## 十一、异常处理

```python
try：
	可能导致一个运行时错误exception
except Exception as err：
	print('An exception happened: ' + str(err))
	错误恢复代码
finally：
	代码总会执行
```

## 十二、文件读写

### 1. 文件路径

#### 1.1 根文件

- Windows   C:\
- Linux/OS X   /

#### 1.2  os.path.join()

```
>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
		print(os.path.join('C:\\Users\\asweigart', filename))
		
C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv
C:\Users\asweigart\invite.docx
```

#### 1.3 os.getcwd(),os.chdir()

```
>>> os.getcwd()
'C:\\Users\\MiloYe'
>>> os.chdir('d:')
>>> os.getcwd()
'D:\\'
```

#### 1.4 绝对路径与相对路径

- “绝对路径”， 总是从根文件夹开始。 
- “相对路径”，它相对于程序的当前工作目录。 
- 点（.） 这个目录， (.\study.txt)  和 （study.txt）指向同一个文件
- 点点（..）父文件夹

#### 1.5 os.makedirs()

```
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')
```

#### 1.6 处理绝对路径和相对路径

- os.path.abspath(path)

- os.path.isabs(path)

  ```
  >>> os.path.abspath('.')
  'C:\\Python34'
  >>> os.path.abspath('.\\Scripts')
  'C:\\Python34\\Scripts'
  >>> os.path.isabs('.')
  False
  >>> os.path.isabs(os.path.abspath('.'))
  True
  ```

- os.path.basename (path)

- os.path.dirname(path)

- os.path.split(path) 

- os.path.sep

- split() 

  ```
  >>> path = 'C:\\Windows\\System32\\calc.exe'
  >>> os.path.basename(path)
  'calc.exe'
  >>> os.path.dirname(path)
  'C:\\Windows\\System32'
  >>> os.path.split(path)
  ('C:\\Windows\\System32', 'calc.exe')
  >>> path.split(os.path.sep)
  ['C:', 'Windows', 'System32', 'calc.exe']
  ```

#### 1.7 查看文件大小和文件夹内容

- os.path.getsize(path) --> 字节数
- os.listdir(path) 

```
>>> total_size = 0
>>> for filename in os.listdir(os.getcwd()):
...     total_size = total_size + os.path.getsize(os.path.join(os.getcwd(),filename))
...
>>> total_size
5738516
```

#### 1.8 检查路径有效性

- 如果 path 参数所指的文件或文件夹存在， 调用 os.path.exists(path)将返回 True，
  否则返回 False。 
- 如果 path 参数存在，并且是一个文件， 调用 os.path.isfile(path)将返回 True， 否
  则返回 False。 
- 如果 path 参数存在， 并且是一个文件夹， 调用 os.path.isdir(path)将返回 True，
  否则返回 False。 

```
>>> os.path.exists('D:\\')
True
>>> os.path.exists('D:')
True
```

### 2. 文件读写

EOF是一个计算机术语，为End Of File的缩写，在操作系统中表示资料源无更多的资料可读取。资料源通常称为档案或串流。通常在文本的最后存在此字符表示资料结束

如果传递给 open()的文件名不存在，写模式和添加模式都会创建一个新的空文件。调用 close()方法， 然后才能再次打开该文件  

open() 返回一个表示文件的对象

- w write（覆盖原文）
- a append
- r read
- t text
- b binary system

read() 读取文件中的全部内容

with 自动处理所有已打开文件的关闭工作

readline() 读取文件中的每一行，将其存储在一个**列表**中

seek(0) 将文件退回到起始位置

split() 将一个字符分解为一个子串列表

find() 在一个字符串中查找一个特定子串

pass 空语句

```
try:
    with open("its.txt","w") as data:
        print("It's ...", file=data)
except IOError as err:
    print("File error:" + str(err))
```

## 十三、爬虫

1. webbrowser：是 Python 自带的，打开浏览器获取指定页面。
2. requests：从因特网上下载文件和网页。
3. Beautiful Soup：解析 HTML，即网页编写的格式。
4. selenium：启动并控制一个 Web 浏览器。 selenium 能够填写表单，并模拟鼠标在这个浏览器中点击 

### 1. webbrowser

```
import webbrowser

# 在浏览器中打开页面
webbrowser.open('http://inventwithpython.com/')
```

### 2. requests

HTTP请求(request)方法：

- GET请求会把表单数据追加到URL的最后(不安全)
- POST请求将表单数据包括在请求的体中

`get(url, params=None, **kwargs) Sends a GET request, return requests.Response.`

#### 1. get

```python
url = "https://morvanzhou.github.io/static/scraping/list.html"
r = requests.get(url)
print(r.text)
# <!DOCTYPE html>
# <html lang="cn">

param = {'wd': '哔哩哔哩'}
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
webbrowser.open(r.url)
# http://www.baidu.com/s?wd=%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9


```

#### 2. post

- 使用cookies登录

  ```python
  payload = {'username': 'MiloYe', 'password': 'password'}
  r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
  print(r.cookies.get_dict())
  
  # 使用cookies维持登录状态
  r = requests.get('http://pythonscraping.com/pages/cookies/welcome.php', cookies=r.cookies)
  print(r.text)
  
  r = requests.get('http://pythonscraping.com/pages/cookies/welcome.php')
  print(r.text)
  
  ​```
  {'username': 'MiloYe', 'loggedin': '1'}
  
  <h2>Welcome to the Website!</h2>
  You have logged in successfully! <br><a href="profile.php">Check out your profile!</a>
  
  <h2>Welcome to the Website!</h2>
  Whoops! You logged in wrong. Try again with any username, and the password "password"<br><a href="login.html">Log in here</a>
  ​```
  ```

- 使用session登录

  ```
  session = requests.Session()
  payload = {'username': 'MiloYe', 'password': 'password'}
  r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
                   
  print(r.cookies.get_dict())   
  
  r = session.get("http://pythonscraping.com/pages/cookies/welcome.php")   
  print(r.text)
  
  ​```
  {'loggedin': '1', 'username': 'MiloYe'}
  
  <h2>Welcome to the Website!</h2>
  You have logged in successfully! <br><a href="profile.php">Check out your profile!</a>
  ​```
  ```

#### 3. download

`iter_content(chunk_size=1, decode_unicode=False)`

```
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# 检查错误
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)   
playFile.close()

# 下一点, 保存一点
r = requests.get(IMAGE_URL, stream=True)
with open('./img/image2.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
```

### 3. Beautiful Soup

1. lxml HTML 解析器	`BeautifulSoup(html, "lxml")`
2. Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: `Tag` , `NavigableString` , `BeautifulSoup` , `Comment` .
3. `Tag` (元素)对象与XML或HTML原生文档中的tag相同:

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')
tag = soup.b
type(tag)
# <class 'bs4.element.Tag'>

tag.name
# 'b'

# 操作跟字典相同
tag.attrs
# {'class': ['boldest']}

tag['class']
# ['boldest']

tag..get('class')
# ['boldest']

tag.get_text()
# 'Extremely bold'
```

#### 1. find - find_all

`find(name=None, attrs={}, recursive=True, text=None, **kwargs) `

- name = tag-name 标签名
- attrs = tag-attrs 标签属性

`find_all(name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)`

```python
# 下面两行代码是等价
soup.find_all("a")
soup("a")

# 下面两行代码是等价
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]
soup.find('title')
# <title>The Dormouse's story</title>

month = soup.find_all('li', {"class": "month"})
print(month)
# [<li class="month">一月</li>, <li class="feb month">二月</li>, <li class="month">三 # 月</li>, <li class="month">四月</li>, <li class="month">五月</li>]

```

#### 2. select

返回一个list，list元素为tag。`len(list_name)`可以查看列表中的元素个数

```
soup.select('div') 所有名为<div>的元素
soup.select('#author') 带有 id 属性为 author 的元素
soup.select('.notice') 所有使用 CSS class 属性名为 notice 的元素
soup.select('div span') 所有在<div>元素之内的<span>元素
soup.select('div > span') 所有直接在<div>元素之内的<span>元素， 中间没有其他元素
soup.select('input[name]') 所有名为<input>，并有一个 name 属性，其值无所谓的元素
soup.select('input[type="button"]') 所有名为<input>，并有一个 type 属性，其值为button的元素
```

## PS

- Python中的切片不可以进行运算，但是Numpy中的可以
- range和切片运算都是 half-open。[start: stop)

```
>>> x = list(range(10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[0:10] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> import numpy as np
>>> y = np.array(x)
>>> y
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> y[0:10] = 10
>>> y
array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
```

## 常用函数

### 1. zip()

`zip(iter1 [,iter2 [...]]) --> zip object `

- zip() 函数用于将**可迭代的对象**作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。 

- 使用list() 转换来输出列表

```
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个zip对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))       # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]

# 与 zip 相反，*zip 可理解为解压，返回二维矩阵式
>>> a1, a2 = zip(*zip(a,b))          
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
```

### 2. map()

`map(func, *iterables) --> map object`

- Make an iterator that computes the function using arguments from each of the iterables.  Stops when the shortest iterable is exhausted.

```
>>> def square(x):
...     return x**2
...
>>> map(square, [1,2,3,4,5])
<map object at 0x000002B784776BA8>
>>> x = map(square, [1,2,3,4,5])
>>> list(x)
[1, 4, 9, 16, 25]

def square(a, b):
	return a**2 + b**2

print(list(map(square, [1, 2, 3, 4], [1, 2, 3, 4])))
```

### 3. id()

`id(obj, /)`

- Return the identity of an object.

### 4. enumerate()

`enumerate(iterable[,start]) -> iterator for index, value of iterable`

```
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> enumerate(seasons)
<enumerate object at 0x0000018BB7CD3EA0>
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]


>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
... 
0 one
1 two
2 three

```

### 5. print() 和input()

` print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)`

print()允许传入一个整型值或字符串 

`input() --> string`

```
>>> input('please input a number')
please input a number 2
' 2'

print('Hello')
print('World')
#Hello
#World

print('Hello', end='')
print('World')
# HelloWorld

print('cats', 'dogs', 'mice')
# cats dogs mice

print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice

```

### 6. len()

`len(obj, /) Return the number of items in a container.`

```
>>> s = '23sad'
>>> len(s)
5
>>> a = list(range(1,11))
>>> len(a)
10

```

### 7. sorted()

在Python 中sorted是内建函数(BIF),而sort()是列表类型的内建函数list.sort()。

## 常用模块

### 1. OS

`os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])`

- top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root, dirs, files)。
- root 当前文件夹名称的字符串 
- dirs 当前文件夹中子文件夹的字符串的列表 
- files 当前文件夹中文件的字符串的列表。 

**d = dir = directory**  

| function                                  |                                                              |
| ----------------------------------------- | ------------------------------------------------------------ |
| `os.getcwd()`                             | 获取当前工作目录，即当前python脚本工作的目录路径             |
| `os.chdir("dirname")`                     | 改变当前脚本工作目录；相当于shell下cd                        |
| `os.mkdir('dirname')`                     | 生成单级目录；相当于shell中mkdir dirname                     |
| `os.makedirs('dir1/dir2', exist_ok=True)` | 可生成多层递归目录                                           |
| `os.listdir('dirname')`                   | 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印 |
| `os.rename("oldname","new")`              | 重命名文件/目录                                              |
| `os.removedirs('dirname1')   `            | 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推 |
| `os.rmdir('dirname')  `                   | 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname |
| `os.remove()  `                           | 删除一个文件                                                 |
| `os.sep`                                  | 操作系统特定的路径分隔符，win下为"\\",Linux下为"/"           |
| `os.path.exists(path)`                    | 如果path存在，返回True；如果path不存在，返回False            |
| `os.path.split(path)`                     | 将path分割成目录和文件名二元组返回                           |
| `os.path.dirname(path)`                   | 返回path的目录。其实就是`os.path.split(path)`的第一个元素    |
| `os.path.basename(path)`                  | 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即 `os.path.split(path)`的第二个元素 |
| `os.path.join(path1[, path2[, ...]])`     | 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略       |
| `os.path.abspath(path)`                   | 返回path规范化的绝对路径                                     |
| os.curdir                                 | 返回当前目录: ('.')                                          |
| os.pardir                                 | 获取当前目录的父目录字符串名：('..')                         |

```

```

### 2. collections

```
>>> c = Counter('abcdeabcdabcaba')
>>> c
Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
>>> c.most_common(1)
[('a', 5)]
>>> c.most_common(1)[0][0]
'a'
>>> c.keys()
dict_keys(['a', 'b', 'c', 'd', 'e'])
>>> c.values()
dict_values([5, 4, 3, 2, 1])
```

### 3. random

| function                                  |                                                |
| ----------------------------------------- | ---------------------------------------------- |
| print(random.random())                    | 随机产生[0,1)之间的浮点值                      |
| print(random.randint(1,6))                | 随机生成指定范围[a,b]的整数                    |
| print(random.randrange(1,3))              | 随机生成指定范围[a,b)的整数                    |
| print(random.randrange(0,101,2))          | 随机生成指定范围[a,b)的指定步长的数（2--偶数） |
| print(random.choice("hello"))             | 随机生成指定字符串中的元素                     |
| print(random.choice([1,2,3,4]))           | 随机生成指定列表中的元素                       |
| print(random.choice(("abc","123","liu"))) | 随机生成指定元组中的元素                       |
| print(random.sample("hello",3))           | 随机生成指定序列中的指定个数的元素             |
| print(random.uniform(1,10))               | 随机生成指定区间的浮点数                       |
| random.shuffle(x)                         | Shuffle list x in place, and return None       |

###   4. pyperclip

```
>>> import pyperclip
>>> pyperclip.copy('Hello')
>>> pyperclip.paste()
'Hello'
```

### 5. shutil

#### 1. 复制文件和文件夹

- shutil.copy(source, destination)   复制一个文件 

```
>>> shutil.copy('hello.txt', 'D:')
'D:hello.txt'
>>> shutil.copy('hello.txt', 'D:hello2.txt')
'D:hello2.txt'
```

- shutil.copytree(source, destination )  复制整个文件夹，以及它包含的文件夹和文件 

```
>>> shutil.copytree('hello', 'D:\\Hello')
'D:\\Hello'
```

#### 2. 文件和文件夹的移动与改名 

- shutil.move(source, destination) -->返回新位置的绝对路径的字符串 

```
>>> shutil.move('hello.txt', 'hello')
'hello\\hello.txt'

>>> shutil.move('hello\\hello.txt', '.\\')
'.\\hello.txt'

>>> shutil.move('hello.txt', 'hello2.txt')
'hello2.txt'
```

#### 3. 永久删除文件和文件夹 

- os.unlink(path) --> 删除 path 处的文件 
- os.rmdir(path) --> 将删除 path 处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹 
- shutil.rmtree(path)  --> 删除 path 处的文件夹，它包含的所有文件和文件夹都会被删除 

```python
import os

for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
```

#### 4. 用 send2trash 模块安全地删除 

​	将文件夹和文件发送到计算机的垃圾箱或回收站，而不是永久删除它们 

```
>>> import send2trash
>>> send2trash.send2trash('hello2.txt')
```

#### 5. 遍历目录树 

`os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])`

- top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root, dirs, files)。
- 先根遍历
- folderName 当前文件夹名称的字符串 
- subfolders 当前文件夹中子文件夹的字符串的列表 
- filenames 当前文件夹中文件的字符串的列表。 

```
# 每次遍历都是一个同时解包3个值folderName, subfolders, filenames，每个值都是一个list
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is '+ folderName)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
```

### 6. sys

sys.argv  -- list对象：第一个参数为本文件的绝对路径字符串，第二参数为从程序外部输入的字符串

### 7. openpyxl

​	一个 Excel 电子表格文档称为一个工作簿 ，一个工作簿保存在扩展名为.xlsx 的文件中。每个工作簿可以包含多个表（也称为工作表） 。用户当前查看的表（或关闭 Excel 前最后查看的表），称为活动表。

#### 1. 结构

-  工作簿（Workbook）
  - 工作表（sheet）
    - 单元格（Cell）

#### 2. Workbook

```
wb = openpyxl.load_workbook('example.xlsx')


wb.sheetnames
# ['Sheet1', 'Sheet2', 'Sheet3']

wb.worksheets
# [<Worksheet "Sheet1">, <Worksheet "Sheet2">, <Worksheet "Sheet3">]

wb.save('balances.xlsx')


```

#### 3. sheet

```
sheet = wb['Sheet3']
sheet = wb[2]

sheet.title
# 'Sheet3'

sheet.max_row
# 7
sheet.max_column
# 3

sheet.rows

tuple(sheet.values)
​```
(('4/5/2015 1:34:02 PM ', 'Apples ', 73),
 ('4/5/2015 3:41:23 AM ', 'Cherries ', 85),
 ('4/6/2015 12:46:51 PM ', 'Pears ', 14),
 ('4/8/2015 8:59:43 AM ', 'Oranges ', 52),
 ('4/10/2015 2:07:00 AM ', 'Apples ', 152),
 ('4/10/2015 6:10:37 PM ', 'Bananas ', 23),
 ('4/10/2015 2:40:46 AM ', 'Strawberries ', 98))
​```

>>> ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
# or
>>> ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
# or
>>> ws3 = wb.create_sheet("Mysheet", -1) # insert at the penultimate position

del wb['Sheet3']
```

####  4.  Cell

- 获取cell对象

  ```
  cell = sheet.cell(row=1, column=1, value=10)
  # <Cell 'Sheet1'.A1>
  
  cell = sheet['A1']
  
  cell_range = ws['A1': 'C2']
  cell_range
  # ((<Cell 'New Title'.A1>, <Cell 'New Title'.B1>, <Cell 'New Title'.C1>),
  #  (<Cell 'New Title'.A2>, <Cell 'New Title'.B2>, <Cell 'New Title'.C2>))
  
  colC = ws['C']
  colC
  ​```
  (<Cell 'New Title'.C1>,
   <Cell 'New Title'.C2>,
   <Cell 'New Title'.C3>,
   <Cell 'New Title'.C4>,
   <Cell 'New Title'.C5>)
  ​```
   
   col_range = ws['C:D']
  col_range
  ​```
  ((<Cell 'New Title'.C1>,
    <Cell 'New Title'.C2>,
    <Cell 'New Title'.C3>,
    <Cell 'New Title'.C4>,
    <Cell 'New Title'.C5>),
   (<Cell 'New Title'.D1>,
    <Cell 'New Title'.D2>,
    <Cell 'New Title'.D3>,
    <Cell 'New Title'.D4>,
    <Cell 'New Title'.D5>))
  ​```
  
  ws[1]
  ​```
  (<Cell 'New Title'.A1>,
   <Cell 'New Title'.B1>,
   <Cell 'New Title'.C1>,
   <Cell 'New Title'.D1>,
   <Cell 'New Title'.E1>)
  ​```
  
  ws[1:2]
  ​```
  ((<Cell 'New Title'.A1>,
    <Cell 'New Title'.B1>,
    <Cell 'New Title'.C1>,
    <Cell 'New Title'.D1>,
    <Cell 'New Title'.E1>),
   (<Cell 'New Title'.A2>,
    <Cell 'New Title'.B2>,
    <Cell 'New Title'.C2>,
    <Cell 'New Title'.D2>,
    <Cell 'New Title'.E2>))
  ​```
  ```


- cell属性

  ```
  cell = sheet['A1']
  cell.value
  # '4/5/2015 1:34:02 PM '
  
  cell.coordinate
  # 'A1'
  cell.row
  # 1
  cell.column
  # 'A'
  ```

- 遍历cell

  ```
  cell_range = sheet['A1':'C3']
  # ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>),
  #  (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>),
  #  (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
  
  for rowOfCellObjects in sheet['A1':'C3']:
      for cellObj in rowOfCellObjects:
          print(cellObj.coordinate, cellObj.value)
      print('-----END OF ROW-----')
  
  ​```
  A1 4/5/2015 1:34:02 PM 
  B1 Apples 
  C1 73
  -----END OF ROW-----
  A2 4/5/2015 3:41:23 AM 
  B2 Cherries 
  C2 85
  -----END OF ROW-----
  A3 4/6/2015 12:46:51 PM 
  B3 Pears 
  C3 14
  -----END OF ROW-----    
  ​```    
  ```

- 按行遍历sheet

  ```
  for row_obj in sheet.rows:
      for cell in row_obj:
          print(cell.value, end=' ')
      print()
      
  ​```
  4/5/2015 1:34:02 PM  Apples  73 
  4/5/2015 3:41:23 AM  Cherries  85 
  4/6/2015 12:46:51 PM  Pears  14 
  4/8/2015 8:59:43 AM  Oranges  52 
  4/10/2015 2:07:00 AM  Apples  152 
  4/10/2015 6:10:37 PM  Bananas  23 
  4/10/2015 2:40:46 AM  Strawberries  98 
  
  >>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
  ...    for cell in row:
  ...        print(cell)
  ```

- 按列遍历sheet

  ```
  for col_obj in sheet.columns:
      for cell in col_obj:
          print(cell.value)
      print()
  
  ​```
  4/5/2015 1:34:02 PM 
  4/5/2015 3:41:23 AM 
  4/6/2015 12:46:51 PM 
  4/8/2015 8:59:43 AM 
  4/10/2015 2:07:00 AM 
  4/10/2015 6:10:37 PM 
  4/10/2015 2:40:46 AM 
  
  Apples 
  Cherries 
  Pears 
  Oranges 
  Apples 
  Bananas 
  Strawberries 
  
  73
  85
  14
  52
  152
  23
  98
  ​```
  
  >>> for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
  ...     for cell in col:
  ...         print(cell)
  ```

#### 5. 创建Workbook

  ```
  from openpyxl import Workbook
  
  wb = Workbook()
  ws = wb.active
  
  ws.title
  # 'Sheet'
  
  ws.title = "New Title"
  ws.title
  # "New Title"
  
  ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
  ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
  ws3 = wb.create_sheet("Mysheet", -1) # insert at the penultimate position
  
  wb.sheetnames
  # ['Mysheet1', 'New Title', 'Mysheet2', 'Mysheet']
  

  ```

#### 6. 写

```
# 初始化单元格， range必须从1开始
for x in range(1,6):
    for y in range(1,6):
        ws.cell(row=x, column=y， value=10)
        
# 填表
ws['A4'] = 4


```

#### 7. 公式

```
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '= sum(A1:A2)'
wb.save('writeFormula.xlsx')
```

#### 8. Working with Pandas and NumPy

##### 1.  Working with Pandas Dataframes

<https://openpyxl.readthedocs.io/en/stable/pandas.html#converting-a-worksheet-to-a-dataframe>

```
from openpyxl.utils.dataframe import dataframe_to_rows
wb = Workbook()
ws = wb.active

for r in dataframe_to_rows(df, index=True, header=True):
    ws.append(r)
    
    
df = DataFrame(ws.values)
```

### 8. pyautogui

```
>>> import pyautogui
>>> pyautogui.PAUSE = 1
>>> pyautogui.FAILSAFE = True
>>> pyautogui.size()
Size(width=1920, height=1080)
>>> width, height = pyautogui.size()
>>> width
1920
```

