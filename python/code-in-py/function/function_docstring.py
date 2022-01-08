def print_max(x, y): #文档字符串（Documentation	Strings） docstring
    '''Prints the maximum of two numbers.打印两个数字中的最大数.

    The two values must be integers.这两个数都应该是整数'''

    x = int(x)
    y = int(y)

    if x>y:
        print(x,'is maximum')
    else:
        print(y, 'is maximum')


print_max(3,5)
print(print_max.__doc__)
help(print_max(3,4))