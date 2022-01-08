zoo = ('python', 'elephant', 'penguin')#括号可以省略,变量zoo指的是包含项目的元组
print('Numbei of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo#zoo是一个元祖,元祖内可以嵌套元组
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print("Animals brought from old zoo are",new_zoo[2])#new_zoo[2] == zoo  []索引运算符
print("Last animal brought from old zoo is",new_zoo[2][2])# new_zoo中的第三个元素zoo中的第三个元素penguin
print("Number of animals in the new zoo is",
      len(new_zoo)-1+len(new_zoo[2]))