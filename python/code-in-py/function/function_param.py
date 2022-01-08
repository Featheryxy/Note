def print_max(a, b):#在定义函数时给定的名称称作“形参”（Parameters）
                    #在调用函数时你所提供给函数的值称作“实参”（Arguments）
    if a == b:
        print(a,'is equal to',b)
    elif a < b:
        print(b, "is maximum")
    else:
        print(a, "is maximum")

print_max(3,4)

x = 6
y = 7
print_max(x, y)