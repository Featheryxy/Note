name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes')

if 'a' in name:
    print('Yes')

if name.find('war') != -1:#	 find方法用于定位字符串中给定的子字符串的位置
    print('Yes')          #。如果找不到相应的子字符串，	 find返回-1

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India','China']
print(delimiter.join(mylist)) #Brazil_*_Russia_*_India_*_China