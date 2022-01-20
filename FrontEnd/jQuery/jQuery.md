# JQuery

## 1 简介

- what: JQuery是一个JavaScript函数库
- why
  - HTML 元素选取
  - HTML 元素操作
  - CSS 操作
  - HTML 事件函数
  - JavaScript 特效和动画
  - HTML DOM 遍历和修改
  - AJAX
  - Utilties

## 2 基础

### 2.1 引入

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script src="jquery.min.js"></script>
    <style>
        div {
            width: 200px;
            height: 200px;
            background-color: pink;
        }
    </style>
</head>
<body>
    <script>
        // $('div').hide();
        // 1. 等着页面DOM加载完毕再去执行js 代码
        // $(document).ready(function() {
        //     $('div').hide();
        // })
        // 2.  等着页面DOM加载完毕再去执行js 代码
        $(function() {
            $('div').hide();
        })
    </script>
    <div></div>
</body>
</html>
```

### 2.2 顶级对象

-  \$ 是jQuery的别称, $同时也是jQuery的 顶级对象

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script src="jquery.min.js"></script>
    <style>
        div {
            width: 200px;
            height: 200px;
            background-color: pink;
        }
    </style>
</head>

<body>
    <div></div>
    <script>
        // 1. $ 是jQuery的别称（另外的名字）
        // $(function() {
        //     alert(11)
        // });
        jQuery(function() {
            // alert(11)
            // $('div').hide();
            jQuery('div').hide();
        });
        // 2. $同时也是jQuery的 顶级对象
    </script>
</body>
</html>
```

### 2.3 jQuery对象和DOM对象

1. DOM 对象：  用原生js获取过来的对象就是DOM对象
   - `var myDiv = document.querySelector('div');`
2. jQuery对象： 用jquery方式获取过来的对象是jQuery对象。 本质：**通过$把DOM元素进行了包装**
   - `$('div'); `
3. jQuery 对象只能使用 jQuery 方法，DOM 对象则使用原生的 JavaScirpt 属性和方法

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="jquery.min.js"></script>
    <style>
        div {
            width: 100px;
            height: 100px;
            background-color: pink;
        }
    </style>
</head>

<body>
    <div></div>
    <span></span>
    <script>
        // 1. DOM 对象：  用原生js获取过来的对象就是DOM对象
        var myDiv = document.querySelector('div'); // myDiv 是DOM对象
        var mySpan = document.querySelector('span'); // mySpan 是DOM对象
        console.dir(myDiv);
        // 2. jQuery对象： 用jquery方式获取过来的对象是jQuery对象。 本质：通过$把DOM元素进行了包装
        $('div'); // $('div')是一个jQuery 对象
        $('span'); // $('span')是一个jQuery 对象
        console.dir($('div'));
        // 3. jQuery 对象只能使用 jQuery 方法，DOM 对象则使用原生的 JavaScirpt 属性和方法
        // myDiv.style.display = 'none';
        // myDiv.hide(); //wrong myDiv是一个dom对象不能使用 jquery里面的hide方法
        // $('div').style.display = 'none'; // wrong 这个$('div')是一个jQuery对象不能使用原生js 的属性和方法
    </script>
</body>
</html>
```

### 2.4 对象转换

jQuery---> Dom

- `$('video')[0].play()`
- `$('video').get(0).play()`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="jquery.min.js"></script>
</head>

<body>
    <video src="mov.mp4" muted></video>
    <script>
        // 1. DOM对象转换为 jQuery对象
        // (1) 我们直接获取视频，得到就是jQuery对象
        $('video');
        // (2) 我们已经使用原生js 获取过来 DOM对象
        // var myvideo = document.querySelector('video');
        // $(myvideo).play();  //wrong jquery里面没有play 这个方法

        // 2.  jQuery对象转换为DOM对象
        // myvideo.play();
        console.dir($('video'))
        $('video')[0].play()
        // $('video').get(0).play()
    </script>
</body>

</html>
```

## 3 选择器

```javascript
$("CSS选择器") 
```

### 3.1 jQuery基础选择器

