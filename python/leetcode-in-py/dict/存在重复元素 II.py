# coding=gbk

# ����һ�����������һ������ k���ж��������Ƿ����������ͬ������ i �� j��ʹ
# �� nums [i] = nums [j]������ i �� j �Ĳ�ľ���ֵ���Ϊ k��
# ����: nums = [1,2,3,1], k = 3
# ���: true


def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1 and i - dict1[nums[i]] <= k:
                    return True
            else: # ��ʹ��else, �ٶȻ����
                dict1[nums[i]] = i
        return False
        
        
def containsNearbyDuplicate1(nums, k)
        dic ={}
        for i,j in enumerate(nums):
            if j in dic and abs(i-dic[j])<=k:
                return True
            dic[j] = i
        return False


if __name__ == "__main__":
	nums = [1,2,3,1]
	k = 3
	print(containsNearbyDuplicate(nums, k))
