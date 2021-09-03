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
            values() 返回枚举类中所有的值。
            ordinal()方法可以找到每个枚举常量的索引，就像数组索引一样。
            valueOf()方法返回指定字符串值的枚举常量。
         */
        for (Color color: Color.values()){
            System.out.println(color + " at index " + color.ordinal());
        }
        System.out.println(Color.valueOf("RED"));

    }
}

// Reference: https://www.runoob.com/java/java-enum.html
```