# Numpy #

[TOC]

| shape       | (1， | 2，           | 1）          |
| ----------- | ---- | ------------- | ------------ |
| AXIS        | z    | y             | x            |
| axis        | 0    | 1             | 2            |
| information |      | raw           | column       |
|             |      | Vertical axis | horizon axis |

## 一、 Array ##

NumPy数组：列表中的每个元素的类型是一样的, 如果类型不匹配，NumPy 将会向上转换（如果可行）, 减少存储空间

Python列表: 列表中的每个元素都是一个独立的对象, 每一项必须包含各自的类型信息、引用计数和其他信息

``array``的缺点是没有将数据当做向量或者矩阵，不支持基本运算。

### 1.1 数组自动向上转型

	>>> np.array([1, 2.0])
	array([1., 2.])

### 1.2 使用dtype关键字设置数组的数据类型
```python
>>> np.array([1, 2, 3, 4], dtype = 'float32')
array([1., 2., 3., 4.], dtype=float32)
```

### 1.3 嵌套列表构成多维数组
	>>> np.array([range(i, i+3) for i in [2, 4, 6]])
	array([[2, 3, 4],
		   [4, 5, 6],
		   [6, 7, 8]])

### 1.4 数组维度

| shape       | (1， | 2，           | 1）          |
| ----------- | ---- | ------------- | ------------ |
| AXIS        | z    | y             | x            |
| axis        | 0    | 1             | 2            |
| information |      | raw           | column       |
|             |      | Vertical axis | horizon axis |

- 数组维度:[]的数量

- 矩阵维度: 表示一个值的位置时所需要的坐标的数量

```
>>> x = np.array([[1,2], [3,4], [5, 6]])
>>> x
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> x.shape
(3, 2)

>>> a = np.arange(6)
>>> a
array([0, 1, 2, 3, 4, 5])
>>> a.shape
(6,)
# 代表一个列向量，6*1

>>> x = np.ones((1,2,1), np.uint8)
>>> x
array([[[1],
        [1]]], dtype=uint8)
        
# 第一个[]中有[[1]，[1]], 第二个[]中有[]有[1]，[1], 第三个[]中有1,所以维度为: 1*2*1
# 1*2*1
# axis: 1,2,3
# AXIS: z,y,x
# 最内层为x，次内层为y， 最外层为z
>>> x.shape
(1, 2, 1)
>>> x[:,:,0]
array([[1, 1]], dtype=uint8)

# x[:，:]
# 如果索引中有:，则本轴存在;
# 如果只是一个数，则本轴消失
```

## 二、Create Array

shape -> tuple or int e.g. (2, 3) or 2

- np.zeros(shape, dtype=float, order='C')
- np.ones(shape, dtype=None, order='C')
- np.full(shape, fill_value, dtype=None, order='C')
- np.arange([start,] stop[, step,], dtype=None)
	 np.linspace(start, stop, num=50, endpoint=True, retstep=False, 	dtype=None)
- np.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')
- np.diag(v, k=0) --> Extract a diagonal or construct a diagonal array
- fromiter(iterable, dtype, count=-1) --> Create a new 1-dimensional array from an iterable object

```
>>>np.eye(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

>>> np.eye(3, 4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.]])
       
>>> np.diag(np.arange(1,5))
array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]])
       
>>> x
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> np.diag(x)
array([0, 4, 8])       
```



## 三、Array Attribute

- ndim: 维度

- shape --> tuple e.g. (10, ) 只有一个维度， 在第一个维度上的元素数量为10

- size： 元素数量

- arr.astype(dtype, copy=True) --> **Copy** of the array, cast to(强制转换) a specified type

- dtype(obj, align=False, copy=False) --> Create a data type object.




  ```
  >>> x = np.arange(10)
  >>> x
  >>> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  >>> X = np.arange(15).reshape((3, 5))
  >>> X
  >>> array([[ 0,  1,  2,  3,  4],
  >>> [ 5,  6,  7,  8,  9],
  >>> [10, 11, 12, 13, 14]])
  >>> x.ndim
  >>> 1
  >>> X.ndim
  >>> 2
  >>> x.shape
  >>> (10,)
  >>> X.shape
  >>> (3, 5)
  >>> x.size
  >>> 10
  >>> X.size
  >>> 15
  
  >>> x = np.array([1, 2, 2.5])
  >>> x
  array([ 1. ,  2. ,  2.5])
  >>> x.dtype
  dtype('float64')
  
  >>> x.astype(int)
  array([1, 2, 2])
  
  >>> x
  array([1. , 2. , 2.5])
  
  >>> x.dtype()
  dtype('float64')
  
  ```


## 四、数组切片

**X[0] == X[0,:]**

x[start: stop: step]
x[ : : ] 默认为start = 0， stop = 维度大小， step = 1

多维数组中，可以用逗号分隔的索引元组获取元素

**数组切片返回的是数组数据的视图**（修改视图即在原数组上修改），而不是数值数据的副本
**python列表中，切片是值的副本**

Numpy使用copy()实现创建数组的副本
 x2_sub_copy = x2_sub.copy()

### 1 一维数组


	>>> x
	array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	# 每隔一个元素
	>>> x[::2]
	array([0, 2, 4, 6, 8])
	# 从索引5开始每隔一个元素逆序
	>>> x[5::-2]
	array([5, 3, 1])

### 2 多维数组

	>>> x2
	array([[12,  5,  2,  4],
	       [ 7,  6,  8,  8],
	       [ 1,  6,  7,  7]])
	# 前两行，前三列
	>>> x2[:2, :3]
	array([[12,  5,  2],
	       [ 7,  6,  8]])
	# 前三行，每隔一列
	>>> x2[:3, ::2]
	array([[12,  2],
	       [ 7,  8],
	       [ 1,  7]])
	# 每隔两列
	>>> x2[:3, ::2]
	array([[12,  2],
	       [ 7,  8],
	       [ 1,  7]])
	# 第一行 
	>>> x2[0,:]
	array([12,  5,  2,  4])
	>>> x2[0]
	array([12,  5,  2,  4])


## 五、数组变形

- n维数组以一维线性存放，reshape前后，数据无变化，只是访问方式变了，先填充x,后y,次z
- reshape(array, newshape, order='C') --> Copy of a array with newshape
- newshape--> int or tuple  **e.g**. (-1, 1) 任意行，一列
- 在一个切片操作中利用 newaxis 关键字
- 将向量转换成矩阵 reshape(1， -1)


	>>> x = np.array([1, 2, 3])
	>>> x.reshape(1, -1)
	array([[1, 2, 3]])
	>>> x
	array([1, 2, 3])
	>>> x.shape
	(3,)
	>>> x1 = x.reshape(1, -1)
	>>> x1.shape
	(1, 3)


	>>> x = np.arange(1, 10)
	>>> x
	array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
	>>> x.reshape(3, 3)
	array([[1, 2, 3],
	       [4, 5, 6],
	       [7, 8, 9]])
	
	# -1代表任意行
	>>> x.reshape(-1, 1)
	array([[1],
	       [2],
	       [3],
	       [4],
	       [5],
	       [6],
	       [7],
	       [8],
	       [9]])
	
	# 通过np.newaxis获得的列向量
	>>> x[:, np.newaxis]
	array([[1],
	       [2],
	       [3],
	       [4],
	       [5],
	       [6],
	       [7],
	       [8],
	       [9]])


## 六、数组拼接

- concatenate((a1, a2, ...), **axis=0**, out=None). **ps：** **(a1, a2, ...) have the same shape**
- np.vstack((a1, a2， ...))
- np.hstack((a1, a2， ...))

### 1 concatenate


	>>> x = np.array([1, 2, 3])
	>>> y = np.array([3, 2, 1])
	>>> np.concatenate(（x, y）)
	array([1, 2, 3, 3, 2, 1])
	
	>>> grid = np.array([[1, 2, 3], [4, 5, 6]])
	>>> grid
	array([[1, 2, 3],
	       [4, 5, 6]])
	>>> np.concatenate((grid, grid), axis=0)
	array([[1, 2, 3],
	       [4, 5, 6],
	       [1, 2, 3],
	       [4, 5, 6]])
	>>> np.concatenate((grid, grid), axis=1)
	array([[1, 2, 3, 1, 2, 3],
	   	   [4, 5, 6, 4, 5, 6]])
	
	>>> x1 = x.reshape(1, -1)
	>>> x1
	array([[1, 2, 3]])
	>>> np.concatenate((grid, x1))
	array([[1, 2, 3],
	       [4, 5, 6],
	       [1, 2, 3]])


### 2 vstack and hstack

	>>> x = np.array([1, 2, 3])
	>>> grid = np.array([[9, 8, 7], [6, 5, 4]])
	>>> np.vstack([x, grid])
	array([[1, 2, 3],
	       [9, 8, 7],
	       [6, 5, 4]])
	
	>>> y = np.array([[99], [99]])
	>>> np.hstack([grid, y])
	array([[ 9,  8,  7, 99],
	       [ 6,  5,  4, 99]])


## 七、 数组分割

- np.split(ary, indices_or_sections, axis=0)
  - indices_or_sections : int or 1-D array
- np.hsplit(ary, indices_or_sections)
- np.vsplit(ary, indices_or_sections)

### 1 split

	>>> x = [1, 2, 3, 99, 99, 3, 2, 1]
	>>> x1, x2, x3 = np.split(x, [3, 5])
	>>> print(x1, x2, x3)
	[1 2 3] [99 99] [3 2 1]
	
	>>> A = np.arange(12).reshape((4, 3))
	>>> A
	array([[ 0,  1,  2],
	       [ 3,  4,  5],
	       [ 6,  7,  8],
	       [ 9, 10, 11]])
	>>> A1, A2 = np.split(A, [2])
	>>> A1
	array([[0, 1, 2],
	       [3, 4, 5]])
	>>> A2
	array([[ 6,  7,  8],
	       [ 9, 10, 11]])
	>>> A1, A2 = np.split(A, [2], axis=1)
	>>> A1
	array([[ 0,  1],
	       [ 3,  4],
	       [ 6,  7],
	       [ 9, 10]])
	>>> A2
	array([[ 2],
	       [ 5],
	       [ 8],
	       [11]])

### 2 hsplit and vsplit

	>>> left, right = np.hsplit(grid, [2])
	>>> left
	array([[ 0,  1],
	       [ 4,  5],
	       [ 8,  9],
	       [12, 13]])
	>>> right
	array([[ 2,  3],
	       [ 6,  7],
	       [10, 11],
	       [14, 15]])
	
	>>> data = np.arange(16).reshape((4, 4))
	>>> data
	array([[ 0,  1,  2,  3],
	       [ 4,  5,  6,  7],
	       [ 8,  9, 10, 11],
	       [12, 13, 14, 15]])
	>>> X, y = np.hsplit(data, [-1])
	>>> X
	array([[ 0,  1,  2],
	       [ 4,  5,  6],
	       [ 8,  9, 10],
	       [12, 13, 14]])
	>>> y
	array([[ 3],
	       [ 7],
	       [11],
	       [15]])
	>>> y[: 0]
	array([], shape=(0, 1), dtype=int32)
	>>> y[:, 0]
	array([ 3,  7, 11, 15])

## 八、Computation

### 1 Array 

	>>> A
	array([[ 0,  1,  2,  3],
	       [ 4,  5,  6,  7],
	       [ 8,  9, 10, 11],
	       [12, 13, 14, 15]])
	>>> A + 1
	array([[ 1,  2,  3,  4],
	       [ 5,  6,  7,  8],
	       [ 9, 10, 11, 12],
	       [13, 14, 15, 16]])

### 2 Matrix

	>>> A
	array([[0, 1],
	       [2, 3]])
	>>> B
	array([[10, 10],
	   	   [10, 10]])
	
	>>> A + B
	array([[10, 11],
	       [12, 13]])
	
	# * 对应元素相乘 hamdam积
	# dot() 点乘
	>>> A * B
	array([[ 0, 10],
	       [20, 30]])
	>>> A.dot(B)
	array([[10, 10],
	       [50, 50]])
	>>> A.T
	array([[0, 2],
	   	   [1, 3]])

### 3 Bordcast

- np.tile(A, reps)
 - reps: The number of repetitions of `A` along each axis. **e.g.** (2, 1)


	>>> v = np.array([1, 2])
	>>> np.tile(v, (2, 1))
	array([[1, 2],
	       [1, 2]])
	
	>>> np.vstack([v] * 2)
	array([[1, 2],
	       [1, 2]])

### 4 向量和矩阵的运算

#### 4.1 加法

	>>> v = np.array([1, 2])
	>>> A
	array([[0, 1],
	       [2, 3]])
	>>> v + A	
	array([[1, 3],
	       [3, 5]])

#### 4.2 乘法

- **array([1, 2]) 可能是行向量，也可能是列向量，在乘法运算中自动判断**


	>>> v
	array([1, 2])
	>>> A
	array([[0, 1],
	       [2, 3]])
	>>> v * A
	array([[0, 2],
	       [2, 6]])
	# vA
	>>> v.dot(A)
	array([4, 7])
	# Av
	>>> A.dot(v)
	array([2, 8])

### 5 矩阵的逆

- np.linalg.inv(a)


	>>> A
	array([[0, 1],
	       [2, 3]])
	>>> np.linalg.inv(A)
	array([[-1.5,  0.5],
	       [ 1. ,  0. ]])

### 6 矩阵的伪逆

- np.linalg.pinv(a)
	

```python
>>> X
array([[ 0,  1,  2,  3,  4,  5,  6,  7],
[ 8,  9, 10, 11, 12, 13, 14, 15]])
>>> np.linalg.inv(X)
Traceback (most recent call last):
>>> pinvX = np.linalg.pinv(X)
>>> pinvX
array([[-1.35416667e-01,  5.20833333e-02],
[-1.01190476e-01,  4.16666667e-02],
[-6.69642857e-02,  3.12500000e-02],
[-3.27380952e-02,  2.08333333e-02],
[ 1.48809524e-03,  1.04166667e-02],
[ 3.57142857e-02, -1.04083409e-17],
[ 6.99404762e-02, -1.04166667e-02],
[ 1.04166667e-01, -2.08333333e-02]])

>>> X.dot(pinvX)
array([[  1.00000000e+00,  -9.71445147e-17],
[ -1.33226763e-15,   1.00000000e+00]])
```



## 九、 arg 运算

- arg： 表示使目标函数取最小值时的变量值
- np.argmin(a, axis=None, out=None)
- np.argsort(a, axis=-1, kind='quicksort', order=None) --> Returns the indices that would sort an array
- np.partition(a, kth, axis=-1, kind='introselect', order=None)

````
>>> x = np.array([3, 1, 2])
>>> np.argsort(x)
array([1, 2, 0])
````



## 十、Fancy Indexing and 比较

### 1 Fancy Indexing

	>>> x = np.array([1, 2, 3, 4, 5])
	>>> ind = [1, 2]
	>>> x[ind]
	array([2, 3])
	
	>>> X
	array([[ 0,  1,  2,  3],
	   [ 4,  5,  6,  7],
	   [ 8,  9, 10, 11],
	   [12, 13, 14, 15]])
	>>> row = np.array([0, 1, 2])
	>>> col = np.array([1, 2, 3])
	>>> X[row, col]
	array([ 1,  6, 11])


### 2 比较

- 数组的比较运算结果是一个布尔数组


	>>> x = np.array([1, 2, 3, 4, 5])
	>>> x < 3
	array([ True,  True, False, False, False])
	>>> (2 * x) == (x ** 2)
	array([False,  True, False, False, False])
	
	>>> x = np.array([[5, 0, 3, 3], [7, 9, 3, 5], [2, 4, 7, 6]])
	>>> print(x)
	[[5 0 3 3]
	 [7 9 3 5]
	 [2 4 7 6]]
	>>> np.count_nonzero(x < 6)
	8
	# x < 6的结果是一个布尔数组，False被解释成0，True 被解释成11 
	>>> np.sum(x < 6)
	8
	# 每行有多少值小于6
	>>> np.sum(x < 6, axis=1)
	array([4, 2, 2])
	# 有任意值大于8
	>>> np.any(x > 8)
	True
	# 所有值小于10
	>>> np.all(x < 10)
	True
	
	# 每行值小于8
	>>> np.all(x < 8, axis=1)
	array([ True, False,  True])

### 3 掩码

使用布尔数组作为掩码，通过该掩码选择数据的子数据集在原array中**获得满足结果的array向量**

	>>> X
	array([[0, 1, 2],
	       [3, 4, 5],
	       [6, 7, 8]])
	>>> X[X % 3 == 0]
	array([0, 3, 6])


​	



|    shape    | (1， |      2，      |     1）      |
| :---------: | :--: | :-----------: | :----------: |
|    AXIS     |  z   |       y       |      x       |
|    axis     |  0   |       1       |      2       |
| information |      |      raw      |    column    |
|             |      | Vertical axis | horizon axis |

## 十一 random

- rand(d0, d1, ..., dn)-->Random values in a given shape

- random --> Return random floats in the half-open interval [0.0, 1.0)

- uniform(low=0.0, high=1.0, size=None) --> Draw samples from a uniform distribution.

- randint(low, high=None, size=None, dtype='l') --> Return random integers from `low` (inclusive) to `high` (exclusive)

- choice(a, size=None, replace=True, p=None) --> Generates a random sample from a given 1-D array

- normal(loc=0.0, scale=1.0, size=None)

- permutation(x) -->  ndarray  Permuted sequence or array range


```
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

nan
False
False
nan
True
False

>>> np.random.permutation(10)
array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6])
```

## PS

- np.mean
- np.std
- np.abs
- np.sqrt
- np.ceil
- np.floor
- np.trunc
- np.around
- np.array_equal(a1, a2) --> True if two arrays have the same shape and elements, False otherwise.
- np.ndenumerate(arr)--> Return an iterator yielding pairs of array coordinates and values

```python
>>>X = np.arange(11)
>>>X[(3 < X) & (X <= 8)] *= -1
>>>X

array([ 0,  1,  2,  3, -4, -5, -6, -7, -8,  9, 10])

# np.intersect1d(ar1, ar2, assume_unique=False)
# Find the intersection(交集) of two arrays.
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(Z1, Z2)
Z = Z1[Z1 == Z2]
print(Z)
print(np.intersect1d(Z1,Z2))

[4 3 1 2 9 9 4 1 8 9] [3 9 3 6 1 2 2 9 5 7]
[]
[1 2 3 9]


Z = np.arange(9).reshape((3, 3))
for index, value in np.ndenumerate(Z):
    print(index, value)
    
(0, 0) 0
(0, 1) 1
(0, 2) 2
(1, 0) 3
(1, 1) 4
(1, 2) 5
(2, 0) 6
(2, 1) 7
(2, 2) 8
```



