## JavaStandardGuide

### 命名

变量命名: 名词，驼峰形式，体现业务语义，尽量减少对数据的判断。sotckBox。

常量命名：PAGE_SIZE

函数命名：动词

类名：实体类（Customer）和辅助类（CustomerService）

包名：类的更高层次抽象，如有一组类Apple、Pear、Orange， 其包名可以为fruit

模块名：一个模块中包含了多个包, <groupId, artifactId>

限定词后置：revenueAverage（平均收入），customerNum表示的是当前客户的序号，最好使用customerId来替代

对数据库操作时，函数命名

新增：create

添加：add

删除：remove

修改：update

查询(单个结果)：get

查询（多个结果）：list

分页查询：page

统计：count

安装 onlinesearch 命名工具

### 异常

业务系统中应该设定两个异常，且都应该是Unchecked Exception

1. BizException 业务异常 

2. SysException 系统异常，

### 函数

SLAP要求函数体中的内容必须在同一个抽象层次上。如果不在同一个层次，应该再次封装函数。

封装判断：使用函数将判断封装，函数名体现业务语义

函数参数：越少越好，**参数应该小等于2个**，超过2个应该使用对象封装.也有例外。

函数应该遵循职责单一的原则，一个方法只做一件事情.

```java
public void pay(List<Employee> employees){
    for (Employee e: employees){
        if(e.isPayDay()){
            Money pay = e.calculatePay();
            e.deliverPay(pay);
        }
    }
}

// 遍历所有雇员，检查是否该发工资，然后支付薪水拆分

public void pay(List<Employee> employees){
    for (Employee e: employees){
        payIfNecessary(e);
    }
}

private void payIfNecessary(Employee e) {
    if(e.isPayDay()){
        calculateAndDeliverPay(e);
    }
}

private void calculateAndDeliverPay(Employee e) {
    Money pay = e.calculatePay();
    e.deliverPay(pay);
}
```

### 设计原则

SOLID

Single Responsibility Principle（SRP）：单一职责原则。

> 一个方法只做一件事情.
> 
> 是否只有一个被修改的原因

Open Close Principle（OCP）：开闭原则。

> 对扩展开放，对修改关闭

Liskov Substitution Principle（LSP）：里氏替换原则。

> 程序中的父类型都应该可以正确地被子类型替换

Interface Segregation Principle（ISP）：接口隔离原则。

> 多个特定客户端接口要好于一个宽泛用途的接口。

Dependency Inversion Principle（DIP）：依赖倒置原则

> 模块之间交互应该依赖抽象，而非实现。

SLAP：抽象层次一致性（Single Level of Abstration Principle，SLAP）

DRY是Don’t Repeat Yourself, 避免重复代码, 系统的每一个功能都应该有唯一的实现

YAGNI（You Ain’t Gonna Need It）的意思是“你不会需要它”, 除了核心的功能之外，其他的功能一概不要提前设计

> DRY原则和YAGNI原则是不兼容的。前者追求“抽象化”，要求找到通用的解决方
> 法；后者追求“快和省”，意味着不要把精力放在抽象化上面，因为很可能“你不会需要它”。因此，就有了Rule of Three原则

Rule of Three也被称为“三次原则”，是指当某个功能第三次出现时，就有必要进行“抽象化”了

KISS（Keep It Simple and Stupid）把事情变复杂很简单，把事情变简单很
复杂

贫血模式提倡模型对象只包含数据，并提供简单的Getter和Setter；

而充血模式提倡数据和行为放在一起，是一种更加面向对象的做法。

### 分层架构

抽象层次：层次越往上，抽象程度越高，它所包含的东西就越多，其含义越宽泛，忽略的细节也越多。

How: 抽象的过程就是合并同类项、归并分类和寻找共性的过程。

在分层架构中，分层的使用可以进行严格地限制

1. 分层只知道直接的下层；

2. 或者可以宽松一些——分层可以访问它之下的任何分层。
   
   > Martin Fowler的经验是在实际中使用第二种方式会更好，因为它避免了在中间分层创建代码方法
