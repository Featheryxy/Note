# Lombok

### 简介

Project Lombok is a java library that automatically plugs into your editor and build tools, spicing up（使更活跃） your java.Never write another getter or equals method again, with one  annotation your class has a fully featured builder, Automate your  logging variables, and much more.         

### 原理

JSR 269：插件化注解处理API（Pluggable Annotation Processing API）

- JDK 6提供的特性，在Javac编译期利用注解搞事情

### 安装

Maven

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.24</version>
    <scope>provided</scope>
</dependency>
```

IDEA

- Go to `File > Settings > Plugins`         
     Click on `Browse repositories...`         
     Search for `Lombok Plugin`         
     Click on `Install plugin`         
     Restart IntelliJ IDEA         

### Features

https://projectlombok.org/features/all

### @Getter and @Setter

```java
package com.example.web_demo.pojo;

import lombok.AccessLevel;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class User {
    static String s = ""; // 没有get，set方法
    final int id2 = 10;  // 只有get方法
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    @Getter(AccessLevel.NONE)
    @Setter(AccessLevel.NONE)
    private String email;  // 没有get，set方法
}
```

```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.example.web_demo.pojo;

public class User {
    static String s = "";
    final int id2 = 10;
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;

    public User() {
    }

    public int getId2() {
        this.getClass();
        return 10;
    }

    public Integer getId() {
        return this.id;
    }

    public String getUserName() {
        return this.userName;
    }

    public String getPassword() {
        return this.password;
    }

    public String getPhone() {
        return this.phone;
    }

    public void setId(final Integer id) {
        this.id = id;
    }

    public void setUserName(final String userName) {
        this.userName = userName;
    }

    public void setPassword(final String password) {
        this.password = password;
    }

    public void setPhone(final String phone) {
        this.phone = phone;
    }
}
```

### @ToString

```java
package com.example.web_demo.pojo;

import lombok.ToString;

@ToString() // 默认输出全部
//@ToString(exclude = {"phone, email"}) // 不输出phone， email
@ToString(of = {"id"})  // 只输出 id

public class User {
    static String s = "";
    final int id2 = 10;
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;
}
```

```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.example.web_demo.pojo;

public class User {
    static String s = "";
    final int id2 = 10;
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;

    public User() {
    }

    public String toString() {
        return "User(id=" + this.id + ")";
    }
}
```

### @EqualsAndHashCode

```java
package com.example.web_demo.pojo;

import lombok.EqualsAndHashCode;


@EqualsAndHashCode(of = {"id"})
public class User {
    static String s = "";
    final int id2 = 10;
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;
}
```

```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.example.web_demo.pojo;

public class User {
    static String s = "";
    final int id2 = 10;
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;

    public User() {
    }

    public boolean equals(final Object o) {
        if (o == this) {
            return true;
        } else if (!(o instanceof User)) {
            return false;
        } else {
            User other = (User)o;
            if (!other.canEqual(this)) {
                return false;
            } else {
                Object this$id = this.id;
                Object other$id = other.id;
                if (this$id == null) {
                    if (other$id != null) {
                        return false;
                    }
                } else if (!this$id.equals(other$id)) {
                    return false;
                }

                return true;
            }
        }
    }

    protected boolean canEqual(final Object other) {
        return other instanceof User;
    }

    public int hashCode() {
        int PRIME = true;
        int result = 1;
        Object $id = this.id;
        int result = result * 59 + ($id == null ? 43 : $id.hashCode());
        return result;
    }
}
```

### @NonNull

```java
package com.example.web_demo.pojo;

import lombok.NonNull;


public class User {
    static String s = "";
    final int id2 = 10;
    @NonNull private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;

    public void test(@NonNull String s){
        System.out.println(s);
    }

    public static void main(String[] args) {
        User user = new User();
        user.test(null);
        // Exception in thread "main" java.lang.NullPointerException: s is marked non-null but is null

    }
}
```

```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.example.web_demo.pojo;

import lombok.NonNull;

public class User {
    static String s = "";
    final int id2 = 10;
    @NonNull
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;

    public User() {
    }

    public void test(@NonNull String s) {
        if (s == null) {
            throw new NullPointerException("s is marked non-null but is null");
        } else {
            System.out.println(s);
        }
    }

    public static void main(String[] args) {
        User user = new User();
        user.test((String)null);
    }
}
```

### @RequiredArgsConstructor

```java
package com.example.web_demo.pojo;

import lombok.NonNull;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class User {
    static String s = "";
    final int id2;
    @NonNull private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;
}
```

```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.example.web_demo.pojo;

import lombok.NonNull;

public class User {
    static String s = "";
    final int id2;
    @NonNull
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;

    public User(final int id2, @NonNull final Integer id) {
        if (id == null) {
            throw new NullPointerException("id is marked non-null but is null");
        } else {
            this.id2 = id2;
            this.id = id;
        }
    }
}
```

### @AllArgsConstructor

```java
package com.example.web_demo.pojo;

import lombok.AllArgsConstructor;
import lombok.NonNull;

@AllArgsConstructor
public class User {
    static String s = "";
    final int id2;
    @NonNull private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;
}
```

```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package com.example.web_demo.pojo;

import lombok.NonNull;

public class User {
    static String s = "";
    final int id2;
    @NonNull
    private Integer id;
    private String userName;
    private String password;
    private String phone;
    private String email;

    public User(final int id2, @NonNull final Integer id, final String userName, final String password, final String phone, final String email) {
        if (id == null) {
            throw new NullPointerException("id is marked non-null but is null");
        } else {
            this.id2 = id2;
            this.id = id;
            this.userName = userName;
            this.password = password;
            this.phone = phone;
            this.email = email;
        }
    }
}
```

### @Data

集成了@Getter, @Setter, @ToString, @RequireArgsConstructor

### JavaBean

```
@Data
@AllArgsConstructor
@NoArgsConstructor
```