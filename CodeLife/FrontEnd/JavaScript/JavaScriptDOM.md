---
title: JavaScriptDOM
date: 2019-11-23 15:17:24
tags:
	- JavaScript
categories:
	- Book
---

《JavaScript DOM编程艺术 第2版》内容摘记

<!-- more -->

## 1.  简介

### 1.1 术语

1. DOM:文档对象模型(Document Object Model)

   ​		对文档的内容进行抽象和概念化的方法。通过DOM这个接口动态地访问和修改文档的内容，结构和样式。是一种API（应用编程接口），API就是一组已经得到有关各方共同认可的基本约定。

2. BOM：浏览器对象模型

3. DHTML:动态HTML(Dynamic HTML)

   - 利用HTML把网页标记为各种元素;
   - 利用CSS设置元素样式和他们的显示位置;
   - 利用JavaScript实时地操控页面和改变样式.

### 1.2 引入

#### 1. 将JavaScript代码放到文档\<head>标签中的\<script>标签之间

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Example</title>
    <script type="text/javascript">
        javascript goes here
    </script>
    </head>
  <body>
  </body>
</html> 
```

1. 在\<head>部分放一个\<script>标签,并把它的src属性指向该文件

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Example</title>
    <script type="text/javascript"src="file.js"></script>
  </head>
  <body>
  </body>
</html> 
```

1. 将\<srcipt>标签放到\</body>标签之前,能使浏览器更快的加载页面

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Example</title>
  </head>
  <body>
    <script type="text/javascript" src="example.js"></script>
  </body>
</html> 
```



## 2. JavaScript语法

### 2.1 简介

1. JavaScript是弱类型语言，不需要进行类型声明(typing)

2. JavaScript允许程序员直接对变量赋值(assignment)，而无需事先声明(declare)

3. 一行一个语句(statament),可以不用分号结尾

4. 区分大小写

5. JavaScript只应用在Web浏览器，由浏览器进行解释和执行

6. 程序设计语言分为解释型和编译型两大类。

   - 编译型程序设计语言需要一个编译器（compiler）,编译器能将高级语言（Java）编写出来的源代码翻译为直接在计算机上执行的文件，编译型语言往往速度更快，可移植性更好

   - 解释型程序设计语言不需要编译器，仅需要解释器

```
// comment 注释

/*
多行
注释
*/

<!-- HTML comment -->

<!-- JavaScript comment

mood = "happy";

alert(mood);
```

### 2.2 数据类型

```javascript
// 1. 字符串
var mood = 'don\'t ask'
var mood = "don't ask"
// 2. 数值
var age = -20;
// 3. 布尔值
var sleeping = true;(没有引号)

// 字符串, 数值和布尔值是标量（scalar），只有一个值。
4. 数组
var beatles = Array(4);

var beatles = Array();
array[index] = element;

var beatles = new Array(4);  //new可以省略
beatles[0] = "John";
beatles[1] = "Paul";
beatles[2] = "Grorge";
beatles[3] = "Ringo";

var beatles = Array("John","Paul","Grorge","Ringo");
var beatles = ["John","Paul","Grorge","Ringo"];

var lennon = ["John", 1940, false];

var name = "John";
beatles[0] = name;

var lennon = ["John", 1940, false];
var bearles = [];
beatles[0] = lennon;

5. 关联数组(字典)
var lennon = Array();
lennon["name"] = "John";
lennon["year"] = 1940;
lennon["living"] = "false"

6. 对象
var lennon = Object();
lennon.name = "John";
lennon.year = 1940;
lennon.living = false;

var lennon = {name:"john", year:"1940", living:false}

var beatles = Array();
beatels[0] = lennon;
// beatles[0].name is "John"

var beatles = {}
beatles.vocalist = lennon;
// beatles.vocalist.name is "John"

```

### 2.3 操作符

#### 2.3.1 算术操作符

```javascript
// + - * / ++ --

// 拼接 concatenation
var message = "I am " + "23";

// += 加法和拼接
```

#### 2.3.2 比较操作符

```
>, <, >=, <=, ==(比较值), !=， ===（比较值和变量类型）
```

#### 2.3.3 逻辑操作符

```
&& 逻辑与
|| 逻辑或
!  逻辑非
```

### 2.4 流程控制

#### 2.4.1 if

```
if(condition){
  statements;
}

if(condition){
  statements;
}else{
  statements;
}

```

#### 2.4.2 while

```
while(condition){
	statements;
}

do{
	statements;
}while(condition)

```

#### 2.4.3 for

```\
initialize;
while(condition){
	statements;
	increment;
}

