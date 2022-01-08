# Longest Palindromic Substring
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 求出每一个子串，判断每一个子串是否回文。


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not len(s):
            return ""        
        
        length = len(s)
        max_len = 1
        ret = ''
        
        for i in range(length):
            for j in range(i+1, length+1):
                palindrome = s[i:j]
                # print(palindrome)
                if palindrome == palindrome[::-1]:
                    if len(palindrome) > max_len:
                        max_len = len(palindrome)
                        ret = palindrome
        
        if ret == '':
            return s[0]
        else:
            return ret
        
        

if __name__ == "__main__":
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))
