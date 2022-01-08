# coding=gbk
# ����һ�����飬���ظ��������п��ܵ��Ӽ��������������������

# ����: nums = [1,2,3]
# ���: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# �������õ�����˼�롣
# ������ֻ��һ������ʱ�����ؿռ��Ϻ����ֱ���.
# ���¼�һ������ʱ����ԭ�ȵ������Ӽ������µ����֣����ǰ��������ֵ��Ӽ���
# ����֮ǰ�����������ֵ��Ӽ����������Ӽ�ֱ����Ӿ����µ������Ӽ���
# һ���ص����鳤�Ȳ������ӣ����ǲ�����ԭ���Ӽ��ϵ����µļ��ϼ���


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
