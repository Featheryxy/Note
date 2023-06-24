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

### 2 标记与元素

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

### 3 属性


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

# CSS

## 一、简介

## 二、选择器

### 1. 引入方式

```
CSS引入方式
1.外部引用：在<head>元素下引入:<link rel="stylesheet" href="index.css">
    可以指定多个样式表,一个样式表会覆盖在它上面链接的样式表中的样式
2.在CSS文件中导入: @import url(xx.css)
3.内部样式表：在style元素下写样式: <style media="screen">       </style>
4.内联样式：在元素标签里直接设定: <p style="color: red">
```

### 2. ID选择器 # 

一个元素只能有一个id,不过可以属于多个类

```
<h1 id="header">

#header{
  color: yellow;

}
```

### 3. 类选择器 .

一个元素可以属于多个类,多个元素可以属于一个类。同级显示css文件中的最后一个规则

```
<p class="yellow red"> //将<p>元素加入yellow类和red类

.yellow.pink{ //
       color: yellow
}

.pink{ //pink类下的所有元素

}

p.pink{ //pink类下的p元素
	

}
```

### 4. 伪类选择器  : 

Pseudo-class

```
a:link{
  color: yellow;
}

a:visited{
  color: gray;
}

a:hover{
  color: pink;
}
```

### 5. 元素选择器 h1

```
h1,h2{
   color: green;
}
```

### 6. 后代(子孙)选择器 div h2

```
div h2{
  color: pink;
}

父元素和子孙元素名之间有一个空格
选择div子孙的所有<h2>

#elixirs h2{

}
选择类名为elixirs的所有<h2>
```

### 7. 叠加规则

1. "层叠" :计算特定性,特定性越高,则应用该规则

2. 特定性数相同,则以其出现的顺序排队,最后出现的会覆盖前面的

| 0    | 0    | 0    |
| ---- | ---- | ---- |

- 百位: ID选择器

- 十位:类选择器和伪类选择器

- 个位:属性选择器

## 三、常用样式

```
font-family : 字体样式
font-size : 字体大小
	关键字:指定body默认字体大小
	em, % ,相对于body字体大小指定其他元素字体大小
	px
color : 文本颜色
text-align: 文本对齐
font-weight : 字体粗细
text-decoration : 
	underline
	overline
	line-through
background: 背景颜色
	        background: rgb(100, 102, 0);
	        background: rgb(10%, 50%, 130%);
	        background: #cc6600;
	        background: red;
Line-height: 行高


background-color：背景颜色

```

## 四、盒模式

每个元素都可以有一个边框

![](picture/盒模式.png)

```
background-image: url(images/2.jpg);
background-position: top left;
background-repeat: repeat;
	no-repeat 
	repeat-x  图像只在水平方向上重复
	inherit 按父元素的设置来处理
Width:设定内容区的宽度

默认地,背景图像会"平铺",也就是反复来填满整个背景空间

padding-top: 0px;                          
padding-right: 20px;
padding-bottom: 30px;
padding-left: 10px;

简化
顺时针
padding: 0px 20px 30px 10px;
		 上	 右	  下	  左

margin: 20px 20px 20px 20px;
简化
margin: 20px;

```



## 五、div 

- 使用div标记逻辑区(页面上彼此相关的一组元素)

- div元素后面有一个<br>
- 利用<span>将相关的内联元素和文本归组在一起

## 六、布局

### 1. 流

流:浏览器从HTML文件最上面开始,从上到下沿着元素流逐个显示所遇到的各个元素.

在每一个块元素之间加一个换行,

两个块元素上下放置时,它们共同的外边距会折叠在一起,它们之间的高度为最大的外边距高度

内联元素在水平方向上相互挨着,总体上内联元素在块元素会从左上方流向右下方.

两个内联元素并排放置时,且都有外边距,则两个元素之间的空间为两外边距之和

 

如果一个元素嵌套在另一个元素中,且都有外边距时,只要两个垂直外边距碰到一起,它们就会发生折叠.

注意:如果外面的元素有一个边框,那么两个元素的外边距就不会碰到一起

### 2. 流体布局(liquidlayouts)

扩展浏览器窗口时,页面中的内容会扩展以适应页面

float: right;  

浏览器遇到浮动元素,首先向右浮动一个元素.然后它下面的所有内容会绕流这个元素

即会把浮动元素尽可能放在右边.还会从流中删除这个段落,就好像它浮在页面上

由于浮动段落已从正常的流中删除,所以其他块元素会补上去,

即浮动元素放在块元素之上,不会影响正常的页面流

不过,内联元素会考虑浮动元素的边界,围绕着浮动元素

如果要浮动一个元素,必须为其设定一个宽度

分栏:

让外边距和边栏宽度相近

clear:

当元素流入页面时,在这个元素的左边,右边或两边不允许有浮动内容

### 3. 冻结布局(frozenlayouts)

