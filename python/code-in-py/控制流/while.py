number = 23
running = True
# while...else
while running:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("Yes")
    elif guess <number:
        print("small")
    else:
        print("Big")
else:
    print("the while loop is over")