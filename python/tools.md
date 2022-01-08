# Jupyter Notebook  #

## 1 简介 ##

notebook 是一种 Web 应用，能让用户将说明文本、数学方程、代码和可视化内容全部组合到一个易于共享的文档中

## 2 常用操作

用符号？获取对象信息
用符号？？获取源代码
用Tab补全代码

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

* 使用快捷键运行
* 查看快捷键（Help->Keyboard Shortcuts）
* 快速添加单元格（A，B）
* 快速改变单元格属性（Y，M）
* 运行所有单元格（Cell菜单）
* 添加代码行数（View->Toggle Line Number）

# Anaconda

conda upgrade --all



创建环境

conda create -n env_name list of packages。

在这里，-n env_name 设置环境的名称（-n 是指名称），而 list of packages 是要安装在环境中的包的列表。conda  create -n my_env numpy。

conda create -n py3 python=3 

进入环境

OSX/Linux：source activate my_env 

Windows：activate my_env

在环境中安装包

conda install package_name

离开环境

OSX/Linux：source deactivate 

Windows：deactivate

列出环境

conda env list 

删除环境

conda env remove -n env_name

保存和加载环境

conda env export > environment.yaml 将包保存为 YAML

conda env export 输出环境中的所有包的名称（包括 Python 版本）。

environment.yaml 将导出的文本写入到 YAML 文件 environment.yaml 中

conda env create -f environment.yaml。这会创建一个新环境，而且它具有在 environment.yaml 中列出的同样的库