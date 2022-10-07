XHR：

Request Headers: 查看Content-Type, 和postman中的要一致

Form Data： request 发送的请求内容



Response：响应内容

Response Preview ：将Response格式化显示

### 请求体与Content-Type头域

**请求参数在body中的格式**以及**请求头中的Content-Type头域**，该头域规定了接口接受的请求参数传值格式

1. x-www-form-urlencoded对应于Content-Type头域为x-www-form-urlencoded的类型，是以键值对形式发送的表单参数，同时参数会携带在url中。
2. form-data对应于Content-Type的multipart/form-data类型，既可以发送键值对也可以进行文件参数传递。
3. raw选项中可以使用请求体原始格式编辑各Content-Type类型对应的参数格式，直接按请求体的格式来进行内容发送。
4. binary选项用于发送文件内容请求。
