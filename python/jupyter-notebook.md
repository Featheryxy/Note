# Jupyter Notebook

## 1 简介

notebook 是一种 Web 应用，能让用户将说明文本、数学方程、代码和可视化内容全部组合到一个易于共享的文档中

## 2 常用操作

用符号？获取对象信息
用符号？？获取源代码
用Tab补全代码

```python
L = [1, 2, 3]
len(L)
len?
L?
len??

```

## 3 魔法命令

%lsmagic 列出其他魔法命令

line magic: 以%为前缀，用于单行输入
cell magic: 以%%为前缀，用于多行输入

%run 执行外部代码
%timeit 计算代码运行时间  多次执行
%%timeit 计算多行代码运行时间 多次执行

% time 单次执行

%history 获取历史记录
%xmode Plain|Context(default)|Verbose

## 4 In， Out对象

In列表对象
Out字典对象

print(_)输出上一个变量
print(__)输出倒数第二个变量
Out[2] 等价于 _2

## 5 matplotlib

在分辨率较高的屏幕（例如 Retina 显示屏）上，notebook 中的默认图像可能会显得模糊。可以在 %matplotlib inline 之后使用 %config InlineBackend.figure_format = 'retina' 来呈现分辨率较高的图像。

## 6 快捷键

- 使用快捷键运行
- 查看快捷键（Help->Keyboard Shortcuts）
- 快速添加单元格（A，B）
- 快速改变单元格属性（Y，M）
- 运行所有单元格（Cell菜单）
- 添加代码行数（View->Toggle Line Number）