| 名称       | 用法            | 描述                     |
| ---------- | --------------- | ------------------------ |
| ID选择器   | $("#id")        | 匹配指定ID的元素         |
| 全选择器   | $("*")          | 匹配所有元素             |
| 类选择器   | $(".class")     | 获取同一类class的元素    |
| 标签选择器 | $("div")        | 获取同一类标签的所有元素 |
| 并集选择器 | $("div,p,li")   | 获取多个元素             |
| 交集选择器 | $("li.current") | 交集元素                 |

### 3.2 层级选择器

| 名称       | 用法       | 描述                                                         |
| ---------- | ---------- | ------------------------------------------------------------ |
| 子代选择器 | $("ul>li") | 使用>号，获取亲儿子层级的元素；注意，并不会获取孙子层级的元素 |
| 后代选择器 | $("ul li") | 使用空格，代表后代选择器，获取ul下的所有li元素，包括孙子等   |

### 3.3 隐式迭代

- 设置样式：`$('div').css('属性'，'值')` 

-  隐式迭代就是把匹配的所有元素**内部进行遍历循环**，给每一个元素添加css这个方法

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="jquery.min.js"></script>
</head>

<body>
    <div>惊喜不，意外不</div>
    <div>惊喜不，意外不</div>
    <div>惊喜不，意外不</div>
    <div>惊喜不，意外不</div>
    <ul>
        <li>相同的操作</li>
        <li>相同的操作</li>
        <li>相同的操作</li>
    </ul>
    <script>
        // 1. 获取四个div元素 
        console.log($("div"));

        // 2. 给四个div设置背景颜色为粉色 jquery对象不能使用style
        $("div").css("background", "pink");
        // 3. 隐式迭代就是把匹配的所有元素内部进行遍历循环，给每一个元素添加css这个方法
        $("ul li").css("color", "red");
    </script>
</body>

</html>
```

### 3.4 筛选选择器

| 语法       | 用法          | 描述                                                |
| ---------- | ------------- | --------------------------------------------------- |
| :first     | $('ls:first') |                                                     |
| :last      | $('ls:last')  |                                                     |
| :eq(index) | $('li:eq(2)') | 获取到的li元素中，选择index为2的元素，索引号从0开始 |
| :odd       | $('li:odd')   |                                                     |
| :even      | $('li:even')  |                                                     |

### 3.5 筛选方法

| 语法               | 用法                           | 说明                                                   |
| ------------------ | ------------------------------ | ------------------------------------------------------ |
| parent()           | $("li").parent();              | 查找父级                                               |
| children(selector) | $("ul").children("li")         | 相当于("ul>li")，最近一级（亲儿子）                    |
| find(selector)     | $("ul").find("li")             | 相当于$("ul li")                                       |
| siblings(selector) | $(".first").siblings("li")     | 查找兄弟节点，不包括自己本身                           |
| nextAll([expr])    | $(".first").nextAll()          | 查找当前元素之后所有的同辈元素                         |
| prevtAll([expr])   | $(".last").prevAll()           | 查找当前元素之前所有的同辈元素                         |
| hasClass(class)    | $('div').hasClass("protected") | 检查当前的元素是否含有某个特定的类，如果有，则返回true |
| eq(index)          | $("li").eq(2)                  | $("li:eq(2)")                                          |

### 3.6 排他思想

当前元素设置样式，其余兄弟元素清除样式。

```javascript
<script>
    $(function() {
        // 1. 隐式迭代 给所有的按钮都绑定了点击事件
        $("button").click(function() {
            // 2. 当前的元素变化背景颜色
            $(this).css("background", "pink");
            // 3. 其余的兄弟去掉背景颜色 隐式迭代
            $(this).siblings("button").css("background", "");
        });
    })
