def ins_sort(nums):
	n = len(nums)
	# n个数字一共循环n-1次, [nums[0]]为[order]的初始
	for i in range(1, n):
		j = i
		# [disorder]中的元素要和[order]中的每个元素进行对比
		# 一个数与每个数进行比较， 冒泡排序
		while j>0 and nums[j] < nums[j-1]:
			nums[j], nums[j-1] = nums[j-1], nums[j]
			j -= 1

def ins_sort2(nums):
	n = len(nums)
	for i in range(1, n):
		j = i + 1
		while i > 0:
			if nums[j] < nums[i]:
				nums[j], nums[i] = nums[i], nums[j]
				i -= 1
		
			
			
			
from random import randrange
nums = [randrange(100) for i in range(10)]
print(nums)
print("------------------Sorting---------------------")
ins_sort(nums)
print(nums)


