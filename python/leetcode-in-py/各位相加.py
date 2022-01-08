# coding=gbk
# ����һ���Ǹ����� num������������λ�ϵ�������ӣ�ֱ�����Ϊһλ
# ����: 38
# ���: 2


class Solution:
	def addDigits1(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		
		str_nums = str(num)
		n = len(str_nums)
		
		if n == 1:
			return num
		
		while n > 1:
			ret = 0
			for str_num in str_nums:
				ret += int(str_num)
			str_nums = str(ret)
			n = len(str_nums)
			
		return ret
	
	
	def addDigits2(self, num):
		str_num = str(num)
		
		while len(str_num) > 1:
			str_num = str(sum(map(int, str_num)))
		
		return int(str_num)
		
		
		
	def addDigits3(self, num):
		while True:
			m = 0
			while num > 0:
				m += num % 10	
				num = int(num / 10)
				# num = num // 10
			if m % 10 == m:  # m // 10 = 0
				return m
			
			num = m
		
		
		
		
		
		

num = 38   
print(Solution().addDigits1(num))
print(Solution().addDigits2(num))
print(Solution().addDigits3(num))

