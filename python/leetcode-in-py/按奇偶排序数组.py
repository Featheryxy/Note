# coding=gbk
# 给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素
# coding=gbk

# 输入：[3,1,2,4]
# 输出：[2,4,3,1]

# 
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        k = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[k], A[i] = A[i], A[k]
                k += 1
        return A  


class Solution1:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = A.copy()
        left = 0
        right = len(A) - 1
        for i in A:
            if i % 2:
                B[right] = i
                right -= 1
            else:
                B[left] = i
                left += 1
        return B
        

if __name__ == "__main__":
	A = [3,1,2,4]
	s1 = Solution()
	print(s1.sortArrayByParity(A))
	s2 = Solution1()
	print(s2.sortArrayByParity(A))

