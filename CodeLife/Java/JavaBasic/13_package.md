## Package

### package name

包名：将一个**因特网域名的逆序**形式作为包名。考虑域名horstmann.com, 工程名为corejava，Employee为包下的类。则**完全限定名(fully qualified name)**为com.horstmann.com.Employee

### 类的导入

```java
import java.time.LocalDate;

public class packtest {
	public static void main(String[] args) {
		java.time.LocalDate today = java.time.LocalDate.now();
		// 等价于
		LocalDate.now();
	}
}
```

### 静态导入

```java
import static java.lang.Math.*;

public classpacktest {
	public static voidmain(String[] args) {
	      Math.pow(2,2);
				// 等价于
				pow(2,2);
	   }
}
```

