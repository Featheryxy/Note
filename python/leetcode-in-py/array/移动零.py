# coding=gbk

# ����һ������ nums����дһ������������ 0 �ƶ��������ĩβ��ͬʱ���ַ���Ԫ�ص����˳��
# ����: [0,1,0,3,12]
# ���: [1,3,12,0,0]

def moveZeroes(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	length = len(nums)
	k = 0
	for i in range(length):
		if nums[i] != 0:
			nums[k] = nums[i]
			k += 1
	while k < length:
		nums[k] = 0
		k += 1
		
		
if __name__ == "__main__":
	nums = [0,1,0,3,12]
	moveZeroes(nums)
	print(nums)
