# coding=gbk
class Array():	
	# 初始化，传入数组的容量
	def __init__(self, capacity = 10):
		self.array = [None for _ in range(capacity)]
		self.size = 0
	
	
	# 获取数组的元素个数
	def get_size(self):
		return self.size
	
	
	# 获取数组的容量
	def get_capacity(self):
		return len(self.array)


	# 数组是否为空
	def is_empty(self):
		return self.size == 0
		
		
	def add_first(self, x):
		self.add(0, x)
		
		
	def add_last(self, x):
		self.add(self.size, x)	
	
	# 向指定位置插入元素
	def add(self, index, x):
		if self.size == len(self.array):
			
		
		if index < 0 or index > self.size:
			print('add failed')
		
		for i in range(self.size-1, index, -1):
			self.array[i+1] = self.array[i]
		
		self.array[index] = x
		self.size += 1
		
	
	def resize(self, newCap):
		self.
		

if __name__ == '__main__':
	array = Array(11)
	print(array.add(-1, 0))
	print(array.add_first(1))
	print(array.add_last(11))
	print('capacity: ', array.get_capacity())
	print('size: ', array.get_size())
	print('array: ', array.array)
