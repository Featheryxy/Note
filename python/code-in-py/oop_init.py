class Person:
    def __init__(self, name):#__init__方法用以接受name参数,self不能省略
        self.name = name#字段self.name, self.name 这个name是某个叫做self的对象的一部分
                        # =name 是一个局部变量,即从第二行传入的name
    def say_hi(self):
        print("Hello,",self.name)

p = Person('Swaroop')
p.say_hi()
#也可写成下式
Person('Swaroop').say_hi()