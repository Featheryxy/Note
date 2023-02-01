# equals

1. == 既可以比较基本类型也可以比较引用类型。对于基本类型就是比较值，对于引用类型就是比较内存地址
2. equals的话，它是属于java.lang.Object类里面的方法，如果该方法没有被重写过默认也是==;我们可以看到String等类的equals方法是被重写过的，而且String类在日常开发中用的比较多，久而久之，形成了equals是比较值的错误观点。
3. 具体要看自定义类里有没有重写Object的equals方法来判断。
4. 通常情况下，重写equals方法，会比较类中的相应属性是否都相等。

```
int it = 65;
float fl = 65.0f;
System.out.println(“65和65.0f是否相等？ ” + (it == fl)); //true int 向上转型为float
char ch1 = 'A'; char ch2 = 12;
System.out.println("65和'A'是否相等？ " + (it == ch1));//true
System.out.println(“12和ch2是否相等？ " + (12 == ch2));//true
String str1 = new String("hello");
String str2 = new String("hello");
System.out.println("str1和str2是否相等？ "+ (str1 == str2));//false
System.out.println("str1是否equals str2？ "+(str1.equals(str2)));//true
```

常量池主要保存字面量(Literal)和符号引用(Symbolic References)

String str = “abc”;可能创建一个或者不创建对象，如果”abc”在字符串池中不存在，会在java字符串池中创建一个String对象（”abc”），然后str指向这个内存地址，无论以后用这种方式创建多少个值为”abc”的字符串对象，始终只有一个内存地址被分配。

String str = new String(“abc”);至少会创建一个对象，也有可能创建两个。因为用到new关键字，肯定会在堆中创建一个String对象，如果字符池中已经存在”abc”,则不会在字符串池中创建一个String对象，如果不存在，则会在字符串常量池中也创建一个对象。

