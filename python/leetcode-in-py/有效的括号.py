# coding=gbk
# 有效表达式的子表达式也应该是有效表达式

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		
		stack = []
		mapping = {')':'(', ']':'[', '}':'{'}
		
		for char in s:
			if char in mapping:
				top_element = stack.pop() if stack else '#'
				
				# element of the stack don't match, return False
				if top_element != mapping[char]:
					return False
			else:
				stack.append(char)
		
		# empty means None, means False 	
		# if stack is empty, return True
		# i.e if stack is False, return True
		return not stack
		
string = '((()' 
s = Solution()
print(s.isValid(string))
