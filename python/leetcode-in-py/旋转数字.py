# coding=gbk

# ������ת�����ַ������д���

# ���ǳ�һ���� X Ϊ����, �������ÿλ��������ر���ת 180 �Ⱥ������Կ��Եõ�һ����Ч
# �ģ��Һ� X ��ͬ������Ҫ��ÿλ���ֶ�Ҫ����ת��

# ���һ������ÿλ���ֱ���ת�Ժ���Ȼ����һ�����֣� �����������Ч�ġ�0, 1, �� 8 ����
# ת����Ȼ�������Լ���2 �� 5 ���Ի�����ת�ɶԷ���6 �� 9 ͬ��������Щ��������������
# ��ת�Ժ󶼲�������Ч�����֡�
# ����������һ�������� N, ����� 1 �� N ���ж��ٸ��� X �Ǻ�����


class Solution:
	def rotatedDigits(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		count = 0
		for i in range(1, N+1):
			i = str(i)
			if '3' in i or '4' in i or '7' in i:
				continue
			if '2' in i or '5' in i or '6' in i or '9' in i:
				count += 1 
		return count
		

s = Solution()
print(s.rotatedDigits(10))
