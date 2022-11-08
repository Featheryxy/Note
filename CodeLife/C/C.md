# C

C语言标识符：只能由字母，数字，下划线组成，不能以数字开头，第一个字符必须是字母或下划线，大小写敏感

Java语言标识符：字母，数字，下划线，美元符号，不能以数字开头

整型常量：

1. 十进制整数：

   由数字0~9和正负号表示

2. 八进制整数：

   由数字0开头，后跟数字0~7和正负号表示，如0123，011

3. 十六进制整数

   由0x开头，后跟数字0~9，a~f，A~F正负号表示。0x123

每个字符串尾自动加一个'\0'作为字符串结束标志

逻辑运算优先级，！> && > ||



Switch可以向下穿越

```java
    public static void main(String[] args) {
        String ch = "H";
        switch (ch) {
            case "H":
                System.out.println("Hello");
            case "g":
            case "G":
                System.out.println("Good morning");
            default:
                System.out.println("Bye_Bye");
        }
        //Hello
        //Good morning
        //Bye_Bye
    }
```

