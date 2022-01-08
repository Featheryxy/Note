# Two Sum
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
# 并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]


# 建立hash map：将原list中的num 和 index 建立映射

def twoSum(nums, target):
        """
        :type numbs: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums)
        d = {}
        
        for x in range(n):
            difference_value = target - nums[x]
            
            if difference_value in d:
                return [d[difference_value], x]
            else:
                d[nums[x]] = x
    
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    List = twoSum(nums, target)
    print(List)
