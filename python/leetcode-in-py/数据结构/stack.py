# coding=gbk
# 能解决逆波兰表达式求值， 求一个十进制的二进制表达，括号匹配问题，图的深度搜索

class Stack:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items) - 1]
	def size(self):
		return len(self.items)

		

if __name__ == "__main__":
	s = Stack() # 变量s 中保存着Stack对象s的地址
	print(s.is_empty())
	s.push(4)
	s.push('dog')
	print(s.peek())
	s.push(True)
	print("size: ", s.size())
	print(s.peek())
	print(dir(s))
	print(s.items) 
	s.push(8.4)
	


