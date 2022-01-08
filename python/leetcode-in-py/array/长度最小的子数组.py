# coding=gbk
# ����һ������ n ���������������һ�������� s ���ҳ���������������� �� s �ĳ�����С��
# ���������顣��������ڷ������������������飬���� 0

# ����: s = 7, nums = [2,3,1,2,4,3]
# ���: 2
# ����: ������ [4,3] �Ǹ������µĳ�����С�����������顣

def minSubArrayLen(s, nums):
	"""
	:type s: int
	:type nums: List[int]
	:rtype: int
	"""
	i, j, n = 0, -1, len(nums)
	total = 0
	min_len = n + 1
	
	if n<1 or sum(nums)<s:
		return 0
	
	# ά��һ����������nums[i,j], nums[i...j] < s
	while i <= n-1:
		if j+1 < n and total < s:
			j += 1
			total += nums[j]
		else:
			total -= nums[i]
			i += 1
		if total >= s:
			min_len = min(min_len, j-i+1)
			
	if min_len == n+1:
		return 0
	return min_len
	
if __name__ == "__main__":
	nums = [2,3,1,2,4,3]
	s = 7
	n = minSubArrayLen(s, nums)
	print(n)
