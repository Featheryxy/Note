def select_sort(nums):
	n = len(nums)

	for i in range(n):
		tag = i
		for j in range(i+1, n):
			if nums[j] < nums[tag]:
				
				tag = j
		nums[i], nums[tag] = nums[tag], nums[i]
	
	return nums		
	
def 
	
from random import randint

nums = [randint(0, 10) for _ in range(10)]
print(nums)
print(select_sort(nums))
