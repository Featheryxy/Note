while True: #break语句用于中断循环语句
            #，如果你的中断了一个for或while循环，任何相应循环中的else块都将不会被执行。
    s = input("Enter something :")
    if s == 'quit':
        break
    print("Length of the string is", len(s))