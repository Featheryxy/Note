# coding=gbk

# 使用中序遍历书写原始表达式。
# 后序遍历，使用栈来处理表达式。
# 每遇到一个操作符，就可以从栈中弹出栈顶的两个元素，计算并将结果返回到栈中

class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.left_child = None
		self.right_child = None
		
	def insert_left(self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def insert_right(self, new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.right_child = self.right_child
			self.right_child = t
	
	def get_right_child(self):
		return self.right_child
	
	def get_left_child(self):
		return self.left_child
	
	def set_root_val(self, obj):
		self.key = obj
	
	def get_root_val(self):
		return self.key
		

r = BinaryTree('a')
print(r.get_root_val())  # a
print(r.get_left_child())  # None
r.insert_left('b')
print(r.get_root_val())

print(r.get_left_child())  # <__main__.BinaryTree object at 0x00000295B41C4048> 
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())  # c
print(r.get_left_child().get_root_val())  # b

r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())
