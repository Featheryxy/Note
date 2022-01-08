def bubble_sort(nums):
	n = len(nums)
	# n个数字一共循环n-1次
	for i in range(n - 1):
		# 每次循环找到一个最大值，加入到已排好序的队列中，[disorder-1][order+1]
		for j in range(n-i-1):   # [disorder]
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]

	

from random import randrange
nums = [randrange(100) for i in range(100)]
print(nums)
print("------------------Sorting---------------------")
bubble_sort(nums)
print(nums)