</script>
```



## 4 样式操作

### 4.1 操作css方法

1. 参数只写属性名，则是返回属性值

   ```javascript
   $(this).css("color")
   ```

2. 参数是属性名，属性值，逗号分隔，则修改属性值

   ```javascript
   $(this).css("color", "red");
   ```

3. 参数是对象形式｛｝，则修改多个属性值

   ```javascript
   $(this).css({
       "color":"white",
       "font-size":"20px"
       
       // 属性可不加引号
        backgroundColor: "blue"
       // 如果是复合属性则必须采取驼峰命名法，如果值不是数字，则需要加引号
   })
   ```

### 4.2 设置类样式方法

   1. 添加类

      ```javascript
      $("div").addClass("current");
      ```

   2. 移除类

      ```javascript
      $("div").removeClass("current")
      ```

   3. 切换类

      ```javascript
      $(div).toggleClass("current");
      ```

### 4.3 类操作与className区别

   - 原生JS中className会覆盖元素原先里面的类名。
   - jQuery里面类操作只是对指定类进行操作，不影响原先的类名。

## 5 效果

- 显示隐藏
  - show(), hide(), toggle()
- 滑动
  - slideDown(), slideUp(), slideToggle()
- 淡入淡出
  - fadIn(), fadeOut(), fadeToggle(), fadeTo()
- 自定义动画
  - animate()

### 5.1 显示隐藏效果

1. 语法规范

   ```javascript
   show([speed, [easing], [fn]])
   ```

2. 参数

   - **speed**: 三种预定速度之一的字符串("slow","normal", or "fast")或表示动画时长的毫秒数值(如：1000)
   - **easing**: (Optional) 用来指定切换效果，默认是"swing"，可用参数"linear"
   - **fn: **在动画完成时执行的函数，每个元素执行一次。

### 5.2 滑动效果

1. 语法规范

   ```javascript
   slideDown([speed],[easing],[fn])
   ```

2. 参数

   - **speed**: 三种预定速度之一的字符串("slow","normal", or "fast")或表示动画时长的毫秒数值(如：1000)
   - **easing**: (Optional) 用来指定切换效果，默认是"swing"，可用参数"linear"
   - **fn: **在动画完成时执行的函数，每个元素执行一次。

### 5.3 事件切换

```javascript
hover([over,]out)
```

- over:鼠标移到元素上要触发的函数

- out:鼠标移出元素要触发的函数
- 如果只写一个函数，那么鼠标经过和鼠标离开都会触发这个函数

```html
>
    <ul class="nav">
        <li>
            <a href="#">微博</a>
            <ul>
                <li>
                    <a href="">私信</a>
                </li>
                <li>
                    <a href="">评论</a>
                </li>
                <li>
                    <a href="">@我</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#">微博</a>
            <ul>
                <li>
                    <a href="">私信</a>
                </li>
                <li>
                    <a href="">评论</a>
                </li>
                <li>
                    <a href="">@我</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#">微博</a>
            <ul>
                <li>
                    <a href="">私信</a>
                </li>
                <li>
                    <a href="">评论</a>
                </li>
                <li>
                    <a href="">@我</a>
                </li>
            </ul>
        </li>
        <li>
            <a href="#">微博</a>
            <ul>
                <li>
                    <a href="">私信</a>
                </li>
                <li>
                    <a href="">评论</a>
                </li>
                <li>
                    <a href="">@我</a>
                </li>
            </ul>
        </li>
    </ul>
    <script>
        $(function() {
            // 鼠标经过
            // $(".nav>li").mouseover(function() {
            //     // $(this) jQuery 当前元素  this不要加引号
            //     // show() 显示元素  hide() 隐藏元素
            //     $(this).children("ul").slideDown(200);
            // });
            // // 鼠标离开
            // $(".nav>li").mouseout(function() {
            //     $(this).children("ul").slideUp(200);
            // });
            // 1. 事件切换 hover 就是鼠标经过和离开的复合写法
            // $(".nav>li").hover(function() {
            //     $(this).children("ul").slideDown(200);
            // }, function() {
            //     $(this).children("ul").slideUp(200);
            // });
            // 2. 事件切换 hover  如果只写一个函数，那么鼠标经过和鼠标离开都会触发这个函数
            $(".nav>li").hover(function() {
                $(this).children("ul").slideToggle();
            });
        })
    </script>
</body>
```

### 5.4 动画队列及其停止排队方法

1. 动画队列

   动画或者效果一旦触发就会执行，如果多次触发，就造成多个动画排队执行

2. 停止排队

   ```
   stop()
   ```

   ps: `stop()`用于停止动画或效果，必须写到动画的前面，相当于停止结束上一次的动画


```
$(".nav>li").hover(function() {
    // stop 方法必须写到动画的前面
    $(this).children("ul").stop().slideToggle();
});
```

### 5.5 淡入淡出

```javascript
fadeIn([speed],[easing],[fn])
fadeOut([speed],[easing],[fn])
fadeToggle([speed,[easing],[fn]])