其中内容的宽度是固定的,不会随着浏览器窗口扩展或收缩

将所有元素放在一个div中,并对div设置样式

​      .all{

​        width: 800px;

​        padding-top: 10px;

​        padding-bottom: 10px;

​        background-color: pink;

​      }

### 4. 凝胶布局(Jello layouts)

内容宽度是固定的,但是外边距会随着浏览器窗口扩展或收缩

​      .all{

​        width: 800px;

​        padding-top: 10px;

​        padding-bottom: 10px;

​        background-color: pink;

​        margin: auto;

​      }

## 七、CSS表格

1.创建一个<div>元素表示整个表格,行和列要嵌套在这个<div>中

2.对于表格中的每一行,要创建一个<div>,其中包含行内容

3.对于每一列,只需要一个块元素作为该列内容

将页面中的所有元素加入到一个div中,为其设定样式display: table;

将每一行的所有元素加入到一个div中,为其设定样式display: table-row; 

将每一个单元格中的元素加入到一个div中,为其设定样式display: table-cell;

display: table; 告诉<div>要想表格一样摆放

display: table-row; 表格中的一行

display: table-cell; 表格的一列

 

vertical-align: top; 内容相对于单元格上边对齐

border-spacing: 10px; 为表格中的单元格增加10像素的边框间距.

相当于常规元素的外边距.

##  八、定位

​    \#middle{

​      position: absolute;

​      top: 300px;

​      left: 600px;

​      width: 150px;

​    }

从流中删除,且流中的元素不会将其内联内容围绕在

一个绝对元素周围,会被绝对元素覆盖.

 

绝对元素可以相互叠加,利用z-index属性决定谁在上面

z-index: auto;

position: fixed;

固定定位,将元素放在相对于浏览器窗口的一个位置上(而不是相对于页面)

position: relative;

相对定位,让元素正常地流入页面,然后按指定的量偏移,从而留出它们原先所在的空间

position: absolute;

绝对定位,从流中删除,默认地会相对于页面边界来放置,如果一个绝对定位元素镶嵌在另一个定位元素中,这个元素就会相对于外包含元素定位.相对于最近的父元素指定

position: static;

静态定位,元素会放在正常的文档流中

# 网络

## HTTP

HTTP(HyperText Transfer Protocol), 超文本传输协议，运行在TCP/IP之上，是**不保存状态的协议**

HTTP使用一种**请求/响应模型（request/response）**,客户做出一个HTTP请求,Web服务器返回一个HTTP响应,再由浏览器确定如何进行处理。如果来自服务器的响应是一个HTML页面,就会把HTML增加到HTTP响应中

 **HTTP请求(request)**

- 请求URI(客户想要访问的资源)
- HTTP方法(GET,POST等)
  - GET: 获取资源  请求会把表单数据（总字符数有限，取决于服务器）追加到URL的最后(不安全)
  - POST： 传输实体主体  请求将表单数据包括在请求的体中
  - PUT：传输文件
  - HEAD : 获取报文首部
  - DELETE： 删除文件
  - OPTIONS : 询问支持的方法
  - TRACE：追踪路径
  - CONNEXT: 要求用隧道协议连接代理
    - SSL Secure Sockets Layer  安全套接层
    - TLS Transport Layer Security 传输层安全
    - CONNECT   代理服务器：端口号  HTTP版本
- (可选)请求首部字段 /表单参数数据(查询串)
- 版本协议
- 内容实体

**HTTP响应response**

- 状态码 status code
- 用以解释状态码的原因短语（reason-phrase）
- 可选的响应首部字段以及实体主体
- ~~响应的实际内容(HTML,图像等)~~



HTTP, HTML, URL

ARP 协议（Address Resolution Protocol）: 根据通信方的IP地址就可以反查出对应的MAC地址

域名 --DNS-- IP地址 -- ARP -- MAC地址

HTTP/1.1 虽然是无状态协议，减少了服务器的CPU即内存资源的消耗。但是为了实现期望的保持状态功能，引入了Cookie，客户端向服务器发出请求，服务器生成Cookie信息，在响应中添加Cookie，客户端保存Cookie后在请求中加入Cookie

HTTP/1.0 每进行一次HTTP通信就要断开一次TCP连接（三次握手），

HTTP/1.1 使用HTTP keep-alive 方法，只要任意一端没有明确提出断开连接，则保持TCP连接状态。管线化（pipelining）出现后，不用等待响应亦可直接发送下一个请求。



报文首部：请求行（方法，URI， HTTP版本），HTTP首部字段（请求首部字段，通用首部字段，实体首部字段，其他）

CR+LF

报文主体

