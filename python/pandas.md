# Pandas

## 简介

Pandas 名字衍生自术语 "panel data"（面板数据）和 "Python data analysis"（Python 数据分析） 

Pandas 的主要数据结构是 Series （一维数据）, DataFrame（二维数据）  和 Index(索引)

Pandas 是在 NumPy 基础上建立的新程序库，可以把它们看成增强版的 NumPy 结构化数组，行列都 不再只是简单的整数索引，还可以带上标签

Numpy不能为数据添加标签、处理缺失值, 或者需要做一些不是对每个元素都进行广播映射的计算（如分组、透视表等）时

## Series

### 简介

Series 对象是一个**带索引数据**构成的**一维数组**

data.values

data.index

```
>>> data = pd.Series([0.25, 0.5, 0.75, 1.0])
>>> data
0    0.25
1    0.50
2    0.75
3    1.00
dtype: float64
>>> data.values
array([0.25, 0.5 , 0.75, 1.  ])
>>> data.index
RangeIndex(start=0, stop=4, step=1)
```

**NumPy 数组**通过**隐式定义的整数索引**获取数值，而 Pandas 的**Series 对象**用一种**显式定义的索引与数值关联**

```
>>> data = pd.Series([0.25, 0.5, 0.75, 1.0],
... index=['a', 'b', 'c', 'd'])
>>> data
a    0.25
b    0.50
c    0.75
d    1.00
dtype: float64
>>> data['c']
0.75
```

### 取值

data[1] 这样的取值操作会使用显式索引

而 data[1:3] 这样的切片操作却会使用隐式索引。

```
>>> data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
>>> data
1    a
3    b
5    c
dtype: object
>>> data[1]
'a'
>>> data[1:3]
3    b
5    c
dtype: object
```

由于整数索引很容易造成混淆，所以 Pandas 提供了一些**索引器（indexer）**属性来作为取值的方法。它们不是 Series 对象的函数方法，而是暴露切片接口的属性。

- loc 属性，表示取值和切片都是显式
- iloc 属性，表示取值和切片都是 Python 形式的 1 隐式索引
- ix，它是前两种索引器的混合形式，在 Series 对象中 ix 等价于标准的[]（Python 列表）取值方式

ps: **“显式优于隐式”。使用 loc 和 iloc 可以让代码更容易维护，可读性更高。

```
>>> data[1]
'a'
>>> data[1:3]
3    b
5    c
dtype: object
>>> data[1]
'a'
>>> data.loc[1]
'a'
>>> data.iloc[1]
'b'
>>> data.loc[1:3]
1    a
3    b
dtype: object
>>> data.iloc[1:3]
3    b
5    c
dtype: object
```

### 转换

```python
s.apply(
    func: 'AggFuncType',
    convert_dtype: 'bool' = True,
    args: 'tuple[Any, ...]' = (),
    **kwargs,
) -> 'FrameOrSeriesUnion'
Docstring:
Invoke function on values of Series.

>>> s = pd.Series([20, 21, 12],
...               index=['London', 'New York', 'Helsinki'])
>>> s
London      20
New York    21
Helsinki    12
dtype: int64

>>> def square(x):
...     return x ** 2
>>> s.apply(square)
London      400
New York    441
Helsinki    144
dtype: int64
# 转换为str    
>>> s.apply(str)    
```



## DataFrame

### 简介

DataFrame 就可以看作是一种既有灵活的行索引，又有灵活列名的二维数组

DataFrame 是一列映射一个 Series 的数据

```
>>> states
            population    area
California    38332521  423967
Texas         26448193  695662
New York      19651127  141297
Florida       19552860  170312
Illinois      12882135  149995
>>> states.index
Index(['California', 'Texas', 'New York', 'Florida', 'Illinois'], dtype='object')
>>> states.columns
Index(['population', 'area'], dtype='object')
>>> states['area']
California    423967
Texas         695662
New York      141297
Florida       170312
Illinois      149995
Name: area, dtype: int64

>>> data
            population    area
California    38332521  423967
Texas         26448193  695662
New York      19651127  141297
Florida       19552860  170312
Illinois      12882135  149995
>>> data.iloc[:2,:2]
            population    area
California    38332521  423967
Texas         26448193  695662


```

### 取值

- `df[col_name]` 每个 Series 分别构成 DataFrame 的一列，可以通过对列名进行字典形式（dictionary-style）的取值获取数据 
- `df.values[:,[0,2], ...]` 是一个二维数组, 通过切片获取元素
- `df.iloc[:,[0,2], ...]` 隐式索引
- `df.loc[col_name]` 显示索引

```
>>> data
            population    area
California    38332521  423967
Texas         26448193  695662
New York      19651127  141297
Florida       19552860  170312
Illinois      12882135  149995

>>> data['area']
California    423967
Texas         695662
New York      141297
Florida       170312
Illinois      149995
Name: area, dtype: int64
>>> data.area
California    423967
Texas         695662
New York      141297
Florida       170312
Illinois      149995
Name: area, dtype: int64

>>> data.values
array([[38332521,   423967],
       [26448193,   695662],
       [19651127,   141297],
       [19552860,   170312],
       [12882135,   149995]], dtype=int64)
>>> data.values
array([[38332521,   423967],
       [26448193,   695662],
       [19651127,   141297],
       [19552860,   170312],
       [12882135,   149995]], dtype=int64)
>>> data.values[0]
array([38332521,   423967], dtype=int64)
>>> data.iloc[:,[0,1]]
            population    area
California    38332521  423967
Texas         26448193  695662
New York      19651127  141297
Florida       19552860  170312
Illinois      12882135  149995
```



## Index

不可变数组或有序集合, 同样有size, shape, ndim, dtype 属性

```
>>> ind = pd.Index([2, 3, 5, 7, 11])
>>> ind
Int64Index([2, 3, 5, 7, 11], dtype='int64')
>>> ind[0]
2
>>> ind[0] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Python39\lib\site-packages\pandas\core\indexes\base.py", line 4585, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations
>>> print(ind.size, ind.shape, ind.ndim, ind.dtype)
5 (5,) 1 int64
```

## 文件

```
pd.read_excel(io, dtype=str)
df | series.to_csv(io, [header=True, index=True,sep=','])
```

