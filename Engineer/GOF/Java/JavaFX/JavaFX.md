# JavaFX

javafxc.exe 编译 JavaFX Script

javafx在jdk8,jdk9,jdk10中，但是在jdk11中移除，作为一个新的开源项目在维护

以树状架构的方式组合物件,各节点称为Node, Node分为一下三类

- Root: 最上层容器
- Parent: 置放组件的容器
- Leaf: 容器中的组件

### 物理抽象

Platform: 平台

> a flat raised area or structure

Screen: 银幕

> a flat surface in a cinema, on a television, or as part of a computer, on which pictures or words are shown

### 软件抽象

Application：应用

> 

Stage: 舞台，窗口

> the area in a theatre that is often raised above ground level and on which actors or entertainers perform

Scene: 场景

> a part of a play or film in which the action stays in one place for a continuous period of time;

Node: 交点

> a place where things such as lines join, or where a leaf and stemjoin on a plant





### 操作

$$
属性绑定 \subset 事件监听器 \\
User Action = {Source Object }
$$

```java
// 属性绑定
circle.centerXProperty().bind(scene.widthProperty().divide(2));
circle.centerYProperty().bind(scene.heightProperty().divide(2));

// 事件监听器
circle.centerXProperty().addListener(new ChangeListener<Number>() {
    @Override
    public void changed(ObservableValue<? extends Number> observable, Number oldValue, Number newValue) {
        System.out.println(String.format("old x: %s, new x %s", oldValue, newValue));
    }
});

// 为事件添加事件处理器
menu1.setOnAction(new EventHandler<ActionEvent>() {
    @Override
    public void handle(ActionEvent event) {
        System.out.println("menu1.setOnAction");
    }
});

cleanBtn.addEventHandler(ActionEvent.ACTION, sayHello);

// 事件与处理器分离
EventHandler<ActionEvent> sayHello = new EventHandler<ActionEvent>() {
    @Override
    public void handle(ActionEvent event) {
        System.out.println("say Hello");
    }
};
cleanBtn.setOnAction(sayHello);


```





### 参考资料

https://blog.csdn.net/godelgnis/article/details/89473896

https://code.makery.ch/zh-cn/library/javafx-tutorial/

https://gitcode.net/mirrors/jfoenixadmin/jfoenix?