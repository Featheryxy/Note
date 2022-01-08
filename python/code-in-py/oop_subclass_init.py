class SchoolMember:
    def __init__(self):
        print("This Father")

class Student(SchoolMember):
   def __init__(self):
        SchoolMember.__init__(self)
        print("This is son")

class Teacher(SchoolMember):
    pass

Student()  #This is son  与java不同,不会自动调用基类的构造函数
Teacher()  #This Father  如果我们没有在一个子类中定义一个 __init__方法，Python将会自动调用基类的构造函数。