for(initial condition; test condition; alter condition){
	statements;
}

```

### 2.5 function

```
function name(arguments) {
	statement;
}

```

### 2.6 object

#### 2.6.1 用户定义对象

user-defined object

```
Object.property()
Object.method()

```

#### 2.6.2 内建对象 

内建对象(native object)：JavaScript预先定义好的对象

```
var beatles = new Array();
beatles.length;

var num = 7.561;
var num = Math.round(num);
alert(num);

```

#### 2.6.3 宿主对象

​		宿主对象(host object)： 不是由JavaScript语言本身而是由它的运行环境提供的。由浏览器提供的预定义对象被称为宿主对象

## 3. DOM

​		DOM(Document Object Model, 文档对象模型)是对文档的内容进行抽象和概念化的方法。是一种API（应用编程接口），API就是一组已经得到有关各方共同认可的基本约定。通过DOM这个接口动态地访问和修改文档的内容，结构和样式。

### 3.1 文档： DOM中的“D”

​		当创建了一个网页并把它加载到Web浏览器中时，浏览器就会把网页文档装换为一个文档对象

### 3.2 对象：DOM中的“O”

- user-defined object
- native object
- host object

### 3.3 模型：DOM中的“M”

​		DOM把一份文档表示为一颗节点树，使用parent， child， sibling(兄弟)等记号表明家族成员之间的关系。

### 3.4 节点

​		文档是由节点构成的集合，只不过此时的节点是文档书上的树枝和树叶而已。节点类型有三种：元素节点、文本节点和属性节点。

#### 3.4.1 元素节点

​		DOM的原子是元素节点(element node)，i.e. html元素

```
<p title="a gentle reminder">Don't forget to buy this stuff</p>

```

#### 3.4.2 文本节点

​		文本节点总是被包含在元素节点内部。

```
元素<p>中的"Don't forget to buy this stuff"就是文本节点

```

#### 3.4.3 属性节点

​		属性节点用来对元素做出更具体的描述

```
元素<p>中的title="a gentle reminder" 就是属性节点

```

#### 3.4.4 获取元素

​		文档中的每一个元素都是一个对象, 可以使用通配符“*”进行匹配

1. getElementById

   返回一个对象，该对象对应着文档里的一个特定的元素节点

   ```
   document.getElementById(id)
   
   ```

2. getElementsByTagName

   返回一个对象数组

   ```
   document.getElementsByTagName(tag)
   
   ```

3. getElementsByClassName

   返回一个对象数组

   ```
   // 可查找带有多个类名的元素，类名顺序不重要
   document.getElementsByClassName(class)
   
   ```

### 3.5 获取和设置属性

​		得到元素后可以使用getAttribute方法获取元素的属性，使用setAttribute方法更改属性节点的值, 只能作用于元素节点。

#### 3.5.1 getAttribute

```
object.getAttribute(attribute)

```

#### 3.5.2 setAttribute

```
object.setAttribute(attribute, value)

```

## 4. 案列：JavaScript图片库

### 4.1 事件处理函数

```
event = "JavaScript statement(s)"

```

​		工作机制：在给某个元素添加了事件处理函数后，一旦事件发生，相应的JavaScript代码就会得到执行。被调用的JavaScirpt代码可以返回一个值，这个值将被传递给那个事件处理函数。

```html
<a href="http://www.baidu.com" onclick="return false">Baidu</a>

```

​		当点击这个链接时，因为onclick事件处理函数所触发的JavaScript代码返回给它的值是false，所以这个链接的默认行为没有被触发。

### 4.2 子节点

```
元素：<标签名 属性="属性值">文本 </标签名>
元素节点：元素的孩子

```

#### 4.2.1 childNodes属性

​		在一颗节点树上，childNodes属性可以用来获取任何一个元素的所有子元素，返回一个包含该元素全部子元素的数组。

```
element.childNodes

```

#### 4.2.2 nodeType属性

​		文档树的节点类型并非只有元素节点一种，文档里几乎每一样东西都是一个节点，甚至连空格和换行符都会被解释为节点，也都包含在childNodes属性所返回的数组中。

​		每个节点都有nodeType属性

- 元素节点的nodeType属性值是1
- 属性节点的nodeType属性值是2
- 文本节点的nodeType属性值是3

#### 4.2.3 nodeValue属性

​		可以使用nodeValue获取和改变文本节点

```
node.nodeValue

alert(document.getElementById("description").nodeValue)
// null
alert(document.getElementById("description").childNodes[0].nodeValue)
// 


```

#### 4.2.3 firstChild和lastChild属性

```
node.firstChild
等价于
node.childNodes[0]

