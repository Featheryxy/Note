# 算法笔记

## 1. 流程控制
- for，while(直到。。。为止)，while True(无限循环)， 

- if。if为真时，执行if子句

- if-else。if为假时，执行else子句，if-else中的语句中不能相同，如有相同，应放置在if-else语句块外。

```
if True:
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



## 2. 标记

``` 
# 标号从0开始
i = -1: 
while condition :
	i = i + 1	
```
&emsp;&emsp;标记变量的状态，flag 

```
    for:
	flag = 1
	for:
		if：
		   flag = 0
	if flag:
		suite
```
## 3. set()

&emsp;&emsp;记录一个字符串或一个列表中出现的不重复元素来筛选出（删除）重复的元素

## 4. HashMap
```
def count(nums):
	dic = {}
	for num in nums:
		if num in dic:
			dic[num] += 1
		else:
			dic[num] = 1
	return dic
```
&emsp;&emsp;**furthermore：** 使用Counter()
```
# Counter.items() --> [()]
# Counter.most_common() -->  [()]
# dict(Counter) --> {}

from collections import Counter

for key, values in dict(Counter(nums)).items():
    if values == 2:
        ret.append(key)

[item[0] for item in Counter(nums).items() if item[1] == 2]
```

## 5. not 
&emsp;&emsp;利用反向思维，简单化问题	
​	

## 6. 数字的处理

- 将数字转换成字符串进行处理
- 逐项操作
```
#　取个位数字
num % 10	
#　删除个位数字
num // 10	
int(num / 10)
```

## 	7.链表推导
```
[function(i) for i in iteration if condition]
```

## 8.数组下标

数组下标和值对应起来， 先保存自己的值，将要更换的数字赋值给自己
```
for i in range(n):
	while nums[i] !=i and i < n:
		int t = nums[i];  # 保存index=i 上的值
		nums[i] = nums[t];  # 将index = t 上的值赋值给 nums[i]
		nums[t] = t  
```

## 9. 对象数组

	class A():
	def __init__(self, a, b):
		self.A = a
		self.B = b
		print(self.A, self.B)
		
	i = 0
	a, b = 1, 1
	obj_list = []
	
	while i < 5:	
		obj_list.append(A(a, b))
		a += 1
		b += 1
		i += 1
			
	print("++++++++++++++++++++")
	
	list_a = [i for i in range(1, 6)]
	list_b = list_a[:]	
	list(map(A, list_a, list_b))


林宙辰， 马毅， 刘光灿

## 10. 语言

```
if(nums[i]< min_num):
	min_num = nums[i]

if(nums[i]>max_num):
	max_num = nums[i]
```

数组长度 = last_index + 1

循环中要用到的变量初始化在循环体外

在判断语句中先将等于的情况考虑进去，如考虑大于等于的情况，再考虑小于



python

初始化时，将要更替为最小值的值设为  无穷大

float('inf') 表示正无穷

-float('inf') 或 float('-inf') 表示负无穷

其中，inf 均可以写成 Inf



## 11 递归

使用递归思想：一层一层调用（将函数压栈，传入每次收缩后的参数），直到递归结束条件成立，再一层一层返回（将函数返回值出栈）；

1.判断终止条件  递归出口

2.计算具有共性的那部分  递归式

3.收缩计算范围,使其趋于终止条件

在最后的部分([169页]),作者总结前面的递归例子后,将递归分这么三类,区别在于上面的第二步出现条件判断,从而发生多次回调行为:

线性递归(Linear recursion):最多只有一次函数回调

二分递归(Binary recursion):函数体内部有两次回调

多路递归(Multiple recursion):函数体内部有超过两次的回调，每次递归的顺序都相同



## 12 <=

- l <= r    等价于 l < r or l == r
- 当数组长度为奇数时，假设 l < r 的迭代次数为 n且 r-l = 1;  l <= r 的迭代次数为n+1且 r-l = 2,
- 当数组长度为偶数时， 假设 l < r 的迭代次数为 n且 r-l = 1;  l <= r 的迭代次数为n且 r-l = 1
- 通常使用  x<y

```python
a = [1, 2, 3, 4, 5]
iter = 0
l = 0
r = len(a)-1

