print('Simple Assignment')
shoplist = ['apple', 'mango','carrot','banana']
#	mylist	只是指向同一对象的另一种名称
mylist = shoplist

del shoplist[0]

print('shoplist is', shoplist)
print("shoplist is", mylist)