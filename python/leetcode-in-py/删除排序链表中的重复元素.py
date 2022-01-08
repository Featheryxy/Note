# coding=gbk

from list_test import List, Node
from random import randint

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        p = head
        q = p.next
        
        while q:
            if q.val != p.val:
                p = q
                q = q.next
            else:
                p.next = q.next
                q = q.next                  
        return head

if __name__ == '__main__':

	head = Node('head')
	linked_list = List(head)
	for i in range(10):
		linked_list.append(randint(0, 10))
	print('链表生成： ', linked_list.traverse())


