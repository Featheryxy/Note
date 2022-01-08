class Node():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	
class BinarySearchTree():
	def __init__(self):
		self.root = None
		self.size = 0
	
	
	def size(self):
		return self.size


	def is_empty(self):
		return self.size == 0
		
		
	def add(self, root, val):
		
		if root is None:
			self.size += 1
			root = Node(val)
		elif val < root.val:
			root.left = self.add(root.left, val)
		elif val > root.val:
			root.right = self.add(root.right, val)				
		return root
		
		
	def contains(self, root, val):
		if root.val == val:
			return True
		
		elif root.val < val:
			return self.contains(root.right, val)
		else: 
			return self.contains(root.left, val)
			
		return False
		
	
	def find_max(self, root):
		if root.right:
			return self.find_max(root.right)
		else:
			return root
		
	
	def preorder(self, root):
		if root == None:
			return 
		
		print(root.val, end = ' ')
		self.preorder(root.left)
		self.preorder(root.right)
		
	
	# 非递归实现先序打印， 使用 stack 来实现。
	# 先将根节点压栈， 再压该节点的右孩子节点和左孩子节点
	# 一次只pop出一个节点	
	def preorder_nr(self, root):
		List = list()
		# List 中存放节点的node 的地址
		List.append(root)
		
		while len(List)!= 0:
			cur = List.pop()
			print(cur.val, end = ' ')
			if cur.right:
				List.append(cur.right)
			if cur.left:
				List.append(cur.left)

	
	# 使用队列进行层次遍历, [tail, front]
	def levelorder(self, root):
		List = list()
		List.insert(0, root)
		
		while len(List) != 0:
			cur = List.pop()
			print(cur.val, end = ' ')
			if cur.left:
				List.insert(0, cur.left)
			if cur.right:
				List.insert(0, cur.right)
			
	
			
	
	def inorder(self, root):
		if root == None:
			return 
		
		self.inorder(root.left)
		print(root.val, end = ' ')
		self.inorder(root.right)


if __name__ == '__main__':
	List = [28, 16, 30, 13, 22, 29,42]
	bst = BinarySearchTree()
	
	root = None
	for val in List:
		root = bst.add(root, val)
		
	print('先序打印二叉搜索树：')		
	bst.preorder(root)
	print()
	print('中序打印二叉搜索树：')		
	bst.inorder(root)
	print()	
	print('非递归先序打印二叉搜索树：')
	bst.preorder_nr(root)
	print()	
	print('层次遍历打印二叉搜索树：')
	bst.levelorder(root)
	print()	
	print('树中最大值为:', bst.find_max(root).val)


	
