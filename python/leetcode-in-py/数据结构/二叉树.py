class Node:
	def __init__(selt, item):
		self.item = item
		self.l_child = None
		self.r_chile = None
		
		
class Tree:
	def __init__(self):
		self.root = None
	

	def add(self, item):
		node = Node(item)
		if self.root is None:
			self.root = node
		else:
			q = [self.root]
			
			
			while True:
				pop_node = q.pop(0)
				if pop_node.child1 is None:
					pop_node.child1 = node
					return 
				elif pop

