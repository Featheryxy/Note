# coding=gbk
# ���ȶ������⣬���������������
# ��ߣ�0�������ұ�(len(self.items)-1)��


class Queue:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
		
		
if __name__ == "__main__":
	q = Queue()
	q.enqueue("hello")
	q.enqueue("dog")
	q. enqueue(3)
	print(q.items)
	q.dequeue()
	print(q.items)
