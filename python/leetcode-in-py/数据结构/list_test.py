# coding=gbk
# while node:   ֻҪ��ǰ�ڵ����
# while node.next:	ֻҪ��ǰ�ڵ������һ���ڵ�

class Node:
	def __init__(self, x):
		self.val = x 
		self.next = None
	
# ͷ��㣬��n���ڵ㣬 n = 1,2,...,n
class List:
	def __init__(self, node):
		self.init_node(node)
		self.head = node
	
	
	def init_node(self, node):
		if not isinstance(node, Node):
			return Node(node)
		return node
	
	
	def append(self, node):		
		temp = self.head
		# �ӵ�һ���ڵ㿪ʼ
		while temp.next is not None:
			temp = temp.next
		temp.next = self.init_node(node)
		
	
	def traverse(self):           # ��ӡ����
		init_data = []
		temp = self.head
		# ��ͷ��㿪ʼ
		while temp is not None:
			init_data.append(temp.val)
			temp = temp.next
		return init_data
	
	
	def get_len(self):
		n = 0
		temp = self.head
		# ͷ��㲻����������
		while temp.next is not None:
			n += 1
			temp = temp.next
		return n
		
		
	def is_empty(self):
		return self.get_len() == 0
		
		
	def insert(self, pos, node):
		if pos < 1 or pos > self.get_len():
			print("����ڵ�λ�ò�����...")
		
		node = self.init_node(node)
		temp = self.head
		# ��ʼλ��Ϊ-1��ͷ���λ��Ϊ0
		cur_pos = -1
		
		while temp is not None:
			# ͷ���λ��Ϊ0,Ϊ��ǰ�ڵ���
			cur_pos += 1
			# �ҵ�Ҫ����ڵ��ǰһ���ڵ�
			if cur_pos == pos-1:
				node.next = temp.next
				temp.next = node
				break
			temp = temp.next
				
		
	def delete(self, pos):
		if pos < 1 or pos > self.get_len():
			print("ɾ���ڵ�λ�ò�����...")
		
		cur_pos = -1
		val = 'x'
		temp = self.head
		while temp is not None:
			cur_pos += 1
			# �ҵ�Ҫɾ���ڵ��ǰһ���ڵ�
			if cur_pos == pos-1:
				val = temp.next.val
				temp.next = temp.next.next
			temp = temp.next
		return val
		
		
	def err_reverse(self):
		p = self.head.next
		q = p.next
		self.head.next = None
		
		while p:
			p.next = self.head.next
			self.head.next = p
			p = q 
			q = q.next
			
	
	def reverse(self):
		if self.get_len() == 1:
			return 
		pre = self.head.next
		cur = pre.next
		# û���¾䣬���в�ͨ
		pre.next = None
		while cur:
			temp = cur.next
			cur.next = pre
			pre = cur
			cur = temp
		self.head.next = pre
		
	
	def get_middle(self):
		m = self.get_len() // 2 + 1
		temp = self.head
		cur_pos = -1
		while temp:
			cur_pos += 1
			if cur_pos == m:
				return temp.val
			temp = temp.next
			
	
	def get_middle1(self):
		m = self.get_len() // 2 + 1
		temp = self.head
		
		while m:
			temp = temp.next
			m = m - 1
		
		return temp.val
		
		
	def delete_double(head)
        set0 = set()
        p = head
        set0.add(p.val)
        
        while p.next:
            if p.next.val in set0:
                p.next = p.next.next
                p = p.next
            else:
                set0.add(p.next.val)
        
        return head
                
		


			

									
		
if __name__ == '__main__':
	from time import time
	
	head = Node('head')
	linked_list = List(head)
	
	for i in range(1, 7):
		linked_list.append(i)
	print('�������ɣ� ', linked_list.traverse())
	
	print('�����ȣ� ', linked_list.get_len())
	
	print('����Ϊ�գ� ', linked_list.is_empty())
	
	begin1 = time()
	middle = linked_list.get_middle()
	t1 = time() - begin1
	print('�м�ڵ�ֵΪ�� {}, ʱ��: {}'.format(middle, t1))
	
	begin2 = time()
	middle = linked_list.get_middle1()
	t2 = time() - begin2
	print('�м�ڵ�ֵΪ�� {}, ʱ��: {}'.format(middle, t2))
	
	pos, value = 1, 0
	linked_list.insert(pos,value)
	print('�ڵ�{0}��λ���ϲ���ڵ�{1}�� {2}'.format(pos, value, linked_list.traverse()))
	
	pos = 1
	value = linked_list.delete(pos) 
	print('ɾ����{0}������ ֵΪ{1}: {2}'.format(pos, value, linked_list.traverse()))
	
	
	linked_list.reverse()
	print('����ת�� ', linked_list.traverse())
	
	
	from random import randint
	head1 = Node('head1')
	linked_list1 = List(head1)
	
	head2 = Node('head2')
	linked_list2 = List(head2)

	for i in range(7):
		linked_list1.append(randint(0, 10))
	print("����A�� ", linked_list1.traverse())
	
	for i in range(5):
	linked_list1.append(randint(0, 10))
	print("����A�� ", linked_list1.traverse())
	
	
		
	
