# coding=gbk

# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]


def sortColors(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	
	a, b, c = 0, 0, 0
	n = len(nums)
	for i in range(n):
		if nums[i] == 0:
			a += 1
		elif nums[i] == 1:
			b += 1
		else:
			c += 1

	for i in range(a):
		nums[i] = 0
	for i in range(a, a+b):
		nums[i] = 1	
	for i in range(a+b, n):
		nums[i] = 2
		
if __name__ == "__main__":
	import time
	nums = [2,0,2,1,1,0]
	begin = time.clock()
	sortColors(nums)
	elapsed = time.clock() - begin
	print("nums: ", nums, "time: ", elapsed)
