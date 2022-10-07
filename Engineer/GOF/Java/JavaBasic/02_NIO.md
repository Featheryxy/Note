## NIO

​	I/O 即 输入输出，是计算机与外界世界的一个接口。IO操作的实际主体是操作系统。在java编程中，一般使用流的方式来处理IO，所有的IO都被视作是单个字节的移动，通过流对象一次移动一个字节。流IO负责把对象转换为字节，然后再转换为对象。

## 1. 简介

NIO: New IO, JDK1.4中引入， NIO主要使用块，效率比传统IO高

### 1.1 阻塞

传统IO方式（阻塞I/O）：在调用InputStream.read() / buffer.readLine()方法时是阻塞的，它会一直等到数据到来或缓冲区已满时或超时时才会返回，并且产生了大量String类型垃圾

NIO（非阻塞IO）：

### 1.2 流与块

NIO和IO最大的区别是数据打包和传输方式。IO是以**流**的方式处理数据，而NIO是以**块**的方式处理数据。

**面向流**的IO一次一个字节的处理数据，一个输入流产生一个字节，一个输出流就消费一个字节。为流式数据创建过滤器就变得非常容易，链接几个过滤器，以便对数据进行处理非常方便而简单，但是面向流的IO通常处理的很慢。

**面向块**的IO系统以块的形式处理数据。每一个操作都在一步中产生或消费一个数据块。按块要比按流快的多，但面向块的IO缺少了面向流IO所具有的优雅性和简单性。



## 2. Buffer

### 2.1 属性

```java
public abstract class Buffer {
    private int mark = -1;
    private int position = 0; // buffer游标
    private int limit; // 记录buffer中字符串长度
    private int capacity; // buffer容量
    ...
}
```

### 2.2 类型

```markdown
无BooleanBuffer
    ByteBuffer
    MappedByteBuffer
    CharBuffer
    DoubleBuffer
    FloatBuffer
    IntBuffer
    LongBuffer
    ShortBuffer
```

### 2.3 常用方法

```markdown
1. 读写
  写入 buffer
    fileChannel.read(buffer)
    buffer.put()
  读出
    fileChannel.write(buffer)
    buffer.read()
2. 其他方法
- lip()： flip方法将Buffer从写模式切换到读模式。调用flip()方法会将position设回0，并将limit设置成之前position的值。  

- rewind() 	Buffer.rewind()将position设回0，所以你可以重读Buffer中的所有数据。limit保持不变，仍然表示能从Buffer中读取多少个元素（byte、char等）。

- clear() position将被设回0，limit被设置成 capacity的值。换句话说，Buffer 被清空了。Buffer中的数据并未清除，只是这些标记告诉我们可以从哪里开始往Buffer里写数据。

- compact()方法将所有未读的数据拷贝到Buffer起始处。然后将position设到最后一个未读元素正后面。limit属性依然像clear()方法一样，设置成capacity。现在Buffer准备好写数据了，但是不会覆盖未读的数据。

- mark() reset()
	通过调用Buffer.mark()方法，可以标记Buffer中的一个特定position。之后可以通过调用Buffer.reset()方法恢复到这个position。例如：

	//在此缓冲区的位置设置标记。
	buffer.mark();
	//多次调用get()的相关操作
	
	//将位置放回标记位置。
	buffer.reset(); 
```

### 2.4 code

```java
public void test() {

        // 1. 创建文件输入流
        FileInputStream fin = null;
        FileOutputStream fout = null;

        try {
            fin = new FileInputStream("hello.txt");
            fout = new FileOutputStream("hello-copy.txt");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // 2. 创建FileChannel对象， 用于读取、写入、映射和操作文件的通道。
        FileChannel finChannel = fin.getChannel();
        FileChannel foutChannel = fout.getChannel();

        // 3. 创建缓冲区
        ByteBuffer buffer = ByteBuffer.allocate(1024);

        //  4. 将数据从通道读到缓冲区
        int eof; // 缓冲区的字符长度为
        try {
            while (true) {
                eof = finChannel.read(buffer);
                if (eof == -1) {
                    break;
                }
                // 重设一下buffer的position=0，limit=position
                buffer.flip();
                foutChannel.write(buffer);

                // 重置buffer，重设position=0,limit=capacity
                buffer.clear();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (finChannel != null) {
                try {
                    finChannel.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (foutChannel != null) {
                try {
                    foutChannel.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            try {
                fin.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                fout.close();
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    }
```

## 3. Scatter/Gather

### 3.1 Scattering Reads

Scattering Reads 是指数据从一个channel读取到多个buffer中

```java
package com.nio;

import java.io.FileInputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

public class ScatteringReads {
    public static void main(String[] args) throws IOException {
        FileInputStream aFile = new FileInputStream("src/readandshow.txt");

        FileChannel inChannel = aFile.getChannel();

        ByteBuffer header = ByteBuffer.allocate(5);
        ByteBuffer body = ByteBuffer.allocate(10);
		// 先填满header,再填body
        ByteBuffer[] bufferArray = {header, body};

        inChannel.read(bufferArray);
        header.flip();
        body.flip();
        System.out.println("-----------------------------");

        while (header.hasRemaining()) {
            System.out.print((char) header.get());
        }

        System.out.println("\n-----------------------------");

        while (body.hasRemaining()) {
            System.out.print((char) body.get());
        }
    }
}
```

### Gathering Writes

Gathering Writes是指数据从多个buffer写入到同一个channel。如下图描述：

```java
package com.nio;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

public class GatheringWrites {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("src/readandshow.txt",true);

        //从此输出流得到一个Channel
        FileChannel channel = fos.getChannel();

        //定义多个buffer,然后分别向这些buffer里面写入一些数据
        ByteBuffer header = ByteBuffer.allocate(10);
        ByteBuffer body = ByteBuffer.allocate(20);

        ByteBuffer bufferArr[] = {header, body};

        //分别向header和body里面写入内容
        byte headerArr[] = {'x', 'y', 'z', 'i', 'j', 'k', 't'};
        byte bodyArr[] = {'A', 'B', 'C', 'D', 'E', 'F'};

        header.put(headerArr);
        body.put(bodyArr);
        System.out.println("header里面的数据量是:" + header.position());
        System.out.println("body里面的数据量是:" + body.position());

        //从写模式切换到读模式
        header.flip();
        body.flip();

        //我们调用channel写buffer数组的方法
        channel.write(bufferArr); //一次性把两个buffer的数据写出去了

        channel.close();
    }
}
```

## 4. 通道传输
