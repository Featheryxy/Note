# IDEA

## Compile、Make、Build

编译，是将源代码转换为可执行代码的过程。编译需要指定源文件和编译输出的文件路径（输出目录）。Java的编译会将java编译为class文件，将非java的文件（一般成为资源文件、比如图片、xml、txt、poperties等文件）原封不动的复制到编译输出目录，并保持源文件夹的目录层次关系。

在Java的集成开发环境中，比如Eclipse、IDEA中，有常常有三种与编译相关的选项Compile、Make、Build三个选项。这三个选项最基本的功能都是完成编译过程。但又有很大的区别，区别如下：

1. Compile：**Compile只编译选定的目标**，不管之前是否已经编译过。
2. Make：编译选定的目标，但是**Make只编译上次编译变化过的文件**，减少重复劳动，节省时间。（具体怎么检查未变化，这个就不用考虑了，IDE自己内部会搞定这些的）
3. Build：是对**整个工程**进行彻底的重新编译，而不管是否已经编译过。Build过程往往会生成发布包，这个具体要看对IDE的配置了，Build在实际中应用很少，因为开发时候基本上不用，发布生产时候一般都用ANT等工具来发布。Build因为要全部编译，还要执行打包等额外工作，因此时间较长。

**Reference**: [https://blog.51cto.com/lavasoft/436216](https://blog.51cto.com/lavasoft/436216)

## **Maven项目导入**

1. File -> open 导入Maven项目
2. File -> New -> Module from Existine Sources 导入相应的Maven子项目
3. 选中pom文件，右键选中add as maven project

对于一个普通的Maven项目，用open和import project其实没什么区别，只是imort project要多一步，选择一下imort的形式，告诉idea这是个maven项目。对于一个文件下的有多个maven项目想要同时导入，只能用open方式，import project方式打不开，但是用open方式也仅仅是打开而已，idea并不能识别为maven项目，还要通过File -> New -> Module from Existine Sources方式再次以maven方式把项目重新导入一次，才能成为maven项目。

## Fields  和 Properties

- 域 Fields：定义的字段，没有get/set
- 属性Properties：setter/getter方法名，就是这个类的属性。

## .iml和.idea

### **.iml文件**

iml =  infomation of module
iml是 intellij idea的**工程配置文件**，里面是当前project的一些配置信息。

### **.idea文件夹**

.idea存放**项目的配置信息**，包括历史记录，版本控制信息等。

不建议隐藏iml，因为项目名出现中括号是因为iml文件名和项目文件名不一样，需要更改iml文件名

## **缓存清除**

file->invalidate caches->invalidate and restart

import的包无法调用 or 已使用的变量提示未使用，可以进行缓存清除

## **文件夹**

- Source roots：该类文件下包含**源代码**，汇编编译期编译，将编译的文件放在target/classes/con/...
- Resource roots：用于存放各种**资源文件**，如（图像，xml，属性文件等），构建过程中，该类资源直接被复制到target/classes/mapper
- Test source roots：包含测试代码，编译的文件放在target/test-classes

## Debug

- Alter + click：查看某个对象的值
- Show Execution Point：跳转到当前代码所执行的地方
- Drop Frame：步入方法体之后，想回退到方法体外，点这个按钮后，断点重新回到方法体之外。在继续还是可以再次进到方法内
- Evaluate Expression：根据输入，执行得到结果

## 常用快捷键

Ctrl+Alt+T：Surround With

Ctrl+Alt+M：抽取方法

F2：光标定位到错误地方

## 常用插件



1. Alibaba Java Coding Guidelines
2. String Manipulation
3. MyBatis Log Plugin
4. MyBatisX
5. Easy Code 根据数据库自动生成dao, entity
6. key promoter 
7. Maven Helper
8. Alibaba java coding 代码规范
9. Gsonformat json转化实体类 
10. javadoc  生成注释文档  
11. generateallsetter 自动生成set代码 
12. stopcoding
13. Grep Console: 日志着色控制台显示 
14. SonarLint  扫描代码的问题，例如 性能，安全和重复问题。新手必备！显著提升代码质量
15. Theme: Cyan Light Theme
16. ,

##  Live Templates

代码模板

Settings --> Live Templates

导出: 在菜单栏选择 `File` | `Manage IDE Settings` | `Export Settings`

导入：在菜单栏选择 `File` | `Manage IDE Settings` | `Import Settings`

## PostFix

Settings→Editor→General→PostFix Completion

## IDEA创建文件添加作者及时间信息

 File ——> Settings…——> Editor ——> File and Code Templates ——> Includes ——> File Header

```
/**
 * @author Name
 * @date ${DATE} ${TIME}
 */
```



## ModuleFileDir

Run/Debug Configurations --> + --> Application --->Edit configuration templates ---> Working directory  --> insert ModuleFileDir



## 项目维度功能

右键项目名称 ——> Optimize import

还可以Run All Tests

Reformat code



## 鼠标滚轮控制缩放大小

File -> Setting -> Editor -> General 

