# coding=gbk
# 给定一个数组，返回该数组所有可能的子集，包含空数组和它本身

# 输入: nums = [1,2,3]
# 输出: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# 考虑是用迭代的思想。
# 数组中只有一个数字时，返回空集合和数字本身.
# 再新加一个数字时，将原先的所有子集加上新的数字，就是包含新数字的子集，
# 保留之前不包含新数字的子集。这两个子集直接相加就是新的所有子集。
# 一样地当数组长度不断增加，我们不断往原来子集上迭代新的集合即可


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for i in range(len(nums)):
            for j in range(len(output)):
                output.append(output[j]+[nums[i]])
        return output

nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))
