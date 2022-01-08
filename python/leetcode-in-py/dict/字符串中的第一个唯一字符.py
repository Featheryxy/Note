# coding=gbk

# ����һ���ַ������ҵ����ĵ�һ�����ظ����ַ���������������������������ڣ��򷵻� -1
# s = "leetcode"
# ���� 0

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
