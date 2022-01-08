# coding=gbk
# ����һ���Ѱ����������� ���������飬�ҵ�������ʹ���������֮�͵���Ŀ������
# ����Ӧ�÷����������±�ֵ index1 �� index2������ index1 ����С�� index2��

# ����: numbers = [2, 7, 11, 15], target = 9
# ���: [1,2]

def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
	
if __name__ == "__main__":
	numbers = [2, 7, 11, 15]
	target = 9
	List = twoSum(numbers, target)
	print(List)
