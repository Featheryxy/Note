# Longest Substring Without Repeating Characters

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度

# 输入: "pwwkew"
# 输出: 3


# 双指针划定无重复的子串

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        
        l = 0
        r = 1
        max_len = 1
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                max_len = max(max_len, r-l)
            else:
                l += 1
                # r = r + 1
        
        return max_len
        
 
if __name__ == '__main__':
	s = "pwwkew"
	solution = Solution()
	print(solution.lengthOfLongestSubstring(s))
