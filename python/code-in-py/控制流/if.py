number = 23
guess = int(input("Enter an integer: "))
#input() 以字符串的形式返回我们输入的内容
#int 是一个类
#if...elif...else
if  guess == number:
    print("Congratulation!")
elif guess < number:
    print("smaller")
else: #":"   分号不能忘 冒号表示后头有一块语句
    print("bigger")