node.lastChild
等价于
node.childNodes[node.childNodes.length-1]

```

### 4.3 图片库

#### 4.3.1 文件结构

```
.
├--images
|  ├--1.jpg
|  ├--2.jpg
|  └── placeholder.jpg
├--scripts
|  └── showPic.js
└-- gallery.html

```

#### 4.3.2 gallery.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>Snapshots</h1>
    <ul>
      <li>
        <a href="images/1.jpg" onclick = "showPic(this); return false" title="boy">boy</a>
      </li>
      <li>
        <a href="images/2.jpg" onclick = "showPic(this); return false" title="girl">girl</a>
      </li>
    </ul>
    <img id="placeholder" src="images/placeholder.jpg" alt="my image gallery">
    <p id="description">Choose an image.</p>
    <script type="text/javascript" src="scripts/showPic.js"></script>
  </body>
</html>

```

#### 4.3.3 showPic.js

```javascript
function showPic(whichpic){
  // whichpic is element 鼠标点击的元素
  var source = whichpic.getAttribute("href")
  var placeholder = document.getElementById("placeholder")
  placeholder.setAttribute("src", source)

  var text = whichpic.getAttribute("title")
  var description = document.getElementById("description")
  // alert(description.nodeValue)
  // alert(description.childNodes[0].nodeValue)
  // alert(description.firstChild.nodeValue)
  description.firstChild.nodeValue = text
}

// function countBodyChildren(){
//   var body_element = document.getElementsByTagName("body")[0]
//   alert(body_element.childNodes.length)
//   alert(body_element.nodeType)
// }

//页面加载时运行countBodyChildren
//window.onload = countBodyChildren;

```

## 5. 最佳实践

### 5.1 平稳退化

​		平稳退化（gracefu degradation）：虽然某些功能无法使用，但最基本的操作仍能顺利完成。

```javascript
创建新的浏览窗口
window.open(url, name, [features])

function popUp(winURL){
	window.open(winURL, "popup", "width=320, height=480")
}

```

#### 5.1.1 ‘’javascript:‘’ 伪协议

```javascript
// url 必须为单引号
<a href="javascript:popUp('https://www.baidu.com/')">Baidu</a>

// 该语句仅在支持“javascript:”伪协议的浏览器中运行正常，较老的浏览器则会打开失败，不推借使用伪协议。

```

#### 5.1.2 内嵌的事件处理函数

```javascript
// "#" 未指向任何目标的内部链接
<a href="#" onclick="popUp('https://www.baidu.com/'); return false">Baidu</a>

// 如果用户已经禁止使用浏览器的JavaScript功能，链接失效

```

#### 5.1.3 平稳退化

```javascript
<a href="https://www.baidu.com/" onclick="popUp('https://www.baidu.com/'); return false">Baidu</a>

<a href="https://www.baidu.com/" onclick="popUp(this.getAttribute('href')); return false">Baidu</a>

<a href="https://www.baidu.com/" onclick="popUp(this.href; return false)); return false">Baidu</a>

```

### 5.2 分离JavaScript

​		在外部JavaScript文件里把一个事件添加到HTML文档中的某个元素上

```
element.event = action...

getElementById(id).event = action

```

```html
<a href="https://www.baidu.com/" class="popup">Baidu</a>

```

```javascript
function popUp(winURL){
	window.open(winURL, "popup", "width=320, height=480");
}

// 在文件加载时立即执行prepareLinks，避免脚本加载时文档可能不完整
window.onload = prepareLinks;
function prepareLinks(){
  var links = document.getElementsByTagName("a")
  for (var i=0; i<links.length; i++){
    if(links[i].getAttribute("class") == "popup"){
      links[i].onclick = function(){
        popUp(this.getAttribute("href"))
        return false
      }
    }
  }
}

```

## 6. 图片库改进

### 6.1 共享onload事件

```javascript
window.onload = firstFunction
window.onload = secondFunction
// 只执行secondFunction

// 为页面加载完毕时执行的函数创建为一个队列
function addLoadEvent(func){
  var oldonload = window.onload;
  if(typeof window.onload != 'function'){
    window.onload = func;
  }else {
    window.onload = function(){
      oldonload();
      func();
    }
  }
}

// 两个函数依次执行
addLoadEvent(firstFunction)
addLoadEvent(secondFunction)

```

### 6.2 图片库改进

#### 6.2.1 文件结构

```
.
├--images
|  ├--1.jpg
|  ├--2.jpg
|  └── placeholder.jpg
├--scripts
|  └── showPic.js
├--styles
|  └── layout.css
└-- gallery.html

```

