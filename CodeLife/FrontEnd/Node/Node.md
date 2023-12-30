Node.js 有着强大而灵活的包管理器（node package manager，npm）  Node.js 是一个让 JavaScript 运行在服务端的开发平台  JavaScript 是由 ECMAScript、文档对象模型（DOM）和浏览器对象模型（BOM）组成的，而 Mozilla 则指出 JavaScript 由  Core JavaScript 和 Client JavaScript 组成  Node.js 中所谓的 JavaScript 只是 Core JavaScript，或者说是 ECMAScript 的一个实现，不包含 DOM、BOM 或者 Client JavaScript。  这是因为 Node.js 不运行在浏览器中，所以不需要使用浏览器中的许多特性    





```bash
node --help
$ node -e "console.log('Hello World');"
Hello World

```



REPL （Read-eval-print loop），即输入—求值—输出循环

运行无参数的 node 将会启动一个 JavaScript的交互式 shell：

```bash
$ node
Welcome to Node.js v20.10.0.
Type ".help" for more information.
> console.log('hel')
hel
undefined // undefined 就是 console.log 的返回值

```



热部署

npm install -g supervisor

supervisor app.js



线程在执行中如果遇到磁盘读写或网络通信（统称为 I/O 操作），
通常要耗费较长的时间，这时操作系统会剥夺这个线程的 CPU 控制权，使其暂停执行，同
时将资源让给其他的工作线程，这种线程调度方式称为 阻塞。当 I/O 操作完毕时，操作系统
将这个线程的阻塞状态解除，恢复其对CPU的控制权，令其继续执行。这种 I/O 模式就是通
常的同步式 I/O（Synchronous I/O）或阻塞式 I/O （Blocking I/O）

异步式 I/O （Asynchronous I/O）或非阻塞式 I/O （Non-blocking I/O）则针对
所有 I/O 操作不采用阻塞的策略。当线程遇到 I/O 操作时，不会以阻塞的方式等待 I/O 操作
的完成或数据的返回，而只是将 I/O 请求发送给操作系统，继续执行下一条语句。当操作
系统完成 I/O 操作时，以事件的形式通知执行 I/O 操作的线程，线程会在特定时候处理这个
事件。为了处理异步 I/O，线程必须有事件循环，不断地检查有没有未处理的事件，依次予
以处理。

Node.js 使用了单
线程、非阻塞的事件编程模式

创建一个线程的代价是十分昂贵的，
需要给它分配内存、列入调度，同时在线程切换的时候还要执行内存换页，CPU 的缓存被
清空，切换回来的时候还要重新从内存中读取信息，破坏了数据的局部性。



![1703936185151](Node.assets/1703936185151.png)

答案是 Node.js 程序由事件循环开始，到事件循
环结束，所有的逻辑都是事件的回调函数，所以 Node.js 始终在事件循环中，程序入口就是
事件循环第一个事件的回调函数。事件的回调函数在执行的过程中，可能会发出 I/O 请求或
直接发射（emit）事件，执行完毕后再返回事件循环，事件循环会检查事件队列中有没有未
处理的事件，直到程序结束

与其他语言不同的是，Node.js 没有显式的事件循环，类似 Ruby 的 EventMachine::run()
的函数在 Node.js 中是不存在的。Node.js 的事件循环对开发者不可见





模块（Module）和包（Package）是 Node.js 最重要的支柱

Node.js 提供了 require 函数来调用其他模快，exports 是模块公开的接口，require 用于从外部获取一个模块的接口，即所获取模块的 exports 对象



require 不会重复加载模块，也就是说无论调用多少次 require



文件和模块是一一对应的，一个Node.js 文件就是一个模块，这个文件可能是 JavaScript 代码、JSON 或者编译过的 C/C++ 扩展

包实现了某个功能模块的集合，Node.js 的包是一个目录，其中包含一个 JSON 格式的包说明文件 package.json



Node.js包管理器，即npm是 Node.js 官方提供的包管理工具

npm在默认情况下会从http://npmjs.org搜索或下载包，将包安装到当前目录的node_modules
子目录下

在使用 npm 安装包的时候，有两种模式：本地模式和全局模式。默认情况下我们使用 npm
install命令就是采用本地模式，即把包安装到当前目录的 node_modules 子目录下。Node.js
的 require 在加载模块时会尝试搜寻 node_modules 子目录，因此使用 npm 本地模式安装
的包可以直接被引用。

使用全局模式安装的包并不能直接在 JavaScript 文件中用 require 获
得，因为 require 不会搜索 /usr/local/lib/node_modules/

```shell
npm [install/i] [package_name] // 
npm [install/i] -g [package_name] //
```

| 模 式    | 可通过 require 使用 | 注册PATH |
| -------- | ------------------- | -------- |
| 本地模式 | 是                  | 否       |
| 全局模式 | 否                  | 是       |

 npm link，它的功能是在本地包和全局包之间创建符号链
接。我们说过使用全局模式安装的包不能直接通过 require 使用，但通过 npm link命令
可以打破这一限制



npm init 可以根据交互式问答产生一个符合标准的 package.json

在发布前，我们还需要获得一个账号用于今后维护自己的包，使用 npm adduser 根据
提示输入用户名、密码、邮箱，等待账号创建完成。完成后可以使用 npm whoami 测验是
否已经取得了账号。
接下来，在 package.json 所在目录下运行 npm publish，稍等片刻就可以完成发布了。
打开浏览器，访问 http://search.npmjs.org/ 就可以找到自己刚刚发布的包了。现在我们可以在
世界的任意一台计算机上使用 npm install byvoidmodule 命令来安装它。图3-6 是npmjs.
org上包的描述页面。
如果你的包将来有更新，只需要在 package.json 文件中修改 version 字段，然后重新
使用 npm publish 命令就行了。如果你对已发布的包不满意（比如我们发布的这个毫无意
义的包），可以使用 npm unpublish 命令来取消发布