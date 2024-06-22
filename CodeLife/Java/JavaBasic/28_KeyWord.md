### switch

switch 只支持整型 如 byte, short, char,inte

字符串通过hashCode来支持，switch 通过 ordinary

执行顺序，若无break，则依次向下穿透

### static

static 类型的属性会在类被加载之后初始化

java类的加载都是线程安全的，使用同步代码块

### 同步/异步与阻塞/非阻塞

I/O发生时，一定有两方参与，分为调用方和被调用方

阻塞/非阻塞 描述 调用方

同步/异步 描述 被调用方