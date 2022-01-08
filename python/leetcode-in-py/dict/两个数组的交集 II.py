# coding=gbk

# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]

def intersect(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	nums3 = []
	for num in nums1:
		if num in nums2:
			nums3.append(num)
			nums2.remove(num)
	return nums3


def intersect2(nums1, nums2):
	m, n = len(nums1), len(nums2)
	
	if m == 0 or n == 0:
		return []
	
	dicts = {}
	for num1 in nums1:
		# num1 已经存在在dicts中，
		if num1 in dicts:
			dicts[num1] += 1
		else:
			# num1 不在字典中，添加该字典
			dicts[num1] = 1
	
	ret = []
	for num2 in nums2:
		if num2 in dicts and dicts[num2] > 0:
			ret.append(num2)
			dicts[num2] -= 1
	
	return ret
			

	
if __name__ == "__main__":
	import time
	nums1 = [1,2,2,1]
	nums2 = [2,2]
	begin = time.clock()
	nums3 = intersect(nums1, nums2)
	elapsed = time.clock() - begin
	print("交集： ", nums3, "Time: ", elapsed)
	
	nums1 = [1,2,2,1]
	nums2 = [2,2]
	begin = time.clock()
	nums3 = intersect(nums1, nums2)
	elapsed = time.clock() - begin
	print("交集： ", nums3, "Time: ", elapsed)




