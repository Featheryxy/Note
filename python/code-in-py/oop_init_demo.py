class Person:
    def __init__(self,local_name):#__init__方法用以接受name参数
        self.name = local_name#字段self.name, self.name 这个name是某个叫做self的对象的一部分
                        # =name 是一个局部变量
    def say_hi(self):
        print("Hello,",self.name)

p = Person('Swaroop')
p.say_hi()

Person('Swaroop').say_hi()