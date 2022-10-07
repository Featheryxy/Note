```sql
MERGE INTO [target-table] A USING [source-table sql] B ON([conditional expression] and [...]...)
WHEN MATCHED THEN
	[UPDATE sql]
WHEN NOT MATCHED THEN
	[INSERT sql]
```

判断Ｂ表和Ａ表是否满足ON中条件，如果满足则用B表去更新A表，如果不满足，则将B表数据插入A表

在ON中出现的字段，不可以在WHEN MATCHED THEN中更新

https://blog.csdn.net/jeryjeryjery/article/details/70047022