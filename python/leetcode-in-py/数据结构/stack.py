# coding=gbk
# �ܽ���沨�����ʽ��ֵ�� ��һ��ʮ���ƵĶ����Ʊ�����ƥ�����⣬ͼ���������

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
	s = Stack() # ����s �б�����Stack����s�ĵ�ַ
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
	


