# coding=gbk

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1
# s = "leetcode"
# 返回 0

from collections import Counter
def firstUniqChar(s):
		"""
		:type s: str
		:rtype: int
		"""

		dict1 = dict()
		for i in range(len(s)):
			if s[i] in dict1:
				dict1[s[i]] += 1
			else:
				dict1[s[i]] = 1
		for i in range(len(s)):
			if dict1[s[i]] == 1:
				return i
		return -1




if __name__ == "__main__":
	s = "leetcode"
	print(firstUniqChar(s))
