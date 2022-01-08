# coding=gbk
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组

# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
 '''       
        k = len(nums1)-1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k -= 1
        if n > 0:
            nums1[ :n] = nums2[ :n]
'''
        i = m-1
        j = n-1
        c = m+n-1

        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[c] = nums1[i]
                i -= 1
            else:
                nums1[c] = nums2[j]
                j -= 1
            c -= 1
        if j >= 0:
			num1[:j] = nums2[:j]


if __name__ == "__main__":
    nums1 = [2,2,0,0]
    m = 2
    nums2 = [1,5]       
    n = 2
    merge(nums1, m, nums2, n)
    print(nums1)
