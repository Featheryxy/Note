#coding=gbk

# ����һ������ nums ��һ��ֵ val������Ҫԭ���Ƴ�������ֵ���� val ��Ԫ�أ������Ƴ���������³��ȡ�
# ��Ҫʹ�ö��������ռ䣬�������ԭ���޸��������鲢��ʹ�� O(1) ����ռ����������ɡ�
# Ԫ�ص�˳����Ըı䡣�㲻��Ҫ���������г����³��Ⱥ����Ԫ�ء�

# ���� nums = [0,1,2,2,3,0,4,2], val = 2,
# ����Ӧ�÷����µĳ��� 5, ���� nums �е�ǰ���Ԫ��Ϊ 0, 1, 3, 0, 4��
# ע�������Ԫ�ؿ�Ϊ����˳��
# �㲻��Ҫ���������г����³��Ⱥ����Ԫ�ء�

def removeElement(nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""
	l = len(nums)
	k = 0
	for i in range(l):
		if nums[i] != val:
			nums[k] = nums[i]
			k += 1 
	return k
	
	
if __name__ == "__main__":
	nums = [0,1,2,2,3,0,4,2]
	val = 2
	length = removeElement(nums, val)
	print("length: ", length, "nums: ", nums[:5])
