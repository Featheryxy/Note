# coding=gbk

class TreeNode:
	'''二叉搜索树节点的定义'''
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class OperationTree:
	'''二叉搜索树操作'''
	def insert(self, root, val):
		'''二叉搜索树插入操作'''
		if root == None:
			root = TreeNode(val)
		elif val < root.val:
			root.left = self.insert(root.left, val)
		elif val > root.val:
			root.right = self.insert(root.right, val)
		return root


	def printTree(self, root):
		# 打印二叉搜索树(中序打印，有序数列)
		if root == None:
			return 
		self.printTree(root.left)
		print(root.val, end = ' ')
		self.printTree(root.right)

if __name__ == '__main__':
	List = [17,5,35,2,11,29,38,9,16,8]
	root = None
	op = OperationTree()
	for val in List:
		root = op.insert(root, val)
	print('中序打印二叉搜索树：', end = ' ')
	op.printTree(root)
	print('')
	print('根节点的值为：', root.val)


