# coding=gbk
# ����һ���Ǹ��������� A������һ���� A ������ż��Ԫ����ɵ����飬����� A ����������Ԫ��
# coding=gbk

# ���룺[3,1,2,4]
# �����[2,4,3,1]

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