while l < r:
	iter += 1
	print(iter)
	l += 1;
	r -= 1;
	
print('l=', l, ' r=', r)
# l= 2  r= 2

print('end')
##################################
a = [1, 2, 3, 4, 5]
iter = 0
l = 0
r = len(a)-1

while l <= r:
	iter += 1
	print(iter)
	l += 1;
	r -= 1;
	
print('l=', l, ' r=', r)
# l= 3  r= 1

print('end')

##################################

a = [1, 2, 3, 4, 5, 6]
iter = 0
l = 0
r = len(a)-1

while l < r:
	iter += 1
	print(iter)
	l += 1;
	r -= 1;
	
print('l=', l, ' r=', r)
# l= 3  r= 2

print('end')
##################################

a = [1, 2, 3, 4, 5, 6]
iter = 0
l = 0
r = len(a)-1

while l <= r:
	iter += 1
	print(iter)
	l += 1;
	r -= 1;
	
print('l=', l, ' r=', r)
# l= 3  r= 2

print('end')
```

## 13 动态规划

动态规划算法一般都有下面两种实现方式，前者我称为递归版本，后者称为迭代版本，两个版本是可以相互转换的

1. 备忘录法（递归）：直接自顶向下实现递归式，并将中间结果保存

2. 迭代法：按照递归式自底向上地迭代，将结果保存在某个数据结构中求解。

计算顺序

1.运行速度快，因为没有用栈去实现，也避免了栈溢出的情况；

2.迭代实现的话可以不使用dict来进行缓存，而是使用其他的特殊cache结构，例如多维数组等更为高效的数据结构

动态规划其实就是一个连续决策的过程，每次决策我们可能有多种选择(二项式系数和0-1背包问题中我们只有两个选择，DAG图的单源最短路径中我们的选择要看点的出边或者入边，矩阵链乘问题中就是矩阵链可以分开的位置总数…)，我们每次选择最好的那个作为我们的决策。所以，动态规划的时间复杂度其实和这两者有关，也就是子问题的个数以及子问题的选择个数，一般情况下动态规划算法的时间复杂度就是两者的乘积。

动态规划有两种实现方式：一种是带备忘录的递归形式，这种方式直接从原问题出发，遇到子问题就去求解子问题并存储子问题的解，下次遇到的时候直接取出来，问题求解的过程看起来就像是先自顶向下地展开问题，然后自下而上的进行决策；另一个实现方式是迭代方式，这种方式需要考虑如何给定一个子问题的求解方式，使得后面求解规模较大的问题是需要求解的子问题都已经求解好了，它的缺点就是可能有些子问题不要算但是它还是算了，而递归实现方式只会计算它需要求解的子问题。

##  14 while 和 for的使用时机

- for ：知道要循环的次数时使用
- while：知道循环停止的时机时使用

## 15 常用链表操作

给链表添加一个头结点，便于对链表的操作

- 快慢指针：链表循环或寻找中间节点
- 指针窗口：
- 对撞指针

## 16 知道value求key

```python
# 把字典列表化 key与对应的value有相同的index
student = {'小萌': '1001', '小智': '1002', '小强': '1003', '小明': '1004'}
print(list(student.keys())[list(student.values()).index('1004')])


def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]


print(get_key(student, '1002'))

# 利用字典表达式，把字典的key与val互换。
new_dict = {v : k for k, v in student.items()}

print(new_dict['1001'])
```

## 17 dict根据value排序

```python
>>> dic = {'a':31, 'bc':5, 'c':3, 'asd':4, '33':56, 'd':0}
>>> sorted(dic.items(), key=lambda d:d[1], reverse = False )
[('d', 0), ('c', 3), ('asd', 4), ('bc', 5), ('a', 31), ('33', 56)]
```

## 18 List删除元素

使用for循环对list操作时，应该copy一个列表（listB = listA[:]），在listA中遍历，对listB进行增删改查。

```python
A = ["123", "456", "789", "234"]
B = ["2","3","4"]

A_copy = A[:]
for i in range(len(A)):
    for j in range(len(B)):
        if B[j] not in A[i]:
            A_copy.remove(A[i])
            break
            
A_copy
# ['234']
```





滑动窗口--队列

反转---stack

