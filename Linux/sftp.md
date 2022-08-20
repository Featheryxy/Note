SFTP（Secure File Transfer Protocol，安全文件传输协议） 

```
1. 连接远程服务器
sftp remote_user@remote_host
2. 使用端口进行连接
sftp -P remote_port remote_user@remote_host
3. 从远程服务器拉取文件
get /path/remote_file
get -r ./. # 拉取远程的 当前目录下的 所有 子目录及里面的 文件
4. 上传本地文件到服务器
put local_file
5. 查看远程服务器目录内容
ls
6.查看本地目录内容
lls  # l = local
7.执行本地 Shell 命令
![command]
```

