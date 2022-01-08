# coding=gbk

# 输入: s = "paper", t = "title"
# 输出: true

def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hashmap = {}
        ismap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    print(i)
                    return False
            else:
                if t[i] in ismap:
                    return False
                hashmap[s[i]] = t[i]
                ismap[t[i]] = True
        print(hashmap, ismap)
        return True
        
        
        
if __name__ == "__main__":
	s = "aa"
	t = "ab"

	print(isIsomorphic(s, t))
