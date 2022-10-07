依赖导入

```xml
<!-- 单元测试模块 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-logging</artifactId>
                </exclusion>
            </exclusions>
            <scope>test</scope>
        </dependency>
```



同级目录

```java
package ###;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.sql.SQLException;

@SpringBootTest(
        classes = ServerStarter.class
)
public class ServerStarterTest {
    @Autowired
    private OnlineServiceConfigration configration;

    @Test
    public void testGetOutBankCodeByProjectNo() throws BizBussinessException {
        String outBankCode = PubTrustApiFactory.getOutBankCodeByProjectNo("jksfgh");
        System.out.println(outBankCode);
    }
}

```

