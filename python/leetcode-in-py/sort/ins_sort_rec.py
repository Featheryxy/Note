def ins_sort_rec(seq, i):
	if i == 0: return  # Base case -- do nothing
	ins_sort_rec(seq, i - 1)  # Sort 0..i-1
	j = i  # Start "walking" down
	while j>0 and nums[j] < nums[j-1]:
		nums[j], nums[j-1] = nums[j-1], nums[j]
		j -= 1
		

from random import randrange
nums = [randrange(100) for i in range(100)]
print(nums)
print("------------------Sorting---------------------")
ins_sort_rec(nums, len(nums)-1)
print(nums)
