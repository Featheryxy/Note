## 纵向

字符组

```
a         普通字符 匹配a
[abc]     字符集合 匹配a 或 匹配b 或 匹配c
[^abc]    字符集合取反
[a-zA-Z0-9]
******************************
\d      [0-9]        digit 一位数字
\D      [^0-9]       非数字
\w      [a-zA-Z0-9]  数字，字母，下划线  word
\W      [^a-zA-Z0-9]
\s      [\t\v\n\r\f]  space 空白字符
\S      [^\t\v\n\r\f]   非空白字符
.                       通配符
```

## 横向

量词

```markdown
x{m, n}   x匹配m到n次
x{m,}     x匹配至少m次
x{m}      x匹配m次


x*        x匹配任意次，包含0次
x+        x匹配至少一次     x{1，}
x?        x匹配零次或一次   x{0} 或 x{1}
```

## 其他

```
^\d          ^    以数字开头
[a-zA-Z]$     $    以字母结尾
|                管道符
[]                可选的，表示从方括号中选取一个字符
```

## 常见正则表达式

```java
^[A-Z][a-z][0-9] 以大写字母、小写字母和数字组成的、长度为 3 的字符串，其中第一个字符为大写字母，第二个字符为小写字母，第三个字符为数字
[^A-Za-z0-9] 匹配的是任何不是字母或数字的字符
```

## Demo

```java
Pattern（模板）由final修饰，构造器声明为private。只能通过 Pattern.compile(reg) 来获得Pattern对象;

Matcher（匹配器）： 根据模板pattern去匹配字符串str
boolean isfind = pattern.matcher(str).find()

boolean isfind = Pattern.compile(regex).find()
```

```java
package reg;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Demo3 {
    public static void main(String[] args) {
        // group：将一个正则表达式分成多个group, group(0)为匹配到的字符
        // groupCount()不包含group(0)，
        String regex = "(\\d{3})(\\d{3})(\\d{4})";

        // 通过Pattern类的静态方法static Pattern.compile() 编译正则表达式，
        // 利用Pattern的*matcher()*方法生产Matcher对象。根据Matcher对象提供的API完成相应的操作
        Pattern p = Pattern.compile(regex);
        String source = "1234567890, 12345,  and  9876543210";

        Matcher m = p.matcher(source);

        while (m.find()) {
            int i = m.groupCount();
            StringBuilder stringBuilder = new StringBuilder();
            for (int j = 0; j < i+1; j++) {
                stringBuilder.append(j).append(": ").append(m.group(j)).append("\t");
            }
            System.out.println(stringBuilder);
        }
        // 0: 1234567890    1: 123    2: 456    3: 7890    
        // 0: 9876543210    1: 987    2: 654    3: 3210    

    }
}


public static void main(String[] args) {
        String reg = "[a-z]+[0-9]+";
        Pattern p = Pattern.compile(reg);
        String str = "abc001122a1@";
        Matcher m =p.matcher(str);
        while(m.find()){
            System.out.println(m.groupCount());
            System.out.println(m.group(0));
//            System.out.println(m.group(1));
            //System.out.println(m.group(2));
        }


    }
```
