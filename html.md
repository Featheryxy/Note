# HTML

## 一、简介

### 1 基本架构

超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。HTML 运行在浏览器上，由浏览器来解析,大小写不敏感，推荐使用小写。

- <!-- HTML注释 -->

```html
<!-- 声明为 HTML5 文档 -->
<!DOCTYPE html> 
<html lang="en">
<head>  
    <!-- 定义网页编码格式为 utf-8。 -->
    <meta charset="UTF-8"> 
    
    
    <!-- 文档与外部资源之间的关系 -->
    <link rel="stylesheet" type="text/css" href="mystyle.css"> 
    
    <!-- 标签定义了HTML文档的样式文件引用地址 -->
    <style type="text/css">
    body {background-color:yellow}
    p {color:blue}
    </style>
    
    <title>Title</title> 
</head>
<body>
	显示可见内容
</body>
</html>
```

### 2 标记与元素（标签）

```
开始标记: <h1>
结束标记: </h1>
元素 = 开始标记 + 内容 + 结束标记
<p name="value">Nothing seek, nothing find.</p>

void元素: 空元素是在开始标签中关闭的 <br/>，  <br> 在所有浏览器中都是有效的

块元素特立独行,内敛元素随波逐流
块元素(block):显示时就好像前后各有一个换行,缩进，会以新行来开始（和结束）<div>
内敛(inline)元素:在页面文本流中总在"行内"出现 <span>
```

### 3 标签属性

属性(Attribute):  属性一般描述于开始标签，总是以**名称/值对的形式出现**，比如：name="value"

```html
<p name="value">Nothing seek, nothing find.</p>
```

- class：为html元素定义一个或多个类名（classname）(类名从样式文件引入)
- id： 定义元素的唯一id
- style：规定元素的行内样式（inline style）
- title：描述了元素的额外信息 (作为工具条使用)，鼠标悬停时显示title的值

## 二、常用标记

```html
<ul> unordered list
<ol> ordered list
<li> list item
list-style-type: 改变列表中使用的列表标记类型
List-style-image: 知道列表标记图像
    
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>

<q>today is Sunday</q>
"today is Sunday"
内敛(inline)元素:在页面文本流中总在"行内"出现

<blockquote>
     Passing cars,
     When you can't see
</blockquote>
自成一段,文字缩进
块元素(block):显示时就好像前后各有一个换行

<em> 斜体
<strong>粗体
<code>计算机代码
    
<q>短引用
<block>长引用
<p> 段落
<h1>一级标题
<br/>换行
<hr>水平线。

<a href="../index.html" target="_blank" title="跳到index页面">内容可点击</a>
..     父文件夹
/      分隔路径的各个部分
target="_blank"  打开一个新窗口
title:文本描述

    
<a id="tips">有用的提示部分</a>
在HTML文档中创建一个链接到"有用的提示部分(id="tips"）"：
<a href="#tips">访问有用的提示部分</a>
    
或者，从另一个页面创建一个链接到"有用的提示部分(id="tips"）"：
<a href="https://www.runoob.com/html/html-links.html#tips">
访问有用的提示部分</a>

<img src="images/1.jpg" alt="图片如果没有显示,则使用属性alt中的内容来替代" width="304" height="228" >
```

## 三、表格元素

```html
  <table>
      <caption>
        The cities I visited on my
        Segway'n USA travels
      </caption>
      <tr>
        <th>Ciyt</th>
        <th>Date</th>
      </tr>
      <tr>
        <td>Walla Walla,WA</td>
        <td>June 15th</td>
      </tr>

<table>标记开始整个表格
<caption>标题
<tr> 表行
<td> 数据单元格,必须嵌套在表行中
<th> 表格表头中的一个单元格,必须嵌套在表行中

caption-side: bottom; 将标题移到表格下方
border-spacing: 5px; 单元格之间的间隙
border-collapse: collapse;使单元格之间没有边框间距
tr:nth-child(2n){                           使第2n行背景颜色为粉色
        background-color: pink;
      }
rowspan="2"   合并单元格
colspan     

```

  <table>
      <caption>
        The cities I visited on my
        Segway'n USA travels
      </caption>
      <tr>
        <th>Ciyt</th>
        <th>Date</th>
      </tr>
      <tr>
        <td>Walla Walla,WA</td>
        <td>June 15th</td>
      </tr>



## 四、表单元素

```html
<form class="" action="index.html" method="post">
      <input type="text" name="fullname" placeholder="name"><br>
      <input type="password" name="" value="123" required><br>
      <input type="radio" name="hotornot" value="hot" id="yes">
      <label for="yes">hot</label>
      <input type="radio" name="hotornot" value="not" id="no">
      <label for="no">not</label><br>
      <input type="submit" name="" value="Submit"><br>
      <fieldset>
        <legend>Condiments</legend>
        <input type="checkbox" name="spice" value="Salt" checked>Salt<br>
        <input type="checkbox" name="spice" value="Pepper">Pepper<br>
        <input type="checkbox" name="spice" value="Garlic">Garlic<br>
      </fieldset>
      <br>
      <input type="number" min="0" max="10"><br>
      <input type="range" min="0" max="20" step="5"><br>
      <input type="color"><br>
      <input type="date"><br>
      <input type="email"><br>
      <input type="tel" ><br>
      <input type="url" ><br>
      <input type="file" >
      <textarea name="comments" rows="10" cols="48"></textarea><br>
      <select class="" name="characters" >
        <option value="Buckarro">Buckarro Banzai</option>
        <option value="Tommy">Perfect Tommy</option>
        <option value="Penny">Penny Priddy</option>
      </select><br>
    </form>

<textarea>文本域
<select> 菜单
    <option>菜单项
```

<form>
      <input type="number" min="0" max="10"><br>
  <input type="range" min="0" max="20" step="5"><br>
  <input type="color"><br>
  <input type="date"><br>
  <input type="email"><br>
  <input type="tel" ><br>
  <input type="url" ><br>
  <input type="file" >
</form>

各个**表单元素都有一个唯一的name,对于每个唯一的元素名.从你在表单中输入的数据中得到一个相应的值value.浏览器打包这些数据,(name, value)发送给服务器**，如果没有设置value属性，浏览器将（name， 元素内容）打包给服务器
value属性为输入域提供默认文本

```
对于不同的输入类型，value 属性的用法也不同：

type="button", "reset", "submit" - 定义按钮上的显示的文本
type="text", "password", "hidden" - 定义输入字段的初始值
type="checkbox", "radio", "image" - 定义与输入相关联的值
注释：<input type="checkbox"> 和 <input type="radio"> 中必须设置 value 属性。
注释：value 属性无法与 <input type="file"> 一同使用。
```



- placeholder属性可以为表单用户提供一个提示
- required 属性是一个布尔属性。
- required 属性规定必需在提交表单之前填写输入字段。
- action:包含服务器脚本的URL
- method:发送表单数据的方法,post或get
- name:

**type类型如下**

- text 单行文本框
- password 密码框
- radio 单选框
- checkbox 复选框
- number 只允许数字字符的单行文本输入控件
- color 颜色选择器
- date 日期选择器
- file 文件选择器