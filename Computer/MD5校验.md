# MD5校验

CertUtil -hashfile C:\xxx.tar MD5 

此命令不仅可以做MD5哈希算法校验，还支持其他的哈希算法，具体如下： 

CertUtil -hashfile 文件路径 [算法] 

支持的算法有：MD2 MD4 MD5 SHA1 SHA256 SHA384 SHA512

```powershell
PS F:\\BaiduNetdiskDownload> CertUtil -hashfile .\\WePE_64_V2.1.exe MD5
MD5 的 .\\WePE_64_V2.1.exe 哈希:
55c4aeba8a2b43b97f0792ba65a434b8
CertUtil: -hashfile 命令成功完成。
```

Reference：https://blog.csdn.net/jiajiren11/article/details/80341149

