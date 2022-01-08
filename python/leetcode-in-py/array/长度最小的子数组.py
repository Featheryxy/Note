# coding=gbk
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的
# 连续子数组。如果不存在符合条件的连续子数组，返回 0

# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

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
	
	# 维护一个滑动窗口nums[i,j], nums[i...j] < s
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