#### 6.2.2 gallery.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>gallery</title>
    <link rel="stylesheet" href="styles/layout.css">
  </head>
  <body>
    <h1>Snapshots</h1>
    <ul id="imagegallery">
      <li>
        <a href="images/1.jpg" title="boy">
          <img src="images/1.jpg" alt="boy">
        </a>
      </li>
      <li>
        <a href="images/2.jpg" title="girl">
          <img src="images/2.jpg" alt="boy">
        </a>
      </li>
    </ul>
    <img id="placeholder" src="images/placeholder.jpg" alt="my image gallery">
    <p id="description">Choose an image.</p>
    <script type="text/javascript" src="scripts/showPic.js"></script>
  </body>
</html>

```

#### 6.2.3 showPic.js

```javascript
// window.onload = prepareGallery
// window.onload = firstFunction
// window.onload = secondFunction
// 只执行secondFunction

addLoadEvent(prepareGallery)
function prepareGallery(){
  if(!document.getElementsByTagName) return false;
  if(!document.getElementById) return false;
  if(!document.getElementById("imagegallery")) return false;
  var gallery = document.getElementById("imagegallery")
  var links = gallery.getElementsByTagName("a")
  for(var i=0; i<links.length; i++){
    links[i].onclick = function(){
      // showPic(this)
      // return false
      // 如果showPic返回true,更新placeholder
      // if(showPic(this)){
      //   return false;
      // }else {
      //   return true
      // }
      return showPic(this)? false:true;
    }
  }
}

function showPic(whichpic){
  // whichpic is element 鼠标点击的元素
  var source = whichpic.getAttribute("href")
  var placeholder = document.getElementById("placeholder")
  placeholder.setAttribute("src", source)

  var text = whichpic.getAttribute("title")
  var description = document.getElementById("description")
  // alert(description.nodeValue)
  // alert(description.childNodes[0].nodeValue)
  // alert(description.firstChild.nodeValue)
  description.firstChild.nodeValue = text

  return true
}

// 为页面加载完毕时执行的函数创建为一个队列
function addLoadEvent(func){
  var oldload = window.onload;
  if(typeof window.onload != 'function'){
    window.onload = func;
  }else {
    window.onload = function(){
      oldonload();
      func();
    }
  }
}

```

#### 6.2.4 layout.css

```css
#imagegallery{
  list-style: none;
}

#imagegallery li{
  display: inline;
}
body{
  font-family: "helvetica", "Arial", serif;
  color: #333;
  background-color: #ccc;
  margin: 1em 10%
}

```

### 6.3 DOM Core和HTML-DOM

​		DOM Core并不专属于JavaScript，支持DOM的任何一种程序设计语言都可以使用它们。

```javascript
document.getElementsByTagName("form")
-->
document.forms

element.getAttribute("src")
-->
element.src

var source = whichpic.getAttribute("href")
-->
var source = whichpic.href

```

## 7. 动态创建标签

​		通过创建新元素和修改现有元素来改变网页结构

### 7.1 一些传统方法

#### 7.1.1 document.write

```javascript
<script type="text/javascript">
    document.write("<p>This is inserted</p>");
</script>

```

#### 7.1.2 innerHTML属性

​		innerHTML属性可以用来读、写谋给定元素里的HTML内容。是HTML专有属性，不能用于任何其他标记语言文档。

1. 读

```html
<div class="" id="testdiv">
	<p>This is <em>my</em> content.</p>
</div>

```

```javascript
window.onload = function(){
  var testdiv = document.getElementById("testdiv")
  alert(testdiv.innerHTML)
}
// <p>This is <em>my</em> content.</p>

```

2. 写

```html
<div class="" id="testdiv">
</div>

```

```javascript
window.onload = function(){
  var testdiv = document.getElementById("testdiv")
  testdiv.innerHTML = "<p>This is <em>my</em> content.</p>"
}

```

### 7.2 DOM方法

​		改变DOM节点树，文档在浏览器里的呈现效果就会发生变化。不过，不改变文档的物理内容，如果用文本编辑器去打开该文档，文档没有发生任何变化。

#### 7.2.1 createElement方法

​		createElement创建的元素有两个属性nodeName和nodeType。

```JavaScript
document.createElement(nodeName)

window.onload = function(){
  var para = document.createElement("p")
  var info = "nodeName: ";
  info += para.nodeName
  info += "  nodeType: "
  info += para.nodeType;
  alert(info)
  // nodeName: P  nodeType: 1
}

