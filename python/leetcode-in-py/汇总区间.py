
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        ret = []
        n = len(nums)
        
        i = 0
        while i < n:
            begin = i
            # i 指向标准序列的最后一位
            while i<n-1 and nums[i+1] == nums[i] + 1:
                i += 1
            print(i)
            if i == begin:
                ret.append(str(nums[i]))
            else:
                ret.append('{}->{}'.format(nums[begin], str(nums[i])))
            i += 1    
                
        return ret
 
nums = [0,1,2,4,5,7]
s = Solution()
print(s.summaryRanges(nums))


a = [i for i in range(1, 11)]
print(a)
i = 0
while i<9 and a[i+1] == a[i]+1:
	print(a[i])
	i+=1
	
	


