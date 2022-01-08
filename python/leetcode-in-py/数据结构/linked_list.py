class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data
		

class List:
	def __init__(self, head):
		if not isinstance(head, Node):
			head = Node(head)
		self.head = head
	
	def is_empty(self):
		return self.get_len() == 0
		
	def get_len(self):
		length = 0
		temp = self.head
		while temp is not None:
			length += 1
			temp = temp.next
		return length
		
	def append(self, node):
		if not isinstance(node, Node):
			node = Node(node)
		
		temp = self.head
		while temp.next is not None:
			temp = temp.next
		temp.next = node
		
	def delete(self, index):
		if index < 1 or index > self.get_len():
			print("cross the border")
			return 
		if index == 1:
			self.head = self.head.next
			return 
		temp = self.head
		cur_pos = 0
		while temp is not None:
			cur_pos += 1
			if cur_pos == index-1:
				temp.next = temp.next.next
			temp = temp.next
			
	def insert(self, pos, node):         # 插入结点
			if pos < 1 or pos > self.get_len():
				print("插入结点位置不合理...")
				return
			temp = self.head
			cur_pos = 0
			while temp is not Node:
				cur_pos += 1
				if cur_pos == pos-1:
					node.next = temp.next
					temp.next = node
					break
				temp = temp.next



		
	def reverseList(self, head):
		p = None
		while head is not None:
			q = head
			head = head.next
			q.next = p
			p = q
		head = p
		return head
		
		
	def middleNode(self, head):
		n = self.get_len()
		m = n // 2 + 1
		cur_pos = 0
		temp = self.head
		while temp is not None:
			cur_pos += 1
			if cur_pos == m:
				return temp.data
			temp.next = temp.next.next
			

	def print_list(self, head):           # 打印链表
		init_data = []
		while head is not None:
			init_data.append(head.get_data())
			head = head.next
		return init_data
		
if __name__ == '__main__':

	head = Node("head")
	list = List(head)
	print('初始化头结点：\t', list.print_list(head))

	for i in range(1, 11):
		list.append(i)
	print('链表添加元素：\t', list.print_list(head))

	print('链表是否空：\t', list.is_empty())

	print('链表长度：\t', list.get_len())

	# list.delete(9)
	# print('删除第9个元素:\t',list.print_list(head))

	# node = Node("insert")
	# list.insert(3, node)
	# print('第3个位置插入‘insert’字符串 :\t', list.print_list(head))
	
	# head = list.reverse(head)
	
	middle = list.middleNode(head)
	print('链表的中间节点： ', middle)

	head = list.reverseList(head)
	print('链表反转：', list.print_list(head))

		