```

#### 7.2.2 appendChild方法

​		将新建的节点插入文档的节点树的最简单方法就是让它成为这个文档某个现有节点的一个子节点

```javascript
parent.appendChild(child)

  var testdiv = document.getElementById("testdiv")
  var para = document.createElement("p")
  testdiv.appendChild(para)

```

#### 7.2.3 createTextNode方法

​		为新建的节点创建文本节点

```javascript
document.createTextNode(text)

window.onload = function(){
  var testdiv = document.getElementById("testdiv")
  var para = document.createElement("p")
  testdiv.appendChild(para)

  var txt = document.createTextNode("Hello world")
  para.appendChild(txt)
}

```

### 7.3 重回图片库

```javascript
// 在已有元素前插入一个新元素
parentElement.insertBefore(newElement, targetElement)
// targetElement.parentNode 就是 parentElement，元素节点的父元素必须是另一个元素节点（不是文本节点和属性节点）

// 在现有方法后插入一个新元素
parentElement.insertAfter(newElement, targetElement)

function insertAfter(newElement, targetElement){
  var parent = targetElement.parentNode;
  if (parent.lastChild == targetElement){
    parent.appendChild(newElement)
  }else {
    parent.insertBefore(newElement, targetElement.nextSibling)
  }
}

```

#### 7.3.1 gallery.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>gallery</title>
    <link rel="stylesheet" href="styles/layout.css">
  </head>
  <body>
    <h1>Snapshots</h1>
    <ul id="imagegallery">
      <li>
        <a href="images/1.jpg" title="boy">
          boy
          <!-- <img src="images/1.jpg" alt="boy"> -->
        </a>
      </li>
      <li>
        <a href="images/2.jpg" title="girl">
          girl
          <!-- <img src="images/2.jpg" alt="boy"> -->
        </a>
      </li>
    </ul>
    <!-- <img id="placeholder" src="images/placeholder.jpg" alt="my image gallery"> -->
    <!-- <p id="description">Choose an image.</p> -->
    <script type="text/javascript" src="scripts/showPic.js"></script>
  </body>
</html>

```

#### 7.3.2 showPic.js

```javascript
function addLoadEvent(func){
  var oldonload = window.onload;
  if(typeof window.onload != 'function'){
    window.onload = func;
  }else {
    window.onload = function(){
      oldonload();
      func();
    }
  }
}

function insertAfter(newElement, targetElement){
  var parent = targetElement.parentNode;
  if (parent.lastChild == targetElement){
    parent.appendChild(newElement)
  }else {
    parent.insertBefore(newElement, targetElement.nextSibling)
  }
}

function preparePlaceholder(){
  var placeholder = document.createElement("img")
  placeholder.setAttribute("id", "placeholder")
  placeholder.setAttribute("src", "images/placeholder.jpg")
  var description = document.createElement("p")
  description.setAttribute("id", "description")
  var desctext = document.createTextNode("Choose an image")
  description.appendChild(desctext)

  var gallery = document.getElementById("imagegallery")
  insertAfter(placeholder, gallery)
  insertAfter(description, placeholder)
}

function prepareGallery(){
  if(!document.getElementsByTagName) return false;
  if(!document.getElementById) return false;
  if(!document.getElementById("imagegallery")) return false;
  var gallery = document.getElementById("imagegallery")
  var links = gallery.getElementsByTagName("a")
  for(var i=0; i<links.length; i++){
    links[i].onclick = function(){
      // showPic(this)
      // return false
      // 如果showPic返回true,更新placeholder
      // if(showPic(this)){
      //   return false;
      // }else {
      //   return true
      // }
      return showPic(this)? false:true;
    }
  }
}

function showPic(whichpic){
  // whichpic is element 鼠标点击的元素
  var source = whichpic.getAttribute("href")
  var placeholder = document.getElementById("placeholder")
  placeholder.setAttribute("src", source)

  var text = whichpic.getAttribute("title")
  var description = document.getElementById("description")
  description.firstChild.nodeValue = text

  return true
}

addLoadEvent(preparePlaceholder)
addLoadEvent(prepareGallery)

```

### 7.4 Ajax

​		Ajax用于异步加载页面内容，对页面的请求以异步方式发送到服务器，而服务器不会用整个页面来响应请求。

#### 7.4.1 XMLHTTPRequest对象

​		XMLHTTPRequest对象充当浏览器中的脚本（客户端）与服务器之间的中间人的角色。





## 11. HTML5

### 11.1 简介

Web设计，三层

1. 结构层
2. 样式层
3. 行为层

对应的技术

1. 超文本标记语言（HTML）
2. 层叠样式表（CSS）
3. JavaScript和文档对象模型（DOM）

HTML5是该三层的集合