class Robot:
    """表示有一个带有名字的机械人."""
    #类变量,机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name #对象变量   属性引用
        print("(Initializing{})" .format(self.name))
        Robot.population +=1

    def die(self):
        '''我挂了'''
        print("{} is being destroyde!" .format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one." .format(self.name))
        else:
            print("There are still {:d} robots working" .format(Robot.population))

    def say_hi(self):
        """来自机械人的诚挚问候

        没问题,你做的到"""
        print("Greetingss, my masters call me {}".format(self.name))

    @classmethod   #用装饰器（Decorator）将how_many方法标记为类方法 how_many=classmethod(how_many)
    def how_many(cls):
        """打印出当前人口数量"""
        print("We have {:d} robots." .format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
droid2.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destory them")
droid1.die()
droid2.die()
print(Robot.how_many.__doc__)
Robot.how_many()
#所有的类成员都是公开的。但有一个例外：如果你使用数据成员并在其名字中使用双下划线
#作为前缀，形成诸如	 	 __privatevar		这样的形式，Python	会使用名称调整（Name-
#mangling）来使其有效地成为一个私有变量。