# coding=gbk
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]

def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
	
if __name__ == "__main__":
	numbers = [2, 7, 11, 15]
	target = 9
	List = twoSum(numbers, target)
	print(List)
