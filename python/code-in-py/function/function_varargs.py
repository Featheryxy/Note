#可变参数-- --参数数量是可变的,可以通使用星号来实现
def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print("single_item", single_item)
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1500))