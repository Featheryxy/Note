# coding=gbk
# �ȼ���쳲���������
# ������������¥�ݡ���Ҫ n ������ܵ���¥����
# ÿ��������� 1 �� 2 ��̨�ס����ж����ֲ�ͬ�ķ�����������¥���أ�


# ���룺 3
# ����� 3
# ���ͣ� �����ַ�����������¥����
# 1.  1 �� + 1 �� + 1 ��
# 2.  1 �� + 2 ��
# 3.  2 �� + 1 ��

class Solution:
	
	# �ݹ飺�Զ�����
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 2:
			return n
		else:
			# ������
			return self.climbStairs(n-1) + self.climbStairs(n - 2)
	
	
	# ����¼��
	def f(self, n):
		dic = dict()
		if n <= 2:
			return n
		else:
			if n in dic.keys():
				return dic[n]
			else:
				dic[n] = self.f(n-1) + self.f(n-2)
				return dic[n]
				

				
			
	
	
	
s = Solution()
print(s.climbStairs(30))
print(s.f(30))
