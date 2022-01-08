# coding=gbk

# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使
# 得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
# 输入: nums = [1,2,3,1], k = 3
# 输出: true


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
            else: # 不使用else, 速度会更快
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
