## 概念

```
// 将函数f应用于值value上, i.e.: f(x)
f.apply(value)
函数中不要返回null，可以返回一个标记值
名称不重要，类型才重要
or else 否则
flat 平坦的
flatMap, 将包含多个流的流展开成

```

引用透明: 函数式程序的输出只能取决于自己的参数

代换模型: 任何函数调用可替换为它的返回值



状态改变:一个初始状态,一个转换过程和一个终止状态

**命令式编程**:不可观测, 有副作用, 只能观测到返回的值类型或者是异常

**函数式编程**:可观测, 无副作用, 只能返回一个值

 副作用: 

- 没有变量改变。
- 没有打印到控制台或其他设备。
- 没有写入文件、数据库、网络或其他什么。
- 没有抛出异常。



### 数学中的函数

函数:函数定义域（ function domain ）的源集（ source set ）和被称为函数陪域（也function codomain ）的目标集（ target set ）之间的关系 

函数定义域 --> 函数陪域

源集 --> 目标集

象(image)集: 在定义域里存在对应元素的陪域元素集被称为函数的像





逆函数:函数未必会有逆函数 C inverse function ） 。 如果 $f^{-1}(x)$是一个从 A 到 B(A 为定义域，B 为陪域）的函数，它的逆函数为 C 1 (x), B 为定义域而 A 为陪域

偏函数:没有在定义域中定义所有元素但是满足其他需求（定义域里不存在任何在陪域里有多个元素与之相对应的元素）的关系 一般称为偏函数（ partial func tion ）如 f(x)=1/x 是一个从 N 到 Q （有理数）的偏函数，因为它对 0 没有定义

全函数:

复合函数: 函数就像积木，可以复合为其他函数 。函数 f 和 q 的复合函数标记为 f。g,读作 f round g 。
$$
f。g = f(g(x)) = f.compose(g) = g.andThen(f) \\

f(x)= x + 2 并且 g(x)=x*2 \\
 则 f 。g(x)=f(g(x)) = x*2+2
$$
多参函数: 一个函数是源集和目标集之间的关系。它并不是多个源集与一个目标集之间的关系。 一个函数不允许有多个参数 。
$$
\because f(x , y) = x + y \\
\because g(y) = x+y \\
\therefore f(x, y) = g(y) \\
\because f(x, y) = f(x)(y) \\
\therefore f(x)(y) = g(y) \\
\therefore g = f(x) ,将函数f应用到x上得到g，再将g应用到y上得到g(y) = x + y
$$


它是一个函数。但是它只有一个参数，即 N x N 的元素。N xN 是所有可能的整数对的集。这个集的元素就是一对整数，更通用的元组
（tuple）表示多个元素的组合，而一对整数其实就是元组的 一个特例。 一对就是持有两个元素的元组。

元组用括号来表示，所以（ 3 , 5 ）是一个元组，也是一个 Nx N 的元素。函数f 可以应用于这个元组：
f ( (3 , 5)) = 3 + 5 = 8 可以按照惯例删除一对括号

**仍然是一个接收一个元组的函数，而不是两个参数的函数**

函数柯里化:函数 f ( x ) ( y ）是 f (x ,y ）的柯里化形式 。对一个元组函数（如果你喜欢可以称为多参函数）应用这种转换就称为柯里化（ currying )  f 的陪域现在不是数字集了 ，而是函数集。将 f 应用于一个整数的结果是一个函数 。 将这个新函数应用 于一个整数的结果是一个整数。

偏应用 函数



f (rate , price) = price I 100 * (100 + rate)

g (price, rate) = price I 100 * (100 + rate)

f (rate) (price ) 和 g (price) (rate) 为偏应用 函数

### Java 中的函数

本质是方法,但是一个方法可以是函数式的，只要它满足纯函数的要求

- 它不能修改函数外的任何东西。外部观测不到内部的任何变化 。
- 它不能修改自己的参数 。
- 它不能抛出错误或异常 。
- 它必须返回 一个值 。
- 只要调用它的参数相同，结果也必须相同。

 ```java
   public add(int a, int b){
       a = 3;
       b = 5;
       return a+b
   }
   // 这是一个函数，值传递，没有改变函数外的值，永远返回8.不依赖方法参数
 ```



所有的实例方法都可以通过在参数里增加外围类(enclosing class ）的类型而变成一个静态方法。

隐式参数：定义在方法外的参数，如实例方法访问类属性可以视为一个外围类实例的隐式参数。

```java
public static int applyTax3(FunctionalMethods x , int a) {
    return a I 100 * 100 + x . percent3 ;
}

f(x) = x^2 + 2
    
```

可以把不访 问 外围类实例的方法安全地标记为静态方法。访问外围类实例的那些方法也可以被标记为静态方法，只需显式地标记它们的隐式参数（外围类实例）

```java
public class Payment {
    public final CreditCard cc;
    public final int amount;


    public Payment(CreditCard cc, int amount) {
        this.cc = cc;
        this.amount = amount;
    }

    // cc 为隐式参数, 可以将cc所属的对象作为函数的变量传入，使其成为显式参数
    public Payment combine1(Payment other) throws Exception {
        if (cc.equals(other.cc)) {
            return new Payment(cc, amount + other.amount);
        } else {
            throw new Exception("Can't combine ");
        }
    }

    //
    public static Payment combine2(Payment payment1, Payment payment2) throws Exception {
        if (payment1.cc.equals(payment2.cc)) {
            return new Payment(payment1.cc, payment1.amount + payment2.amount);
        } else {
            throw new Exception("Can't combine ");
        }
    }

    public void test() throws Exception {
        // 类内调用
        combine2(this, new Payment(null, 1));
    }

    public static void main(String[] args) throws Exception {
        Payment p0 = new Payment(null, 1);
        Payment p1 = new Payment(null, 1);
        Payment p2 = new Payment(null, 1);
        Payment p3 = new Payment(null, 1);

        // 对象标记，隐式
        p0.combine1(p1).combine1(p2);

        // 函数标记，显式
        Payment newPayment = combine2(combine2(combine2(p0 , p1 ) , p2) , p3 );
    }
}

class test {
    public void test1() throws Exception {
        // 类外调用
        Payment newPayment = Payment.combine2(null, null) ;
    }
}

@Data
@NoArgsConstructor
class CreditCard {

}
```



函数由匿名类实现



当 lambda 的实现是一个**单参**的方法调用时，用于替换这个 lambda 的语法

```java
    Function<Double, Double> sin = Math::sin;
    Function<Double, Double> sin2 = a -> Math.sin(a);

```

一个 lambda 访问的局部变量必须是 final 的 , 自 Java 8 起，从匿名类或是 lambda 访问的元素都是隐式 final 的

仅使用一次的函数可以被定义为匿名实例。

在函数式编程里，函数是被当作数据来对待的 。它们可以作为
参数传递给其他函数，可以被函数返回，也可以用于操作

不要相信名称，名称和类型可能没有任何关系 。 务必相信类型 。 类型从不撒谎。 类型是你的好朋友！

## 待办

创建静态和实例变量的默认值为 null



什么是静态引用

Java 8 in Action