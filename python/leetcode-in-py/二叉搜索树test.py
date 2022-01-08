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

	def query(self, root, val):
		'''������������ѯ����'''
		if root == None:
			return False
		if root.val == val:
			return True
		elif val < root.val:
			return self.query(root.left, val)
		elif val > root.val:
			return self.query(root.right, val)

	def findMin(self, root):
		'''���Ҷ�������������Сֵ��'''
		if root.left:
			return self.findMin(root.left)
		else:
			return root

	def findMax(self, root):
		'''���Ҷ��������������ֵ��'''
		if root.right:
			return self.findMax(root.right)
		else:
			return root

	def delNode(self, root, val):
		'''ɾ��������������ֵΪval�ĵ�'''
		if root == None:
			return 
		if val < root.val:
			root.left = self.delNode(root.left, val)
		elif val > root.val:
			root.right = self.delNode(root.right, val)
		# ��val == root.valʱ����Ϊ���������ֻ������������ֻ������������������������������������������
		else:
			if root.left and root.right:
				# ���������������������������ҵ�����������Сֵ�ڵ�
				temp = self.findMin(root.right)
				root.val = temp.val
				# �ٰ�����������Сֵ�ڵ�ɾ��
				root.right = self.delNode(root.right, temp.val)
			elif root.right == None and root.left == None:
				# ����������Ϊ��
				root = None
			elif root.right == None:
				# ֻ��������
				root = root.left
			elif root.left == None:
				# ֻ��������
				root = root.right
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
		root = op.insert(root,val)
	print('�����ӡ������������', end = ' ')
	op.printTree(root)
	print('')
	print('���ڵ��ֵΪ��', root.val)
	print('�������ֵΪ:', op.findMax(root).val)
	print('������СֵΪ:', op.findMin(root).val)
	print('��ѯ����ֵΪ5�Ľڵ�:', op.query(root, 5))
	print('��ѯ����ֵΪ100�Ľڵ�:', op.query(root, 100))
	print('ɾ������ֵΪ16�Ľڵ�:', end = ' ')
	root = op.delNode(root, 16)
	op.printTree(root)
	print('')
	print('ɾ������ֵΪ5�Ľڵ�:', end = ' ')
	root = op.delNode(root, 5)
	op.printTree(root)
	print('')

