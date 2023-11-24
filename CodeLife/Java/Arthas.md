https://arthas.aliyun.com/doc/

```bash
java -jar arthas-boot.jar


watch com.hundsun.lcpt.bizframe.util.ManageUtil getDictMap -x 2 -b -s -n 2
-b 函数调用之前
-s 函数返回之后
-e 函数异常之后
-n 函数执行次数？

重入 arthas
telnet localhost port_id


watch com.hundsun.lcpt.ta.pub.trust.services.impl.TrustPrdDailyNavService getMultiWorkDayNavDate -x 2 -b 
```