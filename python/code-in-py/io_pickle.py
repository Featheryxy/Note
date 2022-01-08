#标准模块pickle,可以将任何纯Python对象存储到一个文件中,并在稍后将其取回.这叫做持久地存储对象
import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')#'b' 二进制模式打开文件
pickle.dump(shoplist,f)#封装,Pickleing
f.close()

del shoplist

f = open(shoplistfile,'rb')
storedlist = pickle.load(f)#拆封
print(storedlist)













