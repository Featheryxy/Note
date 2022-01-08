def maximum(x, y):
    if x == y:
        print("The numbers are equal")
    elif x < y:
        return y
    else:
        return x

#print(maximum(2,3))
print(maximum(2,2))#每一个函数都在其末尾隐含了一句return None