shoplist = ['apple', 'mango','carrot','banana']
name = 'swaroop'

#Indexing of 'Subscription' operation
#索引或下标(Subscription) 操作符#
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1]) #banana  倒数第一个
print('Item -2 is', shoplist[-2]) #carrot
print("Character 0 is", name[0])  #s

print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])#Item 1 to -1 is ['mango', 'carrot']
print('Item start to end is', shoplist[:])#Item start to end is ['apple', 'mango', 'carrot', 'banana']

print('characters	1	to	3	is',	name[1:3])#wa  [1,3)
print('characters	2	to	end	is',	name[2:])#aroop
print('characters	1	to	-1	is',	name[1:-1])#waroo
print('characters	start	to	end	is',	name[:])#[swaroop]

print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::-1])

