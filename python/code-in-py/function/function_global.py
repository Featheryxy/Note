x = 50

def func(): #不需要形式参数  no paramaters
    global  x

    print("x is", x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)