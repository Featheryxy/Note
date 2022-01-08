# coding=gbk
# 优先队列问题，广度优先搜索问题
# 左边（0）进，右边(len(self.items)-1)出


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
