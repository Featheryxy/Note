# coding=gbk

# ���������ַ��� s �� t ����дһ���������ж� t �Ƿ��� s ��һ����ĸ��λ��

# ����: s = "anagram", t = "nagaram"
# ���: true

# method: ֻҪ t �к� s ���ַ���һ������Ŀ��һ��,��t, s Ϊ��Ч����ĸ��λ��
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
	