fadeTo([[speed],opacity,[easing],[fn]])
```

**speed**:三种预定速度之一的字符串("slow","normal", or "fast")或表示动画时长的毫秒数值(如：1000)

**easing**:(Optional) 用来指定切换效果，默认是"swing"，可用参数"linear"

**fn**:在动画完成时执行的函数，每个元素执行一次。

**opacity**:一个0至1之间表示透明度的数字。

### 5.6 自定义动画

```
animate(params,[speed],[easing],[fn])
```

**params**:一组包含作为动画属性和终值的样式属性和及其值的集合，以对象形式传递，属性名可以不用带引号，如果是复合属性则需要采用驼峰命名法borderLeft

**speed**:三种预定速度之一的字符串("slow","normal", or "fast")或表示动画时长的毫秒数值(如：1000)

**easing**:要使用的擦除效果的名称(需要插件支持).默认jQuery提供"linear" 和 "swing".

**fn**:在动画完成时执行的函数，每个元素执行一次。

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="jquery.min.js"></script>
    <style>
        div {
            position: absolute;
            width: 200px;
            height: 200px;
            background-color: pink;
        }
    </style>
</head>

<body>
    <button>动起来</button>
    <div></div>
    <script>
        $(function() {
            $("button").click(function() {
                $("div").animate({
                    left: 500,
                    top: 300,
                    opacity: .4,
                    width: 500
                }, 500);
            })
        })
    </script>
</body>

</html>
```

## 6 属性操作

### 6.1 设置或获取元素固有属性值 prop()

- 设置或获取元素**固有属性值**（a元素的href属性） prop()

1. 获取属性值

   ```javascript
   prop("属性")
   ```

2. 设置属性值

   ```javascript
   prop("属性", "属性值")
   ```

### 6.2 设置或获取元素自定义属性值 attr()

1. 获取属性值

   ```javascript
   attr("属性") 
   ```

2. 设置属性值

   ```javascript
   attr("属性", "属性值")
   ```

### 6.3 数据缓存 data()

data()在指定的元素上存取数据，并不会修改DOM元素结构。一旦页面刷新，之前存放的数据都将被移除。

1. 附加数据语法

   ```javascript
   data("name", "value")
   ```

2. 获取数据语法

   ```javascript
   data("name")
   ```

## 7 内容文本值

### 7.1 普通元素内容html()

```
html() // 获取元素的内容，是一个元素
html("内容") // 设置元素的内容
```

### 7.2 普通元素文本内容text() 

```javascript
text() // 获取元素的文本内容
text() // 设置元素的文本内容
```

### 7.3 表单的值 val()

```
val() // 获取表单元素的value属性值
val("内容") //  设置表单元素的value属性值
```

## 8 jQuery 元素操作

### 8.1 遍历元素

jQuery隐式迭代是对同一类元素做了同样的操作。如果想要给同一类元素做不同操作，就需要用到遍历。

**语法1：**

```
$("div").each(function(index, domEle){xxx;})
```

1. each()方法遍历匹配的每一个元素是DOM对象。
2. 里面的回调函数有2个参数：index是每个元素的索引号；demEle是每个DOM元素对象，不是jquery对象
3. 所以想要使用jquery方法，需要给这个dom元素转换为jquery对象$(domEle)

**语法2：**

```
$.each(object, function(index, element){xxx;})
```

1. $.each()可用于遍历任何对象。主要用于数据处理，比如数组，对象
2. index：索引号，element：遍历内容

### 8.2 创建元素

语法：

```javascript
$("<li></li>")
```

### 8.3 添加元素

1. 内部添加

   ```javascript
   element.append("内容")  // 把内容放入匹配元素内部的最后面
   element.preppend("内容")  //内部添加并且放到内容的最前面
   ```

2. 外部添加

   ```javascript
   element.after("内容") // 把内容放入目标元素后面
   element.before("内容") // 把内容放入目标元素前面
   ```

3. 区别

   - 内部添加元素，生成之后，它们是父子关系
   - 外部添加元素，生成之后，它们是兄弟关系

### 8.4 删除元素

```
element.remove() //删除匹配的元素（本身）
element.empty() //可以删除匹配的元素里面的子节点 孩子
element.html("")  //可以删除匹配的元素里面的子节点 孩子
```

