# coding=gbk

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词

# 输入: s = "anagram", t = "nagaram"
# 输出: true

# method: 只要 t 中和 s 中字符都一样且数目都一样,则t, s 为有效的字母异位词
from collections import Counter
def isAnagram(s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		c1 = Counter(s)
		c2 = Counter(t)
		if c1 == c2:
			return True
		else:
			return False
		
		
		
if __name__ == "__main__":
	
	s = "anagram"
	t = "nagaram"
	print(isAnagram(s, t))
	
