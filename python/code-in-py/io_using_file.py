poem = '''\
Programming is	fun
When the work	is	done
if	you	wanna make your work also fun:
	use	Python!
'''
f = open('poem.txt', 'w') #使用open函数指定文件名 和 模式, 'w' 写入模式  'r' 阅读模式 'a' 追加模式
f.write(poem)                                 #'t' 文本模式  'b' 二进制模式
f.close()

f = open('poem.txt')  #默认为 'r'
while True:
    line = f.readline()
    #零长度指示 EOF (end of file)
    if len(line) == 0:
        break
    #每行（`line`）的末尾
    #都已经有了换行符
    # 因为它是从一个文件中进行读取的
    print(line, end=' ')
f.close()