## 9 尺寸、位置操作

### 9.1 尺寸

| 语法                               | 用法                        |
| ---------------------------------- | --------------------------- |
| width()/height()                   | width/height                |
| innderWidth()/innerHeight()        | 包含padding                 |
| outerWidth()/outerHeight()         | 包含padding, border         |
| outerWidth(true)/outerHeight(true) | 包含padding, border, margin |

- 参数为空，则获取相应值，返回的是数字型
- 参数为数字，则修改相应值
- 参数可以不必写单位

### 9.2 位置

1. offset() 

   - 设置或返回被选元素相对于**文档**的偏移坐标，跟父级没有关系
   - 有两个属性left,top。offset().top 用户获取距离文档顶部的距离
   - 可以设置元素的偏移：offset({top:10, left:30})

2. position()

   - 用于返回被选元素相对于**带有定位的父级偏移坐标**，如果父级都没有定位，则以文档为准
   - 这个方法只能获取不能设置偏移

3. scrollTop()/scrollLeft()

   - 设置或获取元素**被卷去**的头部和左侧

     

## 10 事件

### 10.1 单个事件注册

```
element.事件(function(){})
$("div").click(function(){事件处理程序})
```

### 10.2 绑定事件on()

on()在匹配元素上绑定一个或多个事件的事件处理函数

```
element.on(events, [selector], fn)
```

#### 10.2.1 on可以绑定1个或者多个事件处理程序

            $("div").on({
                mouseenter: function() {
                    $(this).css("background", "skyblue");
                },
                click: function() {
                    $(this).css("background", "purple");
                },
                mouseleave: function() {
                    $(this).css("background", "blue");
                }
            });
如果事件处理程序相同

```
            $("div").on("mouseenter mouseleave", function() {
                $(this).toggleClass("current");
            });
```

#### 10.2.2 事件委派操作

定义：把原来加给子元素身上的事件绑定在父元素身上，就是把事件委托给父元素

```
$("ul").on("click", "li", function() {
    alert(11);
});
// click 是绑定在ul 身上的，但是 触发的对象是 ul 里面的小li
```

#### 10.2.3 给未来动态创建的元素绑定事件

```
$("ol").on("click", "li", function() {
    alert(11);
})
var li = $("<li>我是后来创建的</li>");
$("ol").append(li);
```

### 10.3 解绑事件off()

off()可以移除通过on()方法添加的时间处理程序

```
$("p").off() //解绑p元素所有事件处理程序
$("p").off("click") // 解绑p元素上的click事件
$("ul").off("click", "li"); //解绑事件委托
```

如果有的事件只想触发一次，使用one()

```
$("p").one("click", function() {
    alert(11);
})
```

### 10.4 自动触发事件 trigger()

```
$(function() {
	$("div").on("click", function() {
		alert(11);
});

element.click();
element.trigger("click");
element.triggerHandler("click") //不会触发元素的默认行为
```

### 10.5 事件对象

事件被触发，就会有事件对象的产生。

```
element.on(events,[selector], function(event){})
```

- 阻止默认行为：event.preventDefault() 或 return false
- 阻止冒泡：event.stopPropagation()

## 11 其他方法

### 11.1 拷贝对象

将某个对象拷贝给另一个对象使用，将object拷贝到target

```
$.extend([deep], target, object1, [objectN])
```

- deep: true为深拷贝，默认为false,浅拷贝
- target: 要拷贝的目标对象
- object1: 待拷贝到第一个对象的对象。
- 浅拷贝把原来对象里面的复杂数据类型地址拷贝给目标对象
- 深拷贝把里面的数据完全复制一份给目标对象 如果里面有不冲突的属性,会合并到一起

### 11.2 多库共存

jQuery使用\$作为标识符，随着jQuery的流行，其他js库也会用\$作为标识符，这样一起使用会引起冲突

解决方法：

1. 将$ 改为jQuery
2. 定义新的名称，将"$"换名，var xx = \$.noConflict();

### 11.3 jQuery插件

插件依赖于jQuery来完成，所以必须要先引入jQuery文件，因此也成为jQuery插件

常用网址

1. jQuery插件库：http://www.jq22.com/
2. jQuery之家：http://www.htmleaf.com/