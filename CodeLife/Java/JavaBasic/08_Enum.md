# Enum

Enum 定义的枚举类默认继承了 java.lang.Enum 类。

每个枚举值都是一个枚举对象，每个对象都有name和ordinal属性

>name为枚举变量的名称
>
>ordinal为枚举变量在枚举类中声明的顺序，下标从0开始 

## How

```java
package test;

enum Color
{
    RED, GREEN, BLUE;

    private Color(){
        System.out.println("Constructor called for : " + this.toString());
    }
}



public class EnumTest {
    public static void main(String[] args) {
        // 简单使用
//        Color blue = Color.BLUE;
//        System.out.println(blue); // BLUE

        // switch
//        Color myVar = Color.BLUE;
//        switch(myVar) {
//            case RED:
//                System.out.println("红色");
//                break;
//            case GREEN:
//                System.out.println("绿色");
//                break;
//            case BLUE:
//                System.out.println("蓝色");
//                break;
//        }

        /*
            enum 定义的枚举类默认继承了 java.lang.Enum 类，并实现了 java.lang.Seriablizable 和 java.lang.Comparable 两个接口。
            values(), ordinal() 和 valueOf() 方法位于 java.lang.Enum 类中：
            values() 返回枚举类中所有的枚举值，每个值都是一个对象。
            ordinal()方法可以找到每个枚举常量的索引，就像数组索引一样。
            valueOf()方法返回指定字符串值的枚举常量。
            compareTo(E o)方法：则是比较枚举的大小，注意其内部实现是根据每个枚举的ordinal值大小进行比较的。

         */
        for (Color color: Color.values()){
            System.out.println(color + " at index " + color.ordinal());
        }
        System.out.println(Color.valueOf("RED"));

    }
}

// Reference: https://www.runoob.com/java/java-enum.html
public enum StatusEnum {
    DOING("进行中", "DOING"),
    DONE("已完成", "DONE"),
    CANCELLED("已取消", "CANCELLED");
    private String name;
    private String status;

    StatusEnum(String name, String status){
        this.name = name;
        this.status = status;
    }
    
	public static void main(String[] args) {
        StatusEnum[] values = StatusEnum.values();
        for (StatusEnum tmp : values) {
            System.out.println("name: "+tmp.getName());
            System.out.println("status: "+tmp.getStatus());
            System.out.println("ordinal: "+tmp.ordinal());

            System.out.println();
        }
    }
```
## Reference

 https://www.runoob.com/java/java-enum.html

https://zhuanlan.zhihu.com/p/438813997