#coding=gbk

# ����һ���������飬����Ҫ��ԭ��ɾ���ظ����ֵ�Ԫ�أ�ʹ��ÿ��Ԫ��ֻ����һ�Σ������Ƴ���������³��ȡ�
# ��Ҫʹ�ö��������ռ䣬�������ԭ���޸��������鲢��ʹ�� O(1) ����ռ����������ɡ�

# ���� nums = [0,0,1,1,1,2,2,3,3,4],
# ����Ӧ�÷����µĳ��� 5, ����ԭ���� nums ��ǰ���Ԫ�ر��޸�Ϊ 0, 1, 2, 3, 4��
# �㲻��Ҫ���������г����³��Ⱥ����Ԫ�ء�

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
		"""
				
        n = len(nums)
        if n == 0 or n == 1:
            return n
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k+1
		
		
if __name__ == "__main__":
	nums = [0,0,1,1,1,2,2,3,3,4]
	length = removeDuplicates(nums)
	print("length: ", length, "nums: ", nums[:length])