- 网站名: www.baidu.com
- 域名: baidu.com
- URL：scheme://host.domain:port/path/filename
  - scheme - 定义因特网服务的类型。最常见的类型是 http，ftp
  - host - 定义域主机（http 的默认主机是 www）
  - domain - 定义因特网域名，比如 runoob.com
  - :port - 定义主机上的端口号（http 的默认端口号是 80）
  - path - 定义服务器上的路径（如果省略，则文档必须位于网站的根目录中）。
  - filename - 定义文档/资源的名称
- URI：/path/filename
- URL 只能使用ASCII 字符集
- URL 不能包含空格。URL 编码通常使用 + 来替换空格
- 编码使用 "%" 其后跟随两位的十六进制数来替换非 ASCII 字符。
- 大小写敏感



传输报文前，报文分块传输编码（Chunked Transfer Coding）

通信数据转发程序

- 代理
  - 缓存代理：预先将资源的副本保存在代理服务器上
  - 透明代理
- 网关：能使线路上的服务器提供非HTTP协议服务，连接数据库
- 隧道：建立安全的通信线路，隧道本身是透明的，不会解析HTTP请求

HTTP缺点：

- 通信使用明文，内容可能被窃听
- 不验证通信方的身份，因此有可能遭遇伪装
- 无法证明报文的完整性，所以有可能已经遭到篡改

HTTPS（HTTP Secure, 超文本传输安全协议  HTTP over SSL）：用SSL建立安全通信线路之后，在该线路进行HTTP通信。

HTTPS = HTTP + 加密 + 认证 + 完整性保护

HTTPS

- 应用层（HTTP）
- SSL
- TCP
- IP

对称秘钥加密：加密和解密同用一个密钥

非对称秘钥加密：公开密钥（public key）, 私有秘钥（private key）

HTTPS:使用非对称秘钥加密在稍后通信中使用的密钥，再使用对称秘钥加密进行通信

CA(数字证书认证机构 Certificate Authority)：证明公开密钥的正确性

编写服务器程序来处理客户端请求通常就称之为Web开发。

SSL 采用双因素认证（证书认证和表单（密码）认证）分别用于认证客户端和用户本人



SNS(Social Networking  Service, 社交网络服务)

CGI(Xommon Gateway Interface, 通用网关接口)：指Web服务器在接收到客户端发送过来的请求后转发给程序的一组机制。程序会对请求内容做出相应的动作，如创建HTML动态内容

Servlert = Server + Applet 轻量级服务程序。

CGI，每次接到请求，程序都要跟着启动一次。因此一旦访问量过大，Web服务器要承担相当大的负载。而Servlet运行在于Web相同的进程中，因此负载较小。Servlet的运行环境叫做Web容器或Servlet容器



XML，HTML， JSON：数据的存储格式

客户端将用户ID和密码等登陆信息放入报文实体中，以post方法把请求发送给服务器，使用HTTPS通信。服务器收到请求后发放用以识别用户的Session ID.对登陆信息进行验证，然后把用户的认证状态和Session ID绑定后记录在服务器。客户端收到Session ID后，将其作为Cookie保存在本地。下次向服务器发送请求时，浏览器自动发送Cookie，



## DNS

- URI （Uniform Resource Identifier）：统一资源**标识符**，标识莫一互联网资源

- URL(Uniform Resource Locator): 统一资源**定位符**，标识资源的地点
- URL 是 URI的子集
  - URL= 协议+服务器名+端口号+特定路径+资源名+查询串(GET方法)
  - URI= 特定路径+资源名+查询串
- 域名: baidu.com

DNS（Domain Name System，域名系统），因特网上作为**域名和IP地址相互映射的一个分布式数据库**，能够使用户更方便的访问互联网，而不用去记住能够被机器直接读取的IP数串。

通过主机名，最终得到该主机名对应的IP地址的过程叫做**域名解析**（或主机名解析）。DNS协议运行在UDP协议之上，使用端口号53。

中文名：域名系统

外文名：Domain Name System

使用协议：UDP,TCP（当请求大于512字节时）

使用端口：53

DNS功能

每个IP地址都可以有一个主机名，主机名由一个或多个字符串组成，字符串之间用小数点隔开。有了主机名，就不要死记硬背每台IP设备的IP地址，只要记住相对直观有意义的主机名就行了。这就是DNS协议所要完成的功能。

主机名到IP地址的映射有两种方式：

1）静态映射，每台设备上都配置主机到IP地址的映射，各设备独立维护自己的映射表，而且只供本设备使用；

2）动态映射，建立一套域名解析系统（DNS），只在专门的DNS服务器上配置主机到IP地址的映射，网络上需要使用主机名通信的设备，首先需要到DNS服务器查询主机所对应的IP地址。

通过主机名，最终得到该主机名对应的IP地址的过程叫做域名解析（或主机名解析）。在解析域名时，可以首先采用静态域名解析的方法，如果静态域名解析不成功，再采用动态域名解析的方法。可以将一些常用的域名放入静态域名解析表中，这样可以大大提高域名解析效率。

 

 