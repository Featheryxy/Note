# coding=gbk

# 将数字转换成字符串进行处理

# 我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效
# 的，且和 X 不同的数。要求每位数字都要被旋转。

# 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋
# 转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理，除了这些以外其他的数字
# 旋转以后都不再是有效的数字。
# 现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？


class Solution:
	def rotatedDigits(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		count = 0
		for i in range(1, N+1):
			i = str(i)
			if '3' in i or '4' in i or '7' in i:
				continue
			if '2' in i or '5' in i or '6' in i or '9' in i:
				count += 1 
		return count
		

s = Solution()
print(s.rotatedDigits(10))
