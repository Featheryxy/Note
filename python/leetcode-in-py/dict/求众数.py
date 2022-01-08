# coding=gbk

# 输入: [2,2,1,1,1,2,2]
# 输出: 2


class Solution:
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		
		dic = {}

		for num in nums:
			if num in dic:
				dic[num] += 1
			else:
				dic[num] = 1
		max_num = max(list(dic.values()))
		for key, value in dic.items():
			if value == max_num:
				return key
		

	def majorityElement1(self, nums):
		from collections import Counter
		nums = Counter(nums)
		return nums.most_common(1)[0][0]
				
if __name__ == "__main__":
	nums = [2,2,1,1,1,2,2]
	s = Solution()
	print(s.majorityElement(nums))
