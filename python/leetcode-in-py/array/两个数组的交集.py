# coding=gbk
# 给定两个数组，编写一个函数来计算它们的交集

# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]

def intersection(nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		
		nums1 = list(set(nums1))
		nums2 = list(set(nums2))
		nums3 = []
		for i in range(len(nums1)):
			if nums1[i] in nums2:
				nums3.append(nums1[i])
		return nums3	
		
		
def intersection1(nums1, nums2):
	nums1 = set(nums1)
	nums2 = set(nums2)
	nums3 = nums1 & nums2
	return list(nums)
		
if __name__ == "__main__":
	import time
	
	nums1 = [1,2,2,1]
	nums2 = [2,2]
	begin1 = time.clock()
	a = intersection(nums1, nums2)
	elapsed = time.clock() - begin1
	begin2 = time.clock()
	b = intersection(nums1, nums2)
	elapsed2 = time.clock() - begin2
	print("a: ", a, "time: ", elapsed)
	print("b: ", b, "time: ", elapsed2)

	
		
