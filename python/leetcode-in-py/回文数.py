# coding=gbk

# 输入: 121
# 输出: true


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)
        
        
if __name__ == "__main__":
	x = 121
	
	solution = Solution()
	print(solution.isPalindrome(x))
