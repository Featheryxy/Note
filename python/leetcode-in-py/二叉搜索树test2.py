# coding=gbk

class TreeNode:
	'''�����������ڵ�Ķ���'''
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class OperationTree:
	'''��������������'''
	def insert(self, root, val):
		'''�����������������'''
		if root == None:
			root = TreeNode(val)
		elif val < root.val:
			root.left = self.insert(root.left, val)
		elif val > root.val:
			root.right = self.insert(root.right, val)
		return root


	def printTree(self, root):
		# ��ӡ����������(�����ӡ����������)
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
	print('�����ӡ������������', end = ' ')
	op.printTree(root)
	print('')
	print('���ڵ��ֵΪ��', root.val)


